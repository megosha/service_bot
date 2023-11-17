from main import bot
from service import check_speacker
from speakers import PASTOR


if not check_speacker():
    bot.send_message(PASTOR, '❗ Не забудьте выбрать проповедника на воскресенье ☝️')