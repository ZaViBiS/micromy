import daemon


def requests():
    import requests
    import time

    requests.get('http://google.com')
    time.sleep(3600)


with daemon.DaemonContext():
    requests()
