def removed(ine='NO'):
    special_characters = ['/', '\\', '|', '*', '?', '>', '<', ':', '"']

    for x in special_characters:
        int = ine.replace(x, '')
    return ine


def internet_connect():  # Проверка подключения к интернету
    from requests import get

    try:
        get('http://info.cern.ch/')
    except:
        return False
    return True


def logger(FILE_NAME, text):
    f = open('log/' + FILE_NAME, 'a')
    f.write(str(text) + '\n')
    f.close()


def normal_datetime():  # [2021/03/10 09:25:43]
    from datetime import datetime

    data = datetime.now()

    return f'[{data.year}/{data.month}/{data.day} {data.hour}:{data.minute}:{data.second}]'
