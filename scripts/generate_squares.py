import os

current_dir = os.path.dirname(os.path.abspath(__file__))
squares_world_dir = os.path.join(current_dir, "../worlds/squares")

for i in range(3, 41):
    file = open("{}/{}x{}.w".format(squares_world_dir, i, i), "w")
    file.write("Dimension: ({}, {})\n".format(i, i))
    file.write("Karel: (1, 1); east\n")
    file.write("BeeperBag: INFINITY\n")
