L, C = map(int,input().split())
table  = [list(map(int,input().split())) for _ in range(L)]
table2 = [[int(not e) for e in table[0]]]+[[0 for _ in range(C)] for _ in range(1,L)]
table2[2][2]=1

for i in range(1,L):
    for j in range(C):
        if table[i][j]==0:
            table2[i][j]=1+table2[i-1][j]
valid = 0
for i in range(L-1,-1,-1):
    reads = []
    reads_count = []
    for j in range(C):
        a=table2[i][j]
        if a>valid:
            if not reads or reads[-1]!=a:
                c = [reads_count[b] for b in range(len(reads)) if reads[b]>a]
                reads_count +=[max(c)] if c else [0]
                reads += [a]

            x = 0
            old_val = valid
            while x < len(reads):
                if a>=reads[x]:
                    reads_count[x]+=1
                    if reads_count[x]>= reads[x]:
                        valid = reads[x]
                    x+=1
                else:
                    reads.pop(x)
                    reads_count.pop(x)
                    
            if valid != old_val:
                x=0
                while x<len(reads):
                    if reads[x]<=valid:
                        reads.pop(x)
                        reads_count.pop(x)
                    else:
                        x+=1
        else:
            reads = []
            reads_count = []
print(valid)