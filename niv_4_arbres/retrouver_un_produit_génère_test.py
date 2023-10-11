from random import randint
N = int(input())
R = int(input())
print(N)
print(" ".join([str(randint(0,N)) for _ in range(N)]))
print(R)
print(" ".join([str(randint(1,N)) for _ in range(R)]))