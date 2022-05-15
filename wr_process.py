import sys
import os

for i in range(1, len(sys.argv)):
    directory = str(sys.argv[i])
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        second = open("../wr/" + filename.split(".txt")[0], 'w')
        m = {}
        with open(f, "r") as reader:
            line = reader.readline()
            print("Processing " + filename)
            counter = 0
            while line:
                info = line.split()
                if len(info) > 2:
                    counter = info[2]
                else:
                    counter = counter + 1
                second.write(info[0] + "\t" + info[1] + "\t" + str(counter) + "\n")
                line = reader.readline()
        second.close()
