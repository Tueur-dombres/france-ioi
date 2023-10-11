nbArbres, a, b, c = map(int,input().split())
intervalles = [[0,10**9,0]] #A,B,val
for _ in range(nbArbres):
    X,Y = map(int,input().split())
    i = 0
    while i < len(intervalles):
        A,B,val = intervalles[i]
        if B < X:
            intervalles[i][2] = val + a
            i += 1
        elif Y < A:
            intervalles[i][2] = val + c
            i += 1
        elif X <= A and B <= Y:
            intervalles[i][2] = val + b
            i += 1
        elif A < X <= B <= Y:
            intervalles = intervalles[:i] + [[A,X-1,val+a]] + [[X,B,val+b]] + intervalles[i+1:]
            i+=2
        elif X <= A <= Y < B:
            intervalles = intervalles[:i] + [[A,Y,val+b]] + [[Y+1,B,val+c]] + intervalles[i+1:]
            i+=2
        elif A < X and Y < B:
            intervalles = intervalles[:i] + [[A,X-1,val+a]] + [[X,Y,val+b]] + [[Y+1,B,val+c]] + intervalles[i+1:]
            i+=3
        else:
            print("error","A:",A,"B:",B,"X:",X,"Y:",Y)
            break
print(max([e[2] for e in intervalles]))