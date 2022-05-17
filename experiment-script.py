import sys
import os
import numpy as np
import math

directories_loc = sys.argv[1]
directories = ["caida/2004/", "caida/2005/", "caida/2006/", "caida/2007/", "oregon/2/", "oregon/3/"]
write_directory = sys.argv[2]

for directory in directories:
    directory = os.path.join(directories_loc, directory)
    write_dir = os.path.join(write_directory, directory)
    if not os.path.isdir(write_dir):
        os.mkdir(write_dir)
    for filename in os.listdir(directory):
        for space_frac in np.arange(0.01, 0.3005, 0.01):
            f = os.path.join(directory, filename)
            if os.path.isfile(f) and ".txt" not in f:
                print("Processing", f)
                data_file = open(f, "r")
                lines = data_file.readlines()
                space = math.ceil(space_frac * len(lines))

                write_file_name = write_directory + f + "_" + str(space)
                if not os.path.isfile(write_file_name):
                    open(write_file_name, 'a').close()

                data_file.close()
                command = "./run_ins.sh " + f + " " + write_file_name + " " + str(2 * space) + " 0.5"
                print(command)
                for i in range(10):
                    os.system(command)
