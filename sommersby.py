from drinki import Drinks

class Sommersby(Drinks):
    _name = "Sommersby"
    def __init__(self):
        super().__init__(grupa = "piwo", nazwa = "Sommersby", cena = 20)