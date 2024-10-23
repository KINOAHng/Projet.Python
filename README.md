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

pip install -r requirements.txt 

## Etapes pour cloner le projet

1. Clonez ce dépot Git sur votre machine locale : 

https://github.com/KINOAHng/Projet.Python.git

2. Accédez au répertoire du projet:

cd /FileManager/Python

## Excéxuter l'application

Une fois les dépenadnces installées, Vous pouvez exécuter le fichier Python pour démarrer le gestionnaire de fichiers:



    
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

## Fichier de Logs

Le fichier de logs (log.txt) permet de tracés toutes les actions effectuées par le programme. Voici un exemple de contenu d'un fichier de logs aprés plusieurs opérations: 


