from multiprocessing import Pool
import time
import os
from operator import add

def add_number(x):
    return x

if __name__ == '__main__':
    pool = Pool(processes=4)              # start 4 worker processes
    print map(add_number, range(10))