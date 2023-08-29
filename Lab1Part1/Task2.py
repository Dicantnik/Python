import argparse
import operator
import math

parser = argparse.ArgumentParser()
parser.add_argument("func", type=str)
parser.add_argument('num', type=float, nargs='+')
lab = parser.parse_args()
try:
    if hasattr(operator, lab.func):
        func = getattr(operator, lab.func)
        print(func(*lab.num))
    else:
        func = getattr(math, lab.func)
        print(func(*lab.num))
except Exception:
    print('Something wrong')
