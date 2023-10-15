nbPiles = int(input())
nbCartonsDansPile = list(map(int, input().split()))

total_cartons = sum(nbCartonsDansPile)
nbcartonsparpile = total_cartons//nbPiles
cp = 0
for carton in nbCartonsDansPile:
    if carton>nbcartonsparpile:
        cp+=carton-nbcartonsparpile
print(cp)