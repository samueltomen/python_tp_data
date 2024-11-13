import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

#

# Charger les données
data = pd.read_csv('fontaines-a-boire.csv', sep=';')

# Sélectionner les colonnes
foutain_data = data[['Type Objet', 'Modèle', 'Commune']].dropna()

# Encodage des colonnes afin de les rendre compatibles avec l'arbre de décision car il prend en charge uniquement les
# valeurs numériques
foutain_data['Type Objet'] = foutain_data['Type Objet'].astype('category').cat.codes
foutain_data['Modèle'] = foutain_data['Modèle'].astype('category').cat.codes
foutain_data['Commune'] = foutain_data['Commune'].astype('category').cat.codes

# Définir les caractéristiques (x) et la cible (y)
x = foutain_data[['Modèle', 'Commune']].values
y = foutain_data['Type Objet'].values

# Création de l'arbre de décision
clf = DecisionTreeClassifier(random_state=0, max_depth=8)
clf = clf.fit(x, y)

# Transformer les noms de classes en chaînes de caractères
class_names = foutain_data['Type Objet'].astype('category').cat.categories
class_names_str = [str(class_name) for class_name in class_names]

# Afficher l'arbre de décision
plt.figure(figsize=(50, 50))
plot_tree(clf, filled=True, feature_names=['Modèle', 'Commune'], class_names=class_names_str)
plt.title("Arbre de décision représentant le type de fontaines à boire en fonction du modèle et de la "
          "commune")
plt.show()