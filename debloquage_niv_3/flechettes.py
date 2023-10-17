size = int(input())
for i in list(range(size))+list(range(size-2,-1,-1)):
    j = -1
    while j < i-1:
        j+=1
        print(chr(ord("a")+j), end = "")
    j+=1
    print(chr(ord("a")+j)*(size*2-j*2-2), end = "")
    while j >= 0:
        print(chr(ord("a")+j), end = "")
        j-=1
    print()