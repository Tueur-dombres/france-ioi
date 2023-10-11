L = int(input())
lettres = input()
N = int(input())

print(L**N)
for i in range(L**N):
    new_i = i
    retour = ""
    for k in range(N):
        retour = lettres[new_i%L] + retour
        new_i = (new_i-new_i%L)//L
    print(retour)