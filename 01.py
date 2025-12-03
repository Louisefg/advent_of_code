import numpy as np  

day = 1
test = 0

filename = f'txt/{day:02d}' + '_'*test + '.txt'
with open(filename, 'r') as file:
    data = file.readlines()
L = list()
for line in data :
    a = line.replace('\n','')
    L.append(a)


######### Part one

def turn(current, next):
    if next[0] == 'L':
        current -= int(next[1:])
    elif next[0] == 'R':
        current += int(next[1:])
    else:
        raise ValueError; "c'est la merde"
    return current%100

def rotate_sequence(L, d):
    N = 0
    for k in range(len(L)):
        d = turn(d, L[k])
        if d == 0:
            N += 1
    return N

d = 50
print('*********************')
print('       PART ONE      ')
print('*********************\n')
print('First password:', rotate_sequence(L, d),'\n')

######### Part two

def turn2(current, next):
    current_ = current
    v_next = int(next[1:])
    r, q = v_next % 100, v_next // 100
    if next[0] == 'L':
        current -= r
    elif next[0] == 'R':
        current += r
    else:
        raise ValueError; "c'est la merde"
    if current % 100 != current and current != 100 and current_ != 0: q += 1
    return q,  current%100

def rotate_sequence2(L, d):
    N = 0
    for k in range(len(L)):
        q, d = turn2(d, L[k])
        N += q
        if d == 0:
            N += 1        
    return N

d = 50
print('*********************')
print('       PART TWO      ')
print('*********************\n')
print('Second password:', rotate_sequence2(L, d),'\n')
