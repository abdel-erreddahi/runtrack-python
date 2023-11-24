def tri_bulles(arr):
    n = 0
    while n < len(arr):
        m = 0
        while m < len(arr) - n - 1:
            if arr[m] > arr[m + 1]:
                arr[m], arr[m + 1] = arr[m + 1], arr[m]
            m += 1
        n += 1

def arrondir_liste(arr):
    i = 0
    while i < len(arr):
        arr[i] = int(arr[i] + 0.5)
        i += 1

# Liste initiale
ma_liste = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

# Arrondir les nombres dans la liste
arrondir_liste(ma_liste)

# Tri à bulles
tri_bulles(ma_liste)

# Afficher la liste résultante
print("Liste arrondie et triée :", ma_liste)
