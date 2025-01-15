def etalonnage(nom_fichier):
    etalon = 0
    
    with open(nom_fichier, "r") as fichier:
        for ligne in fichier:
            liste = []
            for c in ligne.strip():
                if c.isdigit():
                    liste.append(c)
                    if len(liste) == 1:
                        premchif = liste[0]
                        derchif = liste[0]
                        valeur_etalonnage = int(premchif + derchif)
                    if len(liste) >= 2:
                        premchif = liste[0]
                        derchif = liste[-1]
                        valeur_etalonnage = int(premchif + derchif)
            etalon += valeur_etalonnage
                
    return etalon


nom_fichier = "document.txt"
reslt = etalonnage(nom_fichier)
print("La somme totale des valeurs d'étalonnage est :", reslt)
