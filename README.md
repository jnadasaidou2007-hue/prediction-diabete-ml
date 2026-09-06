🔗 **[Voir l'application en ligne](https://prediction-diabete-ml-ipnyndt7dbg6qfjqsrmyyn.streamlit.app)**
# 🩺 Prédiction de la progression du diabète

Projet de Machine Learning (régression) réalisé dans le cadre de mon BTS SIO option IA — prédiction du score de progression du diabète chez un patient sur 1 an, à partir de 10 indicateurs médicaux.

## 🎯 Objectif

Prédire un score de progression de la maladie (variable continue) à partir de variables comme l'âge, le sexe, l'IMC, la tension artérielle et 6 mesures sanguines.

## 📊 Dataset

Dataset "Diabetes" intégré à scikit-learn : 442 patients, 10 variables explicatives déjà normalisées, aucune valeur manquante.

## 🛠️ Outils utilisés

- **Python**
- **pandas**, **numpy** — manipulation des données
- **matplotlib**, **seaborn** — visualisation et analyse des corrélations
- **scikit-learn** — modélisation (Régression Linéaire, Random Forest)
- **Streamlit** — interface interactive de prédiction
- **Jupyter Notebook** — environnement de développement

## 🔍 Démarche

1. Exploration des données (EDA) et analyse des corrélations
2. Séparation des données en train/test (80/20)
3. Entraînement et comparaison de deux modèles : Régression Linéaire et Random Forest
4. Évaluation avec MAE (erreur absolue moyenne) et R² (coefficient de détermination)
5. Sauvegarde du meilleur modèle et création d'une interface Streamlit

## 📈 Résultats

| Modèle | MAE | R² |
|---|---|---|
| Régression Linéaire | 42.79 | 0.45 |
| Random Forest | 44.05 | 0.44 |

La régression linéaire obtient de meilleurs résultats que le Random Forest sur ce dataset, ce qui montre qu'un modèle simple peut être plus adapté que des modèles plus complexes selon la nature des données.

## 🚀 Lancer l'application

```bash
pip install streamlit joblib scikit-learn pandas numpy
streamlit run app.py
```

L'application permet d'ajuster les 10 variables via des sliders et d'obtenir une prédiction instantanée du score de progression.

## 📁 Contenu du dépôt

- `projet_diabete_.ipynb` — notebook complet (analyse, modélisation, évaluation)
- `modele_diabete.pkl` — modèle entraîné sauvegardé
- `app.py` — application Streamlit
