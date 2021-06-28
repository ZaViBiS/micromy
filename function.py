import os

import youtube_dl

from config import ydl_opts


def download(url):
    audio_downloder = youtube_dl.YoutubeDL(ydl_opts)
    return audio_downloder.extract_info(url)


def name_and_rename(trash):
    name = f"{trash['title']}-{trash['id']}.mp3"
    new_name = f"{trash['title']}.mp3"
    os.rename(name, new_name)
    return new_name

