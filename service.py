import os
# from pathlib import Path

import telebot

from speakers import SPEAKERS


# BASE_DIR = Path(__file__).resolve().parent
# speaker_file = str(BASE_DIR / 'files' / 'speaker.txt')


def valid_user_by_pk(pk:str):
    return pk.isdigit() and int(pk) in range(len(SPEAKERS))


def valid_user_by_tid(tid):
    for speaker in SPEAKERS:
        for k, v in speaker.items():
            if tid == v.get("t_id"):
                return tid
        else:
            continue


def render_speakers():
    kboard = telebot.types.InlineKeyboardMarkup(row_width=6)
    for speaker in SPEAKERS:
        for k, v in speaker.items():
            kboard.add(telebot.types.InlineKeyboardButton(text=v.get("name"), callback_data=k))
    return kboard


def save_speaker(speaker:str):
    with open("speaker.txt", "w") as file:
        file.write(speaker)


def get_speaker_by_pk(pk):
    for s in SPEAKERS:
        if list(s.keys())[0] == pk:
            speaker = s.get(pk)
            if speaker:
                return speaker.get("t_id"), speaker.get("name")
    return None, None


def read_speaker():
    if os.path.isfile("speaker.txt"):
        with open("speaker.txt", "r") as file:
            pk = file.read()
            return get_speaker_by_pk(pk)
    return None, None


def clear_speaker():
    if os.path.isfile("speaker.txt"):
        os.remove("speaker.txt")

