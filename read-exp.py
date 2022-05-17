import sys
import os
import numpy as np
import math
import statistics

directories = ["caida/2004/", "caida/2005/", "caida/2006/", "caida/2007/", "oregon/2/", "oregon/3/"]
write_directory = sys.argv[1]
count_dir = sys.argv[2]

for directory in directories:
    write_dir = os.path.join(write_directory, directory)
    graphs_to_space = {}
    for filename in os.listdir(write_dir):
        f = os.path.join(write_dir, filename)
        print("Processing", f)
        graph = filename.split("_")[0] + "_" + filename.split("_")[1]
        if not graph in graphs_to_space:
            graphs_to_space[graph] = {}
        space = int(math.ceil(int(filename.split("_")[-1])))
        data_file = open(f, "r")
        lines = data_file.readlines()
        errors = []
        for i in range(10):
            errors.append(float(lines[i]))

        graphs_to_space[graph][space] = (statistics.mean(errors), statistics.stdev(errors))

for key in graphs_to_space:
    graph = key
    p = graph + ", "
    spaces = list(graphs_to_space[graph].keys())
    spaces.sort()

    for space in spaces:
        p += str(graphs_to_space[graph][space][0]) + ", " + str(graphs_to_space[graph][space][1]) + ", "

    print("WaitingRoom" + ", " + p)
