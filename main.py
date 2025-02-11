import pandas as pd
import numpy as np
import re
from colorama import Fore, Style

# chargement et affichage des donnée
print(Fore.BLUE + "chargement et affichage des donnée", "\n" + Style.RESET_ALL)
data = pd.read_csv(r"C:\Users\Ingle\OneDrive\Bureau\OPIA\p2_AI\p2-arbres-fr.csv", sep=";")
print(data)

print(Fore.BLUE + "Affiche les premières lignes du DataFrame pour vérifier l'importation","\n" + Style.RESET_ALL)
print(data.iloc[3])


print(Fore.BLUE + "1- Affiche les 5 premières lignes", "\n" + Style.RESET_ALL)
print(data.head())

print(Fore.BLUE + "1- Affiche les 10 premières lignes (optionnel)", "\n" + Style.RESET_ALL)
print(data.head(10))

print(Fore.BLUE + "1- Affiche un résumé de la structure des données", "\n" + Style.RESET_ALL)
print(data.info())

print(Fore.BLUE + "1- Affiche des statistiques descriptives pour les colonnes numériques", "\n" + Style.RESET_ALL)
print(data.describe())

########################################################################################

# détecter les valeurs manquantes
print(Fore.BLUE + "détecter les valeurs manquantes", "\n" + Style.RESET_ALL)
print(data.isnull().sum())

# détecter les doublons
print(Fore.BLUE + "détecter les doublons", "\n" + Style.RESET_ALL)
print(data.loc[data['id'].duplicated(keep=False),:])

print(data.duplicated().sum())
print(data['id'].duplicated().sum())
print(data.drop(['id'], axis=1).duplicated().sum())

print(data.describe())





# # 1. Moyennes
# moyennes = data.mean()
# print("Moyennes :")
# print(moyennes)

# # 2. Médianes
# mediane = data.median()
# print("\nMédianes :")
# print(mediane)

# 3. Quantiles
# quantiles_25 = data.quantile(0.25)
# quantiles_50 = data.quantile(0.5)  # Médiane
# quantiles_75 = data.quantile(0.75)

# print("\nQuantiles (25%) :")
# print(quantiles_25)
#
# print("\nQuantiles (50%) - Médiane :")
# print(quantiles_50)
#
# print("\nQuantiles (75%) :")
# print(quantiles_75)
#
# # 4. Résumé statistique complet
# print("\nRésumé statistique complet :")
# print(data.describe())

