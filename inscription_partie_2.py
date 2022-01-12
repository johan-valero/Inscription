# Partie 2 : inscription.py V2 (prérequis : logique conditionnelle, opérations logiques, exceptions)

from Fonction import email, categories

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

#Gestion des erreurs : sur l'année de naissance

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


#Liste des inscrits

    adresse_email = email(nom, prenom)
    categorie = categories(annee)
    liste_nouveaux.append([prenom, nom, adresse_email, categorie])


print("=======================")
print("Liste des inscrits")
print("=======================")
for i in enumerate(liste_nouveaux):
    print(i)
