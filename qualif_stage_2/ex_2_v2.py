nbArbres, a, b, c = map(int,input().split())
intervalles = [[0,10**9,0]] #A,B,val
for _ in range(nbArbres):
    X,Y = map(int,input().split())
    i = 0
    new_intervalles = []
    for i in range(len(intervalles)):
        A,B,val = intervalles[i]
        if B < X:
            new_intervalles.append([A,B,val + a])
        elif Y < A:
            new_intervalles.append([A,B,val + c])
        elif X <= A and B <= Y:
            new_intervalles.append([A,B,val + b])
        elif A < X <= B <= Y:
            new_intervalles.append([A,X-1,val+a])
            new_intervalles.append([X,B,val+b])
        elif X <= A <= Y < B:
            new_intervalles.append([A,Y,val+b])
            new_intervalles.append([Y+1,B,val+c])
        elif A < X and Y < B:
            new_intervalles.append([A,X-1,val+a])
            new_intervalles.append([X,Y,val+b])
            new_intervalles.append([Y+1,B,val+c])
        else:
            print("error","A:",A,"B:",B,"X:",X,"Y:",Y)
            break
    intervalles = new_intervalles
print(max([e[2] for e in intervalles]))