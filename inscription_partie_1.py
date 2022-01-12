# Partie 1 : inscription.py V1 (prérequis : input, parcours de liste/dict, opération math, opération littéraires)

from Fonction import email, categories

print("===================================================================")
print("Bienvenue sur le programme d'enregistrement des joueurs de Poudlard")
print("===================================================================")

nom = input("Veuillez renseigner le nom ? \n")
prenom = input("Veuillez renseigner le prénom ? \n")
annee = int(input("Veuillez renseigner l'année de naissance ? \n"))
categorie = categories(annee)
adresse_email = email(nom, prenom)

print("INSCRIPTION")
print("===========")
print("Prénom :", prenom)
print("Nom :", nom)
print("Email :", adresse_email)
print("Catégorie :", categorie)