nbJoursPossibles, nbSeancesAnnulables = map(int, input().split())
joursPossibles = list(map(int, input().split()))
jours_possibles_dafilee = []
nb_jours_impossibles = [0]+[joursPossibles[i+1]-joursPossibles[i]-1 for i in range(nbJoursPossibles-1)]

i_debut = i_fin = 0
annule = 0
while i_fin < nbJoursPossibles:
    annule+=nb_jours_impossibles[i_fin]
    while annule>nbSeancesAnnulables:
        i_debut+=1
        annule-=nb_jours_impossibles[i_debut]
    jours_possibles_dafilee+=[i_fin-i_debut+1]
    i_fin+=1

print(max(jours_possibles_dafilee)+nbSeancesAnnulables)