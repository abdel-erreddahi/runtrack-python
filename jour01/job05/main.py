# Programme affichant l'alphabet en ordre inverse dans le terminal

for lettre in range(ord('z'), ord('a') - 1, -1):
    print(chr(lettre), end=' ')

print()  # Ajout d'une ligne vide à la fin