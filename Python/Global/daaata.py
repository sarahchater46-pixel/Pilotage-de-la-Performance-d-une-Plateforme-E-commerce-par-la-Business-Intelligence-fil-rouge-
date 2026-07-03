import pandas as pd

# 1. Lecture des fichiers (adaptez les noms des fichiers selon votre ordinateur)
# On utilise sep='\t' car vos données semblent séparées par des tabulations (TSV)
df_sales = pd.read_csv('Details_Maroc.csv', sep='\t')
df_customers = pd.read_csv('Orders_Maroc.csv', sep='\t')

# Si vos fichiers sont au format Excel (.xlsx), utilisez plutôt cette ligne :
# df_sales = pd.read_excel('mon_fichier.xlsx', sheet_name='Sheet1')
# df_customers = pd.read_excel('mon_fichier.xlsx', sheet_name='Sheet2')

# 2. On affiche les premières lignes pour vérifier que tout est bien lu
print("--- Aperçu des ventes ---")
print(df_sales.head())

print("\n--- Aperçu des clients ---")
print(df_customers.head())
