# Partie 1 : inscription.py V1 (prérequis : input, parcours de liste/dict, opération math, opération littéraires)

#Catégorie d'un inscrit vis à vis de son age

def categories(annee):
    age = 2022 - int(annee)
    if 6 <= age < 12:
        return "poussin"
    elif 12 <= age < 18:
        return "cadet"
    elif 18 <= age < 24:
        return "junior"
    elif 24 <= age < 30:
        return "semipro"
    elif 30 <= age <= 40:
        return "pro"
    else:
        print("non-admis")

#adresse mail automatique

def email(nom,prenom):
    mail = str(prenom[0]+"."+nom+"@baton-rouge.fr")
    return mail


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