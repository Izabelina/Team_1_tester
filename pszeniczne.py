from drinki import Drinks

class Pszeniczne(Drinks):
    _name = "Pszeniczne"
    def __init__(self):
        super().__init__(grupa = "piwo", nazwa = "pszeniczne", cena = 25)