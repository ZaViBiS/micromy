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

