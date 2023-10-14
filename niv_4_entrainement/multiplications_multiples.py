N =int(input())
cp = 1
for _ in range(N):
    cp*=int(input()[-4:])
    cp = int(str(cp)[-4:])
print("{:04d}".format(cp))