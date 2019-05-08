import os


def write_config():
    # print(os.getcwd())
    top = input("Top folder: ")
    topPath = os.path(top)
    os.chdir(topPath)
    ext = input("Data file extension: ")
    meta1 = yn2tf(input("Save folder names for metadata? Y/N: "))
    if meta1 == 't':
        folderchars = input("Number of folder characters to save? Leave blank for max (64): ")
        if folderchars == '':
            folderchars = 64
    else:
        folderchars = 0
    meta2 = yn2tf(input("Save file names for metadata? Y/N: "))
    if meta2 == 't':
        filechars = input("Number of file characters to save? Leave blank for max (64): ")
        if filechars == '':
            filechars = 64
    else:
        filechars = 0
    mode = yn2tf(input("Use debug mode? Y/N: "))
    stream_to_write = '\n'.join([ext, str(folderchars), str(filechars), mode])

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


def read_config(filename):
    f = open(filename)
    result = f.readlines()
    # top = f.readline()
    # if top == "":
    #     f.close()
    #     write_config()
    #     read_config()
    # result = []
    # result.append(top)
    # result.append(f.readlines())
    f.close()
    return result


if __name__ == "__main__":
    write_config()
