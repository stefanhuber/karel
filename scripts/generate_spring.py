import os
import random

current_dir = os.path.dirname(os.path.abspath(__file__))
spring_world_dir = os.path.join(current_dir, "../worlds/spring")

for i in range(1, 11):
    file = open("{}/spring_{}.w".format(spring_world_dir, i), "w")
    file.write("Dimension: (9, 10)\n")

    for x in range(2, 10):
        if random.random() > .5:
            height = random.randint(1, 8)
            for h in range(1, height + 1):
                file.write("Wall: ({}, {}); east\n".format(x, h))

    file.write("Karel: (1, 1); east\n")
    file.write("BeeperBag: INFINITY\n")
