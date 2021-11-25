from random import randint
from stanfordkarel import *


def main():
    pass


if __name__ == "__main__":
    i = randint(3, 41)
    run_karel_program("squares/{}x{}".format(i, i))
