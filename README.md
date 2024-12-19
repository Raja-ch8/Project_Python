# Project_Python

# **Bienvenue !**

Dans ce dépôt, nous allons explorer différents projets déployés avec Python pour vous aider à mieux comprendre et maîtriser ce langage de programmation. Chaque projet a été pensé pour vous permettre d'apprendre par la pratique.

Dans un premier temps, nous allons découvrir le premier projet, qui concerne la création d'un jeu simple et amusant : Pierre-Papier-Ciseaux. Ce projet vous permettra de vous familiariser avec les bases de Python, comme les entrées utilisateur, les conditions, et la génération aléatoire.

### **1. Projet : Pierre-Papier-Ciseaux.**
- **Objectif :** Créer un script Python qui permet de jouer au jeu classique "Pierre-Papier-Ciseaux" contre l'ordinateur.

- **Description :**

    * L'utilisateur choisit entre Pierre, Papier ou Ciseaux.
    * L'ordinateur génère un choix aléatoire.
    * Le script compare les choix et détermine le gagnant.
    * Le jeu continue jusqu'à ce que l'utilisateur décide d'arrêter.
    * **Bonus :** Des *emojis* ont été intégrés pour rendre le jeu plus visuel et interactif.

- **Compétences abordées :**

   - Manipulation des entrées utilisateur avec *input()*.
   - Utilisation des conditions (*if*, *elif*, *else*).
   - Génération de valeurs aléatoires avec la bibliothèque *random*.
   - Boucles (*while*) pour permettre plusieurs manches.
   - Intégration d'*emojis* grâce à la bibliothèque emoji pour améliorer l'expérience utilisateur. (YOU WIN :trophy: or YOU LOSE :thumbsdown:)

![Capture d’écran 2024-12-17 à 10 29 18](https://github.com/user-attachments/assets/73abd10c-2858-4069-bda2-14fc51f3845a)

:warning: : Si vous souhaitez utiliser des emojis dans votre script Python, vous devez d'abord installer la bibliothèque `emoji` et l'importer dans votre code.

```bash
pip install emoji==1.7
```

- **Importer la bibliothèque dans votre script Python :** Après avoir installé la bibliothèque, vous devez l'importer dans votre code Python comme suit :

```python
import emoji
```

- **Utilisation des emojis :** Vous pouvez maintenant utiliser la fonction emoji.emojize() pour ajouter des emojis dans votre code. Par exemple :

```python
print(emoji.emojize(" YOU WIN :trophy:"))
```

- Création de l'environnement virtuel avec **python3 -m venv vent**

```bash
python3 -m venv vent
```
Lorsque tu crées un environnement virtuel avec la commande python3 -m venv vent, cela crée un dossier (appelé ici vent) qui contient une copie isolée de l'interpréteur Python et un gestionnaire de paquets spécifique à cet environnement.

Cet environnement virtuel te permet de gérer les bibliothèques et les dépendances spécifiques à ton projet sans affecter ton installation globale de Python.

###### **Avantages :**

**Isolation :** Tu peux avoir différentes versions des bibliothèques pour chaque projet sans conflit.


### **2. Projet : Quiz Game**

J'ai créé un projet en utilisant Python pour développer un Quiz Game, un jeu interactif qui permet de tester ses connaissances en répondant à différentes questions.

L'idée principale du projet est d'offrir une façon simple et amusante d'apprendre, en exploitant les capacités de Python. Le jeu inclut :

Des questions à choix multiples parmi lesquelles choisir.
Une vérification automatique des réponses, pour savoir immédiatement si la réponse est correcte.
Des éléments visuels interactifs, comme des émojis, pour rendre le jeu plus engageant.
La possibilité de rejouer ou de quitter à tout moment.


# **3. Projet : Login System**

1 . Installare Flask 

```bash 
pip install flask
```

