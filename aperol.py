from drinki import Drinks

class Aperol(Drinks):
    _name = "Aperol"
    def __init__(self):
        super().__init__(grupa = "drinki", nazwa = "Aperol", cena = 25)

