def moyenne (note1,note2,note3):
    result = (note1 + note2 + note3) / 3
    return result
    
note1=int(input('Enter premiere note:'))
note2=int(input('Enter deuxieme note:'))
note3=int(input('Enter troisieme note:'))

moyenne_etudiant = moyenne(note1,note2,note3)

if moyenne_etudiant <= 20 and moyenne_etudiant >= 15 :
    print(f"{moyenne_etudiant} : Tres bon eleve")
elif moyenne_etudiant <= 14 and moyenne_etudiant >= 11 :
    print(f"{moyenne_etudiant} :Bon eleve")
elif moyenne_etudiant <= 10 and moyenne_etudiant >= 8 :
    print(f"{moyenne_etudiant} :Eleve moyen")
else:
    print(f"{moyenne_etudiant} :Eleve devant faire des efforts") 

    

