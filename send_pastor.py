from main import bot
from service import render_speakers
from speakers import PASTOR

bot.send_message(PASTOR, 'Кто проповедует?', reply_markup=render_speakers())
