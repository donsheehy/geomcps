def write_config():
    top = input("Top folder: ")
    ext = input("Data file extension: ")
    meta1 = yn2tf(input("Save folder names for metadata? Y/N: "))
    if meta1 == 't':
        folderchars = input("Number of folder characters to save? Leave blank for all: ")
    else:
        folderchars = 0
    meta2 = yn2tf(input("Save file names for metadata? Y/N: "))
    if meta2 == 't':
        filechars = input("Number of file characters to save? Leave blank for all: ")
    else:
        filechars = 0
    mode = yn2tf(input("Use debug mode? Y/N: "))
    stream_to_write = '\n'.join([top, ext, str(folderchars), str(filechars), mode])

    try:
        f = open(".config", "wt")
    except Exception as e:
        f = open(".config", "xt")
        del e
    f.write(stream_to_write)
    f.close()


def yn2tf(i):
    if ((i.upper() == 'N') | (i.upper() == 'NO') | (i.upper() == 'FALSE')):
        return 'f'
    return 't'


def read_config():
    f = open(".config")
    top = f.readline()
    if top == "":
        f.close()
        write_config()
        read_config()
    result = []
    result.append(top)
    for i in range(4):
        result.append(f.readline())
    f.close()
    return result


if __name__ == "__main__":
    write_config()
