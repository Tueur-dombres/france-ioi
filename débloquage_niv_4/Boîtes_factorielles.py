nb = int(input())
i=2
L = []
while nb != 0:
    L+=[nb%i]
    nb = nb//i
    i+=1
print(len(L))
print(" ".join(str(e) for e in L))