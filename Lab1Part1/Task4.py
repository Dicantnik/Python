import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-W", type=int)
parser.add_argument("-w", type=int, nargs="+")
lab = parser.parse_args()

def bagpack(W, w):
    capacity = {}
    for c in range(W+1):
        capacity[(0, c)] = 0
    for i in range(1, len(w)+1):
        for c in range(W+1):
            if w[i-1] <= c:
                capacity[(i, c)] = max(capacity[(i-1, c)], w[i-1] + capacity[(i-1, c-w[i-1])])
            else:
                capacity[(i, c)] = capacity[(i-1, c)]
    return capacity[(len(w), W)]

print(bagpack(lab.W, lab.w))


