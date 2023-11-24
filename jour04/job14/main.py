def my_long_word(longueur_min, phrase):
    mots = phrase.split()  # Diviser la phrase en une liste de mots
    mots_long = [mot for mot in mots if len(mot) > longueur_min]
    return mots_long

# Exemple d'utilisation
longueur_minimale = 4
phrase_test = "Le python est un langage de programmation puissant et polyvalent"
resultat = my_long_word(longueur_minimale, phrase_test)

print(f"Mots plus longs que {longueur_minimale} caractères dans la phrase:")
print(resultat)
