from mpiaa.timer import time_me
from mpiaa.util import *
from mpiaa.funcs import *


if __name__ == "__main__":
    file = "../record_gen/records_1e3.txt"
    print(algorithm(file))