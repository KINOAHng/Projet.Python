## Title : Projet de Gestion de fichiers - Python




## Description 

Ce projet est une application de gestion de fichiers en Python qui permet de :

- lire le contenu du fichier texte 
- Ecrire du texte dans un fichiers 
- Analyser le fichier pour rechercher des mots-clés spécifiques.
- Générer un fichier pour enregistrer les actions (lecture, écriture, recheche) Réalisées par l'utilisateur.
## Fonctionnalité

1. Lceture de fichiers:
- Permet de lire et d'afficher le contenu d'un fichiers texte existant.
2. Ecriture dans un fichier:
- Permet d'ajouter du texte à un fichier existant ou de créer un nouveau fichier
3. Rechercher des mots-clés:
- Permet de rechercher un mot ou une expressions dans le fichier et retourne la listes des lignes ou ils apparaissent.
4. Fichier de log:
- Un fichiers de logs est généré pour enregistrer les actions effectuées, notament la lecture, l'écriture et les résultats de recherches. 

## Installation

## Prérequis 

- Python3.x doit etre installé sur votre machine.

- Vous pouvez installer les bibliothèques supplémentaires si nécessaire avec:

``pip install -r requirements.txt``

Si le fichier requirements.txt n'existe pas encore, vous pouvez le créer avec :

``pip freeze > requirements.txt``

## Etapes pour cloner le projet

1. Clonez ce dépot Git sur votre machine locale : 

https://github.com/KINOAHng/Projet.Python.git

2. Accédez au répertoire du projet:

``cd /FileManager/Python``

## Excéxuter l'application

Une fois les dépenadnces installées, Vous pouvez exécuter le fichier Python pour démarrer le gestionnaire de fichiers:

``Python main.py``


    
## Explication du code

1. Def Read_file(self)
- Ouvre le fichier en mode lecture et affiche son contenu.
- Enregistre l'action dans le fichier de logs
2. Def Write_to_file(self, data)
- Ouvre le fichier en mode ajout et ajoute une nouvelle ligne avec le texte fourni.
- Enregistre l'action dans le fichier de logs
 3. Def Count_lines(self)
- Permet de retourner le nombre de ligne dans le fichier
4. Def search_keyword(self, keywork)
- Ouvre le fichier en mode lecture, cherche le mot-clé dans les lignes, et affiche les résultats.
- Enregistre l'action dans le fichier de logs.                                                                                                             

## Usage 

1. Lecture d'un fichier
pour lire le contenu d'un fichier, utilisez la commande suivante dans le fichier
``python main.py read log.txt``
2. Ecriture dans un fichier
Pour ecrire du texte dans un fichier ou en créer un nouveau :
``python main.py write log.txt < Texte_à_ajouté>``
3. Analyse de fichier (recherche de mot-clé)
Pour analyser un fichier et rechercher un mot-clé:
``python main.py search <log.txt>`` "ERROR"
Cela affichera le nombre d'occurrences du mot "ERROR" dans le fichier spécifié.

## Gestion des erreurs
- Si un fichier est introuvable lors de la lecture ou de la recherche, une erreur sera affichée et enregistrée dans le fichier log.
- Si le programme n'a pas les droits d'écriture ou de lecture, cela sera aussi enregistré dans le fichier log.

## Structure du projet

 projet-gestionnaire-fichiers/
│
├── main.py                 # Fichier principal contenant la logique du gestionnaire de fichiers
├── app.log                 # Fichier log généré automatiquement
├── requirements.txt         # Liste des dépendances Python
└── README.md                # Documentation du projet

## Contribuer:
Les contributions sont les bienvenues ! Si vous souhaitez proposer des modifications, ouvrez une pull request ou créez une issue pour discuter de vos suggestions. 😊

![alt text](https://picsum.photos/200/300)
