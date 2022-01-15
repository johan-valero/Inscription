import csv

#Gestion des erreurs : sur l'année de naissance

def lire_annee():
    try:
        annee = int(input("Veuillez renseigner l'année de naissance ? \n"))

    except ValueError:
        print("Veuillez renseigner l'année de naissance en chiffres")
        return lire_annee()
    
    if len(str(annee)) != 4:
        print("Votre année de naissance doit comporter 4 chiffres")
        return lire_annee()

    if annee <= 1982:
        print("Veuillez renseigner une année de naissance valide")
        return lire_annee()
    
    if annee > 2022:
        print("Veuillez renseigner une année de naissance valide")
        return lire_annee()
    
    return annee

#Catégorie d'un inscrit vis à vis de son age

def categories(annee):
    age = 2022 - int(annee)
    if 6 <= age < 12:
        return "Poussin"
    elif 12 <= age < 18:
        return "Cadet"
    elif 18 <= age < 24:
        return "Junior"
    elif 24 <= age < 30:
        return "Semi-pro"
    elif 30 <= age <= 40:
        return "Pro"
    else:
        return("Non-admis")
    
       
#adresse mail automatique

def email(nom,prenom):
    prenom = prenom.upper()
    nom = nom.lower()
    mail = str(prenom[0]+"."+nom+"@baton-rouge.fr")
    return mail

#fichier creation d'un csv


def create_csv(fichier, liste_nouveaux, mode = "a"):
    with open(fichier, mode, newline="") as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=" ")

        for nouveau in liste_nouveaux:
            spamwriter.writerow(nouveau)

