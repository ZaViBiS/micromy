import os


def ogg(inputname=None, outputname=None):
    os.system(
        'ffmpeg -i {0} -acodec copy -vn {1}'.format(inputname, outputname))


def mp4(inputname=None, outputname=None):
    os.system('ffmpeg -i {0}  {1}'.format(inputname, outputname))


def connect(video=None, audio=None, outputname=None):
    os.system(
        'ffmpeg -i {0} -i {1} -map 0:v -map 1:a -c copy {2}.webm'.format(video, audio, outputname))
    os.system('ffmpeg -i {0}.webm {1}'.format(outputname, outputname))
