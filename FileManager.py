class FileManager:
    def __init__(self, file_path):
        self.file_path = file_path
    
    def read_file(self):
        try:
            with open(self.file_path, 'r') as file:
                content = file.read()
                print("\n--- Contenu du fichier ---")
                print(content)
                print("--------------------------\n")
        except FileNotFoundError:
            print(f"Erreur : le fichier '{self.file_path}' n'a pas été trouvé.")
    
    def write_to_file(self, data):
        try:
            # Ouverture en mode 'a' pour ajouter à la fin sans effacer le contenu existant
            with open(self.file_path, 'a') as file:
                file.write(data + '\n')  # Ajouter une nouvelle ligne à la fin
            print("Données ajoutées avec succès.")
        except FileNotFoundError:
            print(f"Erreur : le fichier '{self.file_path}' n'a pas été trouvé.")
    
    def count_lines(self):
        try:
            with open(self.file_path, 'r') as file:
                lines = file.readlines()
                return len(lines)
        except FileNotFoundError:
            print(f"Erreur : le fichier '{self.file_path}' n'a pas été trouvé.")
            return None
    
    def search_keyword(self, keyword):
        try:
            with open(self.file_path, 'r') as file:
                lines = file.readlines()
                found = False
                print(f"\n--- Lignes contenant '{keyword}' ---")
                for line in lines:
                    if keyword in line:
                        print(line.strip())
                        found = True
                if not found:
                    print(f"Aucune occurrence de '{keyword}' trouvée.")
                print("-------------------------------\n")
        except FileNotFoundError:
            print(f"Erreur : le fichier '{self.file_path}' n'a pas été trouvé.")
