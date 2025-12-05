import numpy as np
from copy import deepcopy

day = 5
test = 0

filename = f"txt/{day:02d}" + "_" * test + ".txt"
with open(filename, "r") as file:
    data = file.readlines()
L_ingredients = list()
Fresh_ing_IDs = list()
for line in data:
    line = line.replace("\n", "").split("-")
    if len(line) == 2:
        Fresh_ing_IDs.append([int(line[0]), int(line[1])])
    elif line[0] != "":
        L_ingredients.append(int(line[0]))


def is_fresh(ing, Fresh_ing_IDs):
    for [a, b] in Fresh_ing_IDs:
        if ing >= a and ing <= b:
            return True
    return False


def main1(L_ingredients, Fresh_ing_IDs):
    N = 0
    for ing in L_ingredients:
        N += is_fresh(ing, Fresh_ing_IDs)
    return N


print("*********************")
print("       PART ONE      ")
print("*********************\n")
print("Number of fresh ingredents:", main1(L_ingredients, Fresh_ing_IDs), "\n")


def merge_two_list(L1, L2):
    if min(L1[1], L2[1]) < max(L1[0], L2[0]) - 1:
        # ranges don't overlap
        return L1, L2
    else:
        # ranges are overlapping
        return [min(L1[0], L2[0]), max(L1[1], L2[1])]


def pop_and_run(L):
    # pop the first element and merge it with others
    L_ = deepcopy(L)
    range1 = L.pop(0)
    for range2 in L_[1:]:
        merge = merge_two_list(range1, range2)
        if type(merge) != tuple:
            range1 = merge
            # print(range2)
            L.remove(range2)
    return range1


def entire_list(L):
    # pop and run for all lines, until convergence
    L_ = []
    while L_ != L:
        L_ = deepcopy(L)
        for k in range(len(L)):
            new_range = pop_and_run(L)
            L = L + [new_range]
    return L


def get_N(L):
    N = 0
    for [a, b] in L:
        N += (b - a) + 1
    return N


print("*********************")
print("       PART TWO      ")
print("*********************\n")
L = deepcopy(Fresh_ing_IDs)
New_ing_IDs = entire_list(L)
print("Number of fresh IDs:", get_N(New_ing_IDs), "\n")
