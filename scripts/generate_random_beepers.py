import os
import random

current_dir = os.path.dirname(os.path.abspath(__file__))
invert_world_dir = os.path.join(current_dir, "../worlds/invert")

for i in range(1, 11):
    file = open("{}/invert_{}.w".format(invert_world_dir, i), "w")
    file.write("Dimension: (6, 10)\n")

    for x in range(1, 7):
        for y in range(1, 11):
            if random.random() > .5:
                file.write("Beeper: ({}, {}); 1\n".format(x, y))

    file.write("Karel: (1, 1); east\n")
    file.write("BeeperBag: INFINITY\n")
