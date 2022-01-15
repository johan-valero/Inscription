# Partie 1 : inscription.py V1 (prérequis : input, parcours de liste/dict, opération math, opération littéraires)

from Fonction import email, categories

print("===================================================================")
print("Bienvenue sur le programme d'enregistrement des joueurs de Poudlard")
print("===================================================================")

def donnee():
    nom = input("Veuillez renseigner le nom ? \n")
    prenom = input("Veuillez renseigner le prénom ? \n")
    annee = int(input("Veuillez renseigner l'année de naissance ? \n"))
    categorie = categories(annee)
    adresse_email = email(nom, prenom)


    if categorie != "Non-admis":

        print("===========")
        print("INSCRIPTION")
        print("===========")
        print("Prénom :", prenom)
        print("Nom :", nom)
        print("Email :", adresse_email)
        print("Catégorie :", categorie)
        
    else:
        print("Ce profil n'est pas admissible")
        while True:
            enregistrer = input("Faire un autre enregistrement ? Oui : (o) - Non : (n) \n")
            print("réponse :", enregistrer)
            if enregistrer == "n":
                print("non")
                break
                print("oui")
            elif enregistrer == "o":
                return donnee()
            else:
                print("Veuillez saisir o ou n ") 
        
donnee()
