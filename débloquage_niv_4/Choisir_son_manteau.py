class Manteau:
    def __init__(self,inf,sup):
        self.inf = int(inf)
        self.sup = int(sup)
        self.inclus = []
        self.strinclus = []
        self.nbinclus = 0
    def __str__(self):
        return f"[inf : {self.inf}, sup : {self.sup}, inclus : {self.strinclus}, nbinclus : {self.nbinclus}]"
    def add(self,mantel):
        self.inclus += [mantel]
        self.strinclus += [str(mantel)]
        self.nbinclus += mantel.nbinclus + 1

nb = int(input())
L = []
for i in range(nb):
    inf,sup = input().split()
    L+=[Manteau(inf,sup)]
L = sorted(sorted(L,key=lambda mantel:mantel.sup),key=lambda mantel:-mantel.inf)

cps = []
print("\n".join(str(e) for e in L))

i=1
while i <len(L):
    
    i+=1
print(max(cps))