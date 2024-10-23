# Calculatrice Simple

## Description
Ce projet est une calculatrice simple développée en Python. La calculatrice permet d'effectuer des opérations mathématiques de base telles que l'addition, la soustraction, la multiplication, et la division. Des fonctionnalités bonus avancées sont également proposées.
L'utilisateur doit entrer l'opération qu'il souhaite réaliser sur des nombres.

## Fonctionnalités
### Opérations de base
- **Addition** : Prend deux nombres en entrée et renvoie leur somme.
- **Soustraction** : Prend deux nombres en entrée et renvoie leur différence.
- **Multiplication** : Prend deux nombres en entrée et renvoie leur produit.
- **Division** : Prend deux nombres en entrée et renvoie leur quotient.

### Fonctionnalités Bonus
- **Modulo** : Renvoie le reste de la division entre deux nombres.
- **Exponentielle** : Renvoie la base élevée à la puissance d'un exposant.
- **Logarithme** : Calcule le logarithme d'un nombre selon une base donnée (base naturelle par défaut).
- **Historique des calculs** : Permet de consulter les opérations précédentes.
- **Interface CLI avancée** : Offre une interface utilisateur en ligne de commande interactive.
- **Racine carrée** : Calcule la racine carrée d'un nombre.
- **Fonctions trigonométriques** : Implémente des fonctions de sinus, cosinus, et tangente.
- **Conversion d'unités** : Convertit entre différentes unités (par exemple, km en miles).

## Structure du Projet
Chaque fonctionnalité de la calculatrice est développée dans un fichier Python séparé :
- `addition.py` : Contient la fonction d'addition.
- `soustraction.py` : Contient la fonction de soustraction.
- `multiplication.py` : Contient la fonction de multiplication.
- `division.py` : Contient la fonction de division.
- `calculatrice.py` : Contient la fonction de calculatrice
- `main.py` : Point d'entrée principal du programme, contient l'interface utilisateur CLI qui appelle les différentes fonctions.

### Fonctionnalités Bonus (Fichiers associés)
- `modulo.py`
- `exponentiation.py`
- `logarithm.py`
- `cli_interface.py`
- `history.py`
- `sqrt.py`
- `trigonometry.py`
- `unit_conversion.py`

## Workflow Git
1. **Branche principale (`main`)** : La branche stable contenant le code final.
2. **Branche de développement (`develop`)** : Pour tester les fonctionnalités avant de les fusionner dans `main`.
3. **Branches par fonctionnalité** : Chaque membre de l'équipe développe une fonctionnalité dans une branche distincte. Exemples : `feature/addition`, `feature/division`.

## Instructions pour Cloner le Dépôt
1. Cloner le dépôt sur votre machine locale :
    ```bash
    git clone https://github.com/nom-utilisateur/calculatrice-simple.git
    ```
2. Créez une nouvelle branche pour ajouter ou modifier une fonctionnalité :
    ```bash
    git checkout -b feature/nom-de-la-fonctionnalité
    ```
3. Après avoir implémenté la fonctionnalité, poussez les modifications :
    ```bash
    git add .
    git commit -m "Ajout de la fonctionnalité de [nom]"
    git push origin feature/nom-de-la-fonctionnalité
    ```
4. Ouvrez une Pull Request pour fusionner la branche dans `develop`.

## Auteurs
- Michael
- Antoine
- David
(MAD)
## Licence
Ce projet est sous licence MAD corp.