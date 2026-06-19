class Gestion_employe :
    def __init__(self, id, nom, poste, salaire):
        self._id = id
        self.nom = nom
        self.poste = poste
        self.__salaire = salaire
    
    def display_info(self):
        print(f"ID : {self._id}")
        print(f"Nom : {self.nom}")
        print(f"Poste : {self.poste}")
        print(f"Salaire : {self.__salaire:,} Ar".replace(","," ") )
    
    def to_dict(self):
        return True

class Employe_manager(Gestion_employe) :
    def __init__(self, id, nom, poste, salaire , employee):
        super().__init__(id, nom, poste, salaire)
        self.employe  = employee
    
    def add_employe(self) :
        print("Veuillez remplir la tache suivant")
    def remove_employe(nom) :
        print(" selectionner le nom de l'employe")
    def fin_employe(nom) :
        print("ajouter le nom que vous rechrchez")
    def display_all(self) :
        return self.display_info()       
    
Tout = [
    Gestion_employe(62 , "nisi" , "RESEAUX", 15000000 ),
    Employe_manager(45 , "bogosy" , "Dev", 19000000 , "Tsara")
]  
for Gestion_employe in Tout : 
    print(f"{Gestion_employe.display_info()}")
    
    def all():
        return Tout
            