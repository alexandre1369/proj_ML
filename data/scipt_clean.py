import csv
import re


# Fonction pour remplacer les virgules dans les tableaux par des points-virgules
def replace_commas_in_arrays(line):
    # Utilisation d'une expression régulière pour repérer les tableaux [ ... ]
    return re.sub(r'\[([^\]]+)\]', lambda x: '[' + x.group(1).replace(',', ';') + ']', line)

# Lire et modifier le fichier CSV
input_file = '/home/alex/Bureau/Machin_learning/proj_ML/data/data.csv'  # Chemin absolu
output_file = '/home/alex/Bureau/Machin_learning/proj_ML/data/data_modifie.csv'

with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Lire le fichier ligne par ligne
    for row in reader:
        # Convertir la ligne en chaîne de caractères
        row_str = ','.join(row)
        # Remplacer les virgules à l'intérieur des tableaux par des points-virgules
        modified_row_str = replace_commas_in_arrays(row_str)
        # Re-séparer la ligne en colonnes et écrire dans le nouveau fichier
        modified_row = modified_row_str.split(',')
        writer.writerow(modified_row)

print("Fichier modifié avec succès !")
