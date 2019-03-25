import random
import os

files = []
for i in range(3):
    for j in range(2):
        if i == 0:
            subdir = "sample_a"
        elif i == 1:
            subdir = "sample_b"
        else:
            subdir = "sample_c"
        if j == 0:
            file = "run1.csv"
        else:
            file = "run2.csv"
        files.append(os.path.join(subdir, file))

for file in files:
    f = open(file, "wt")
    v0 = random.randint(0, 50)
    x0 = random.randint(0, 300)
    totaltime = random.randint(1, 21)
    g = random.randint(90, 106)
    for t in range(0, 10):
        time = t * totaltime / 10.0
        x = x0 + v0 * time - g / 10.0 * time ** 2
        y = v0 - g / 10.0 * time
        writeme = str(time)
        writeme += ","
        writeme += str(x)
        writeme += ","
        writeme += str(y)
        writeme += "\n"
        f.write(writeme)
    f.close()
    print("File ", file, " done.")
