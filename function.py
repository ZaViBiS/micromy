import os

import pafy


def download(url):
    '''audio_downloder = youtube_dl.YoutubeDL(ydl_opts)
    return audio_downloder.extract_info(url)'''
    video = pafy.new(url)
    video.getbestaudio().download('file/')
    '''audiostreams = video.audiostreams
    for a in audiostreams:
        print(a.bitrate, a.extension, a.get_filesize())'''
    return video.title

'''
def name_and_rename(trash):
    name = f"{trash['title']}-{trash['id']}.mp3"
    new_name = f"{trash['title']}.mp3".replace('*', '')
    os.rename(name, new_name)
    return new_name
'''

def ffmpeg_convert_webm_to_m4a():
    filename = os.listdir('file/')[0]
    new_name = filename[:-5] + '.m4a'
    os.system(f'ffmpeg -i file/\'{filename}\' -vn \'{new_name}\' -y')
    return new_name, filename
