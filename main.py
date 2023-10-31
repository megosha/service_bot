import os

from dotenv import load_dotenv
import telebot

import service
from speakers import PASTOR, MEDIA

load_dotenv()


BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    if service.valid_user_by_tid(message.chat.id):
        bot.reply_to(message, "Бот для опроса названия проповеди успешно запущен!👋"
                              "\n\n ⚠️Внимание! Когда бот спросит у вас название, "
                              "не пишите ничего, кроме темы проповеди в ответе ⚠️")
    else:
        return None


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    if str(call.message.chat.id).startswith('-'):
        return None
    try:
        bot.answer_callback_query(callback_query_id=call.id)
        # если чат с пастором и ответ - кто проповедует
        if call.message.chat.id == PASTOR and service.valid_user_by_pk(call.data):
            # сохранить в файл id проповедника для отправки в субботу сообщения
            service.save_speaker(call.data)
            # переслать проповедника media
            bot.send_message(MEDIA, f'Проповедует {call.data}, {service.get_speaker_by_pk(call.data)}')
    except Exception as e:
        bot.send_message(MEDIA, f'‼️Ошибка выбора проповедника:  {e}')
        bot.send_message(PASTOR, f'❌ Ошибка выбора проповедника. Работаем над исправлением ошибки.')
    else:
        bot.send_message(PASTOR, f'Проповедник {service.get_speaker_by_pk(call.data)[1]} успешно выбран.')
    finally:
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.id, reply_markup=None)

# если ответ - тема проповеди, переслать проповедника media
@bot.message_handler(content_types=['text',])
def message_reply(message):
    if service.valid_user_by_tid(message.chat.id):
        try:
            bot.forward_message(MEDIA, message.chat.id, message_id=message.id)
        except Exception as e:
            bot.send_message(MEDIA, f'‼️Ошибка отправки темы проповеди:  {e}.\n\n'
                                    f'Не забудьте удалить файл с проповедником после проверки.')
        else:
            bot.reply_to(message, f'✅ Ваше сообщение успешно передано')
            service.clear_speaker()




if __name__ == '__main__':
    bot.polling(none_stop=True)