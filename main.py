from FileManager import FileManager

def main():
    # Spécifier le chemin du fichier log.txt
    file_path = 'log.txt'
    
    # Créer une instance de FileManager
    file_manager = FileManager(file_path)
    
    # Menu simple pour interagir avec le fichier
    while True:
        print("\n=== Menu ===")
        print("1. Lire le fichier")
        print("2. Écrire dans le fichier")
        print("3. Compter les lignes du fichier")
        print("4. Rechercher un mot-clé")
        print("5. Quitter")
        
        choix = input("Choisissez une option (1-5) : ")
        
        if choix == '1':
            # Lire et afficher le contenu du fichier
            file_manager.read_file()
        elif choix == '2':
            # Écrire des données dans le fichier
            data = input("Entrez les données à ajouter au fichier : ")
            file_manager.write_to_file(data)
        elif choix == '3':
            # Compter et afficher le nombre de lignes
            nombre_lignes = file_manager.count_lines()
            if nombre_lignes is not None:
                print(f"Nombre de lignes dans le fichier : {nombre_lignes}")
        elif choix == '4':
            # Rechercher un mot-clé dans le fichier
            keyword = input("Entrez le mot-clé à rechercher : ")
            file_manager.search_keyword(keyword)
        elif choix == '5':
            # Quitter l'application
            print("Fermeture de l'application.")
            break
        else:
            print("Option invalide, veuillez réessayer.")

# Point d'entrée du programme principal
if __name__ == "__main__":
    main()
