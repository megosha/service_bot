from main import bot
from service import read_speaker, valid_user_by_tid
from speakers import MEDIA


tid, name = read_speaker()
if valid_user_by_tid(tid):
    theme = bot.send_message(tid,
                     'Здравствуйте!\n'
                     '🔖 Пришлите места Писания для сегодняшнего служения,если ещё не сделали этого.', )
else:
    bot.send_message(MEDIA, f'Проповедник неизвестен. Нет мест Писания.')

