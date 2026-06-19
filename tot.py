from prettytable import PrettyTable
from colorama import Fore, init
from dotenv import load_dotenv
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt #mampiasa dp 
import os

load_dotenv()
APP_NAME = os.getenv("APP_NAME")
ADMIN = os.getenv("DB_USER")    

todos = {}
next_id = 1

def afficher_menu():
    print(f"\n{Fore.CYAN} ====== {APP_NAME}======")
    print("1. Ajouter une tache")
    print("2. Voir les taches")
    print("3. Supprimer une tache")
    print("4. Quitter une tache")
    print("5. Verifie la tache")
    print("6. afficher le diagramme")

def ajouter_tache():
    #id:1, titre: "cours python", status: "Termine"
    global next_id

    titre = input("Entrer le tittre: ")

    todos[next_id] = {
        "titre": titre,
        "status": "non terminé"
    }

    print(Fore.GREEN + "tache ajouter avec succès")
    next_id +=1

def afficher_tache():
    if not todos:
        print(Fore.YELLOW + "aucune tache trouvée")
        return
    table = PrettyTable()
    table.field_names = ["ID", "Titre", "Status"]

    for id_tache, tache in todos.items():
        table.add_row([id_tache,tache["titre"], tache["status"]])

    print(table)

def supprimer_tache():
    try:
        id_tache = int(input("Entrer l'ID à supprimer: "))
        if id_tache not in todos:
            raise KeyError("Tache introuvable")
        del todos[id_tache]

        print(Fore.GREEN + "Tache supprimer.")
    
    except ValueError:
        print(Fore.RED + "Veuiller entrer l'ID à supprimer")
    except KeyError  as e:
        print(Fore.RED + str(e))
        
def verifie_tache():
    try:
        id_tache = int(input("Entrer l'ID à verifier: "))
        if id_tache not in todos:
            raise KeyError("Tache introuvable")
        
        todos[id_tache]["status"] = "terminer"

        print(Fore.GREEN + "Tache marquée comme terminée.")
    
    except ValueError:
        print(Fore.RED + "Veuiller entrer l'ID à verifier")
    except KeyError as e:
        print(Fore.RED + str(e))

def diagramme_tache():
    #verifie si aucun tache 
    if not todos :
        print("Aucun donné")
        return
    #variable pour stocker les taches non terminé et terminé
    terminer = 0
    non_terminer = 0
    
    #recuper les valeur de status dans le ictionnaire todo{}
    for tache in todos.values():
        
        if tache ["status"] == "terminer":
            terminer += 1
        else: 
            non_terminer += 1
    
    #label du diagramme 
    labels = [
        "terminer",
        "non terminer"
    ]
    
    #valeur afficher dans le diagramme 
    valeurs = [
        terminer,
        non_terminer
    ]
    
    plt.figure(figsize=(6, 4))
    
    #diagramme circulaire avec : valeur en % et labels 
    plt.pie(
        valeurs,
        labels=labels,
        autopct="%1.1f%%"
    )    
    
    #titre du diagramme 
    plt.title("reparation des taches ")
    #enregistrement le diagramme en image png
    plt.savefig("diagramme taches.png")
    #afficher le diagramme sur l'interface graphique GUI
    plt.show()
def main():
    print(Fore.GREEN + f"Bienvenue {ADMIN}")

    while True:
        afficher_menu()

        try:
            choix = int(input("Votre choix"))

            if choix == 1:
                ajouter_tache()
            elif choix == 2:
                afficher_tache()
            elif choix == 3:
                supprimer_tache()
            elif choix == 5:
                verifie_tache()
            elif choix == 6:
                diagramme_tache()
            elif choix == 4:
                print(Fore.CYAN + "Au revoir")
                break
            else:
                print(Fore.RED + "choix invalide")
        except ValueError:
            print(Fore.RED + "Entrer un nombre valide")


if __name__ == "__main__":
    main()
