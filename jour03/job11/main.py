def time_to_text(minutes):
    # Calculer le nombre d'heures et de minutes
    heures = minutes // 60
    minutes_restantes = minutes % 60

    # Construire la chaîne de caractères
    if heures == 0:
        temps_texte = f"{minutes_restantes} minutes"
    elif heures == 1:
        temps_texte = f"1 heure et {minutes_restantes} minutes"
    else:
        temps_texte = f"{heures} heures et {minutes_restantes} minutes"

    # Afficher la chaîne de caractères en console
    print(temps_texte)

# Exemple d'utilisation
time_to_text(75)  # Affichera "1 heure et 15 minutes"
time_to_text(120)  # Affichera "2 heures"
time_to_text(45)  # Affichera "45 minutes"

