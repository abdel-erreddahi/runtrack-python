# Programme affichant l'alphabet dans le terminal

for lettre in range(ord('a'), ord('z') + 1):
    print(chr(lettre), end=' ')

print()  # Ajout d'une ligne vide à la fin