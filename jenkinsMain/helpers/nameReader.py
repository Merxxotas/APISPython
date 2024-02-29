def readName():
    file = open("GeneratedName.txt", "r+")
    # file.write(name + "\n")
    return list(map(lambda x: x.strip('\n'), file.readlines()))
    # file.close()
