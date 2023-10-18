import sys
input = sys.stdin.readline

def nombre(nom):
    nb = sum(ord(l) - ord("A") for l in nom)
    while nb >= 10:
        nb = sum(int(ch) for ch in str(nb))
    return nb
        
def main():
    print(*[nombre(prenom) for prenom in input().split()])

main()