from random import randint
types_tries = sorted(list(set([randint(1,20) for _ in range (10)])))

def dicho(L, elt):
    a = 0
    b = len(L)
    while b > a + 1:
        m = (a + b) // 2
        if L[m] > elt:
            b = m
        else:
            a = m
    return a-1 if L[a] == elt else a

print(types_tries)
for pic in range(1,20):
    if pic > types_tries[0]:
        i = dicho(types_tries, pic)
        j = 0
        while j < len(types_tries) and pic > types_tries[j]:
            j+=1
        j-=1
        print(i == j, pic, i, j)