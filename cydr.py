from drinki import Drinks

class Cydr(Drinks):
    _name = "Cydr"
    def __init__(self):
        super().__init__(grupa = "piwo", nazwa = "Cydr", cena = 15)