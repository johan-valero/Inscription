# Partie 2 : inscription.py V2 (prérequis : logique conditionnelle, opérations logiques, exceptions)

from Fonction import email, categories, lire_annee

print("===================================================================")
print("Bienvenue sur le programme d'enregistrement des joueurs de Poudlard")
print("===================================================================")


# Gestion des erreurs : sur le nombre d'inscrit

while True:
    try:
        nbr_inscrit = int(input("Indiquez le nombre de personnes à inscrire \n"))
        break
    except ValueError:
        print("Veuillez saisir un nombre sous forme de chiffres")

liste_nouveaux = []

for i in range(nbr_inscrit):

    nom = str(input("Veuillez renseigner le nom ? \n"))
    prenom = str(input("Veuillez renseigner le prénom ? \n"))
    annee = lire_annee()
    adresse_email = email(nom, prenom)
    categorie = categories(annee)
    
    if categorie != "Non-admis":
        liste_nouveaux.append([prenom, nom, adresse_email, categorie])
    else:
      print("Ce profil n'est pas admissible")



print("=======================")
print("Liste des inscrits")
print("=======================")
for i in enumerate(liste_nouveaux):
    print(i)
