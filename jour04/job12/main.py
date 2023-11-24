def tri_bulles(L):
    n = len(L)
    i = 0

    while i < n:
        j = 0
        while j < n - i - 1:
            if L[j] > L[j + 1]:
                # Échanger les éléments si l'élément actuel est plus grand que le suivant
                L[j], L[j + 1] = L[j + 1], L[j]
            j += 1
        i += 1

# Exemple d'utilisation
ma_liste = [64, 34, 25, 12, 22, 11, 90]
tri_bulles(ma_liste)

print("Liste triée :", ma_liste)