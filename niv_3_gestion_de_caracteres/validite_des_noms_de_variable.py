import sys
input = sys.stdin.readline

def is_valide(variable):
    if not ("a"<=variable[0].lower()<="z" or variable[0]=="_"):
        return False
    
    for elt in variable[1:]:
        if not ("a"<=elt.lower()<="z" or elt=="_" or elt.isdigit()):
            return False
        
    return True

def main():
    nblivres = int(input())
    retour = []

    for _ in range(nblivres):
        var = input()[:-1]
        retour.append("YES" if is_valide(var) else "NO")
        
    print("\n".join(retour))

main()