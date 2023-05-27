from drinki import Drinks

class Tyskie(Drinks):
    _name = "Tyskie"
    def __init__(self):
        super().__init__(grupa = "piwo", nazwa = "Tyskie", cena = 17)