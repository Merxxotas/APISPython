from jenkinsMain.helpers.name import Name

NAMES = []


def generateName(name):
    data = Name(name, len(NAMES) + 1)
    NAMES.append(str(data))
