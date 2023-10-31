from main import bot
from service import read_speaker, valid_user_by_tid, clear_speaker
from speakers import MEDIA


tid, name = read_speaker()
if valid_user_by_tid(tid):
    theme = bot.send_message(tid,
                     'Здравствуйте! Напишите название проповеди в ответном сообщении.'
                     '\n ⚠️Не пишите ничего, кроме темы в ответе ⚠️', )
else:
    bot.send_message(MEDIA, f'Проповедник неизвестен')
    clear_speaker()


