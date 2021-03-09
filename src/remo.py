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
    from time import sleep

    while True:

        try:
            if get('https://habr.com/') == '<Response [200]>':
                break
            break
        except:
            sleep(10)
