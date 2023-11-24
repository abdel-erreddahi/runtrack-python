def supprimer_doublons(liste):
    liste_sans_doublons = []

    for element in liste:
        # Vérifier si l'élément n'est pas déjà présent dans la nouvelle liste
        if element not in liste_sans_doublons:
            # Ajouter l'élément uniquement s'il n'est pas déjà présent
            liste_sans_doublons.append(element)

    return liste_sans_doublons

# Exemple d'utilisation
L = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
resultat = supprimer_doublons(L)

print("Liste originale :", L)
print("Liste sans doublons :", resultat)
