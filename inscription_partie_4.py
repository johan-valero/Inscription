import os
import csv
from Fonction import create_csv

chemin_de_base = "./inscriptions/"
noms_fichiers = os.listdir(chemin_de_base)
total_inscrits = []
total_inscrits_par_categorie = {}

for nom_fichier in noms_fichiers:
  if (os.path.isfile(chemin_de_base + nom_fichier)):
    csvfile = open(chemin_de_base + nom_fichier, "r", newline="")
    spamreader = csv.reader(csvfile, delimiter=" ")

    for row in spamreader:
      if row not in total_inscrits:
        total_inscrits.append(row)

for inscrit in total_inscrits:
  categorie = inscrit[-1]

  if not categorie in total_inscrits_par_categorie:
    total_inscrits_par_categorie[categorie] = []
  
  total_inscrits_par_categorie[categorie].append(inscrit)

for categorie in total_inscrits_par_categorie:
  print(categorie, ":", str(len(total_inscrits_par_categorie[categorie])), "inscrits")

create_csv("./inscrits_total.csv", total_inscrits, "w")