TOKEN = '783312094:AAECzfAdp1sHAktngrWi8CqkaHrV7LZwthQ'
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
