def moyenne(note1, note2, note3):
    resultat = (note1 + note2 + note3) / 3
    return resultat


note1 = float(input("Entrez la première note : "))
note2 = float(input("Entrez la deuxième note : "))
note3 = float(input("Entrez la troisième note : "))

moyenne_etudiant = moyenne(note1, note2, note3)

if moyenne_etudiant >= 15:
    print("Très bon élève")
elif moyenne_etudiant >= 11:
    print("Bon élève")
elif moyenne_etudiant >= 8:
    print("Élève moyen")
elif moyenne_etudiant >= 0:
    print("Élève devant faire des efforts")


