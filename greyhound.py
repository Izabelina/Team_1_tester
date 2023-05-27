from drinki import Drinks

class Greyhound(Drinks):
    _name = "Greyhound"
    def __init__(self):
        super().__init__(grupa = "drinki", nazwa = "Greyhound", cena = 21)