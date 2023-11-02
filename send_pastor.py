from main import bot
from service import render_speakers, clear_speaker
from speakers import PASTOR


clear_speaker()
bot.send_message(PASTOR, 'Здравствуйте!\n 📣 Выберите проповедника на воскресенье из списка ниже:', reply_markup=render_speakers())
