import numpy as np  

day = 2
test = 0

filename = f'txt/{day:02d}' + '_'*test + '.txt'
with open(filename, 'r') as file:
    data = file.readlines()
L = list()
for line in data :
    L.append(line.replace('\n','').split(','))
L = [(int(a),int(b)) for a,b in [item.split('-') for sublist in L for item in sublist]]


######### Part one

def compute_bounds(a,b):
    low = a
    alpha = int(np.log10(a)) 
    beta = int(np.log10(b))
    if alpha == beta and alpha%2 == 0:
        return 0,0
    low = a if alpha%2 == 1 else 10**(alpha+1)
    up = b if beta%2 == 1 else 10**beta-1
    return low, up

def f(a):
    if a == 0: 
        return 0,0
    nb_digits = int(np.log10(a)) + 1
    return int(a // 10**(nb_digits/2)), nb_digits/2

def g(a,low, b,n):
    aa = a + a*10**n
    L = []
    while aa <= b :
        a += 1
        if aa <= b and aa >= low: L.append(int(aa))
        aa = a + a*10**n
    return L

def main1(L):
    N = 0
    for k in range(len(L)):
        low, up = compute_bounds(L[k][0],L[k][1])
        (demi_low, nb) = f(low)
        l = g(demi_low, low, up, nb)
        try: N += sum(l)
        except: pass
    return N





def get_N_digits(a):
    return int(np.log10(a)) + 1

def repete_number(number,n_rep,n):
    assert get_N_digits(number) == n; "Bad news"
    return sum([number*10**(k*n) for k in range(n_rep)])

def get_L(a,b,n):

    n_min, n_max = get_N_digits(a), get_N_digits(b)

    if n_min == n_max and n_min % n != 0 :
        return []
    if n_min % n != 0 and n_max % n != 0 :
        return []

    L = list()
    
    # Case n=1
    if n == 1:
        for k in range(n_min, n_max+1):
            To_test = [repete_number(i,k,1) for i in range(1,10)]
            for test in To_test:
                if test >= a and test <= b:
                    L.append(test)
        return L

    # Compute the number of repetition of the scheme of size n
    n_rep = n_min // n if n_min % n == 0 else n_max // n 
    if n_rep == 0: return []

    c = min([(a % 10**((k+1)*n)) // 10**(k*n) for k in range(n_rep) if get_N_digits((a % 10**((k+1)*n)) // 10**(k*n))==n]) if n_min == n_rep*n else 10**(n-1)
    rep_c = repete_number(c, n_rep, n)
    while rep_c <= b :
        if rep_c >= a and rep_c <= b:
            L.append(rep_c)
        c += 1
        if get_N_digits(c) != n:
            rep_c = b + 1
        else :
            rep_c = repete_number(c, n_rep, n)
    
    return L
        




print('*********************')
print('       PART ONE      ')
print('*********************\n')
print('First invalid IDs:', main1(L),'\n')



# ######### Part two



invalids_ID = list()
for (a,b) in L:
    invalids_ID_l = list()
    N_a, N_b = get_N_digits(a), get_N_digits(b)
    for n in range(1, max(N_a//2, N_b//2)+1):
        invalids_ID_l += get_L(a,b,n)
    invalids_ID += set(invalids_ID_l)


print('*********************')
print('       PART TWO      ')
print('*********************\n')
print('Second invalid IDs:', sum(invalids_ID),'\n')

# 54446379166 too high 