def removed(ine=None):
    ine = ine.replace('/', '')
    ine = ine.replace('\\', '')
    ine = ine.replace('|', '')
    ine = ine.replace('*', '')
    ine = ine.replace('?', '')
    ine = ine.replace('>', '')
    ine = ine.replace('<', '')
    ine = ine.replace(':', '')
    ine = ine.replace('"', '')

    return ine


def internet_connect():  # Проверка подключения к интернету
    from requests import get

    try :
        get('http://info.cern.ch/')
    except :
        return False
    return True


def logger(text):
    f = open('log.txt', 'a')
    f.write(str(text))
    f.close()


def normal_datetime(): # [2021/03/10 09:25:43]
    from datetime import datetime

    data = datetime.now()

    return '[{0}/{1}/{2} {3}:{4}:{5}]'.format(data.year, data.month, data.day, data.hour, data.minute, data.second)
