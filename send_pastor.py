from main import bot
from service import render_speakers
from speakers import PASTOR

bot.send_message(PASTOR, 'Здравствуйте! Выберите проповедника на воскресенье из списка ниже 👇', reply_markup=render_speakers())
