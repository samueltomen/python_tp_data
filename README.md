# Prédiction du Type de Fontaine à Boire

Ce projet utilise un arbre de décision pour prédire le type de fontaine (à savoir "borne", "totem", etc.) en fonction du modèle et de la commune où elle se situe. Le jeu de données utilisé est "fontaines-a-boire.csv".

## Prérequis

- Python 3
- Bibliothèques Python : `pandas`, `scikit-learn`, `matplotlib`

Pour installer les dépendances, vous pouvez utiliser pip :

```bash
pip install pandas scikit-learn matplotlib
```

## Données Utilisées

Les données chargées sont issues du fichier `fontaines-a-boire.csv`. Ce fichier contient des informations sur des fontaines à boire telles que :

- `Type Objet` : Le type de la fontaine (par exemple, borne, totem).
- `Modèle` : Le modèle de la fontaine.
- `Commune` : La commune où la fontaine se situe.

Les colonnes sélectionnées pour l'analyse sont `Type Objet`, `Modèle` et `Commune`.

## Prétraitement des Données

Le prétraitement consiste à :

1. Charger le fichier CSV.
2. Sélectionner les colonnes pertinentes et retirer les lignes vides (`dropna()`).
3. Convertir les valeurs des colonnes `Type Objet`, `Modèle` et `Commune` en valeurs numériques grâce à `astype('category').cat.codes` pour rendre les données compatibles avec l'algorithme d'arbre de décision.

## Construction de l'Arbre de Décision

L'arbre de décision est construit en utilisant la classe `DecisionTreeClassifier` de `scikit-learn` avec une profondeur maximale de 4.

- Caractéristiques (`x`) : `Modèle` et `Commune`
- Cible (`y`) : `Type Objet`

L'arbre de décision est ensuite entraîné pour prédire le type de fontaine en fonction du modèle et de la commune.

## Visualisation de l'Arbre de Décision

L'arbre de décision est visualisé à l'aide de la fonction `plot_tree` de `matplotlib`. La figure montre comment le type de fontaine est déterminé en fonction des caractéristiques `Modèle` et `Commune`.

```python
plt.figure(figsize=(50, 50))
plot_tree(clf, filled=True, feature_names=['Modèle', 'Commune'], class_names=class_names_str)
plt.title("Arbre de décision représentant le type de fontaines à boire en fonction du modèle et de la commune")
plt.show()
```

L'arbre présenté met en évidence les différentes décisions prises en fonction des caractéristiques fournies.

## Utilisation

Pour exécuter le script, assurez-vous que le fichier `fontaines-a-boire.csv` est présent dans le répertoire de travail, puis lancez le script.

L'arbre de décision sera affiché dans une nouvelle fenêtre, présentant la classification des fontaines à boire selon les caractéristiques fournies.

## Auteurs

Samuel

## Licence

Ce projet est sous licence libre. Vous êtes libre de l'utiliser, le modifier et le redistribuer.

