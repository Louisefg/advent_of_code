import numpy as np
from copy import deepcopy

day = 4
test = 0

filename = f"txt/{day:02d}" + "_" * test + ".txt"
with open(filename, "r") as file:
    data = file.readlines()
L = list()
for line in data:
    L.append(line.replace("\n", ""))
L = [[k for k in line] for line in L]


######### Part one
def get_neighbors(i, j, L):
    n = list()
    # Left
    if j > 0:
        n.append(L[i][j - 1])
    # Right
    if j < len(L[0]) - 1:
        n.append(L[i][j + 1])
    # Up
    if i > 0:
        n.append(L[i - 1][j])
    # Down
    if i < len(L) - 1:
        n.append(L[i + 1][j])
    # Up-right
    if i > 0 and j < len(L[0]) - 1:
        n.append(L[i - 1][j + 1])
    # Up-left
    if i > 0 and j > 0:
        n.append(L[i - 1][j - 1])
    # Down-right
    if i < len(L) - 1 and j < len(L[0]) - 1:
        n.append(L[i + 1][j + 1])
    # Down-left
    if i < len(L) - 1 and j > 0:
        n.append(L[i + 1][j - 1])
    return n


def is_accessible(i, j, L):
    N = get_neighbors(i, j, L)
    s = len([k for k in N if k == "@"])
    return s < 4


print("*********************")
print("       PART ONE      ")
print("*********************\n")


N = 0
for i in range(len(L)):
    for j in range(len(L[0])):
        if L[i][j] == "@":
            N += is_accessible(i, j, L)


print("Number of paper that can be accessed by a forklift:", N, "\n")

######### Part two


def process_grid(L):
    N = 0
    L_ = deepcopy(L)
    for i in range(len(L)):
        for j in range(len(L[0])):
            if L[i][j] == "@":
                N += is_accessible(i, j, L)
                if is_accessible(i, j, L):
                    L_[i][j] = "."
    return N, L_


print("*********************")
print("       PART TWO      ")
print("*********************\n")

L_ = deepcopy(L)
L__ = []
N = 0
while L_ != L__:
    L__ = deepcopy(L_)
    n, L_ = process_grid(L__)
    N += n


print("Total number of paper that can be accessed by a forklift:", N, "\n")
