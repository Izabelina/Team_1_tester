from drinki import Drinks

class Merlot(Drinks):
    _name = "Merlot"
    def __init__(self):
        super().__init__(grupa = "wino", nazwa = "Merlot", cena = 35)