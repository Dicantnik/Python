import argparse


parser = argparse.ArgumentParser()

parser.add_argument('int1', type=int)
parser.add_argument('act', type=str)
parser.add_argument('int2', type=int)
lab = parser.parse_args()


def calculate(int1, int2, act):
    if act == '+':
        return int1 + int2
    elif act == '-':
        return int1 - int2
    elif act == '*':
        return int1 * int2
    elif act == '/':
        try:
            return int1 / int2
        except ZeroDivisionError:
            return 'You can not divide by zero'
    else:
        return 'Wrong action'


print(calculate(lab.int1, lab.int2, lab.act))
