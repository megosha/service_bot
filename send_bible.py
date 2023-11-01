from main import bot
from service import read_speaker, valid_user_by_tid, clear_speaker
from speakers import MEDIA


tid, name = read_speaker()
if valid_user_by_tid(tid):
    theme = bot.send_message(tid,
                     'Здравствуйте! Пришлите места Писания для проповеди на сегодняшнее служение.', )
else:
    bot.send_message(MEDIA, f'Проповедник неизвестен. Нет мест Писания.')
    clear_speaker()


