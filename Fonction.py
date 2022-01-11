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
        print(" Non-admis")

#adresse mail automatique

def email(nom,prenom):
    mail = str(prenom[0]+"."+nom+"@baton-rouge.fr")
    return mail