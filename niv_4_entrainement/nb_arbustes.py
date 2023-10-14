L,C = map(int,input().split())
cp = 0
for _ in range(L):
    cp+=input().count("#")
print(cp)
