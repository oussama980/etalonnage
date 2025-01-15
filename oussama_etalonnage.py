def etalonnage(nom_fichier):
    somme_totale = 0
    
    with open(nom_fichier, "r") as file:
        for line in file:
            chiffres = []
            for char in line.strip():
                if char.isdigit():
                    chiffres.append(char)
                    if len(chiffres) == 1:
                        premier = chiffres[0]
                        dernier = chiffres[0]
                        valeur_etalonnage = int(premier + dernier)
                    if len(chiffres) >= 2:
                        premier = chiffres[0]
                        dernier = chiffres[-1]
                        valeur_etalonnage = int(premier + dernier)
            somme_totale += valeur_etalonnage
                
    return somme_totale


nom_fichier = "document.txt"
reslt = etalonnage(nom_fichier)
print("La somme totale des valeurs d'étalonnage est :", reslt)
