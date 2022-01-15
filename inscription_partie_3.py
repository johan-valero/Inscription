# Partie 3 : inscription.py V3 (fichiers, bibliothèques)

from datetime import date
from Fonction import email, categories, lire_annee
from Fonction import create_csv

print("===================================================================")
print("Bienvenue sur le programme d'enregistrement des joueurs de Poudlard")
print("===================================================================")

liste_nouveaux = []

def inscription():
  nom = input("Veuillez renseigner le nom ? \n")
  prenom = input("Veuillez renseigner le prénom ? \n")
  annee = lire_annee()
  adresse_email = email(nom, prenom)
  categorie = categories(annee)

  if categorie != "Non-admis":
    liste_nouveaux.append([prenom, nom, adresse_email, categorie])
  else:
      print("Ce profil n'est pas admissible")

  while True:
    nouveau = input("Faire un autre enregistrement ? Oui : (o) - Non : (n) \n")
    if nouveau == "n":
      break
    elif nouveau == "o":
      return inscription()
    else:
      print("Veuillez saisir o ou n ")

inscription()
print("=======================")
print("Liste des inscrits")
print("=======================")
for i in enumerate(liste_nouveaux):
    print(i)


#creation fichier csv

date_ = str(date.today())
create_csv("inscrits-"+ date_ +".csv", liste_nouveaux)