# Partie 3 : inscription.py V3 (fichiers, bibliothèques)

from datetime import date
from Fonction import email, categories
from Fonction import create_csv

print("===================================================================")
print("Bienvenue sur le programme d'enregistrement des joueurs de Poudlard")
print("===================================================================")


liste_nouveaux = []

def inscription():
  nom = str(input("Veuillez renseigner le nom ? \n"))
  prenom = str(input("Veuillez renseigner le prénom ? \n"))

  while True:
    try:
      annee = int(input("Veuillez renseigner l'année de naissance ? \n"))

    except ValueError:
      print("Veuillez renseigner l'année de naissance en chiffres")

    if len(str(annee)) != 4:
      print("Votre année de naissance doit comporter 4 chiffres")   

    if 1930 <= annee <= 2022:
      break
    else:
      print("Veuillez renseigner une année de naissance valide")
  
  adresse_email = email(nom, prenom)
  categorie = categories(annee)
  liste_nouveaux.append([prenom, nom, adresse_email, categorie])

  while True:
    nouveau = input("Faire un autre enregistrment ? Oui : (o) - Non : (n) \n")
    if nouveau == "n":
      break
    elif nouveau == "o":
      return inscription()
    else:
      print("Veuillez saisir o ou n ")

inscription()
print("=======================")
print("Liste des inscriptions")
print("=======================")
for i in enumerate(liste_nouveaux):
    print(i)


#creation fichier csv

date_ = str(date.today())
create_csv("inscrits-"+ date_ +".csv", liste_nouveaux)
