musique = input()
retour = []
i = 0

while i < len(musique) - 1:
    if musique[i] != musique[i+1]:
        if not retour or retour[-1] != musique[i]:
            retour += [musique[i]]
        else:
            retour.pop()
        i+=1
    else:
        i+=2

if i == len(musique) - 1:
    if not retour or retour[-1] != musique[i]:
        retour += [musique[i]]
    else:
        retour.pop()

print("".join(retour))