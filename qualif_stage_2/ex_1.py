nbArticlesAchetes, nbArticlesScannes = map(int, input().split())
achats = list(map(int, input().split()))
scans = list(map(int, input().split()))


i_achats = i_scans = 0
retour = set()

while i_achats < nbArticlesAchetes:
    if achats[i_achats] == scans[i_scans]:
        i_achats += 1
        i_scans += 1
    else:
        retour.add(scans[i_scans])
        i_scans += 1
if i_scans < nbArticlesScannes:
    retour.add(scans[-1])
print(" ".join([str(e) for e in sorted(retour)]))