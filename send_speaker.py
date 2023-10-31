from main import bot
from service import read_speaker, valid_user_by_tid
from speakers import MEDIA

def forward_theme(message):
    bot.forward_message(MEDIA, message.chat.id, message_id=message.chat.id)

tid, name = read_speaker()
if valid_user_by_tid(tid):
    theme = bot.send_message(tid,
                     'Здравствуйте! Напишите название проповеди в ответном сообщении.'
                     '\n ⚠️Не пишите ничего, кроме темы в ответе ⚠️', )
    # bot.register_next_step_handler(theme, forward_theme)
    # bot.send_message(tid, 'Название отправлено')
else:
    bot.send_message(MEDIA, f'Проповедник неизвестен')


