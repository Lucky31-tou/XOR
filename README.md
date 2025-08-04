# Chiffrement XOR en Python

Ce projet est une implémentation simple de l'algorithme de chiffrement XOR en Python.

Une particularité de ce script est qu'il n'utilise volontairement que très peu de fonctions natives de Python. La plupart des fonctions de base (comme `len`, `join`, `reverse`, etc.) et des structures de données (`Pile`, `File`) ont été réimplémentées dans le fichier `native_py.py` à des fins éducatives.

## 🚀 Fonctionnalités

- **Chiffrement** : Chiffre un message texte à l'aide d'une clé via l'opération logique XOR.
- **Déchiffrement** : Déchiffre le message chiffré en utilisant la même clé.
- **Interface interactive** : Une interface en ligne de commande simple pour saisir le message et la clé.
- **Dépendances "maison"** : Utilise une bibliothèque personnalisée (`native_py.py`) qui recrée des fonctions Python de base à partir de zéro.

## 🛠️ Structure du Projet

Le projet est divisé en deux fichiers principaux :

1.  `xor.py`:
    - Contient la logique principale de chiffrement et de déchiffrement.
    - Gère les entrées de l'utilisateur pour le message et la clé.
    - Orchestre le processus complet : chiffrement puis déchiffrement pour vérification.

2.  `native_py.py`:
    - Une bibliothèque "maison" qui réimplémente des fonctions Python courantes (`len`, `join`, `reverse`, `append`, `pop`, etc.).
    - Contient également des implémentations de base pour les structures de données `Pile` (Stack) et `File` (Queue).
    - L'objectif de ce fichier est de démontrer la compréhension des algorithmes fondamentaux.

## 📋 Prérequis

- Python 3.x

Aucune bibliothèque externe n'est nécessaire, car toutes les fonctions requises sont implémentées dans `native_py.py`.

## ⚙️ Utilisation

1.  Assurez-vous que les fichiers `xor.py` et `native_py.py` se trouvent dans le même répertoire.

2.  Exécutez le script principal depuis votre terminal :
    ```bash
    python xor.py
    ```

3.  Suivez les instructions à l'écran :
    - Saisissez le message que vous souhaitez chiffrer.
    - Saisissez une clé de chiffrement (8 caractères maximum).

### Exemple de session

```
Votre message : Hello World!
Votre clé : secret
19 20 3 3 10 75 23 10 8 3 13 74 
Hello World!
```

Le script affichera d'abord la version chiffrée du message (une série de nombres), puis le message déchiffré pour prouver que le processus fonctionne correctement.

---

*Ce projet a été créé pour illustrer les principes du chiffrement XOR et la réimplémentation d'algorithmes de base en Python.*

