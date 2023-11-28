def cesar(chaine: str, decal: int) -> str:
    sortie = ''
    for k in range(0, len(chaine)):
        sortie += chr((ord(chaine[k]) + decal - 97) % 26 + 97)
    return sortie


message="abcdefghijklmnopqrstuvwxyz"
print(f"message: {message}")
print(f"message chiffré: {cesar(message, 3)}")
print(f"message déchiffré: {cesar(cesar(message, 3), -3)}")