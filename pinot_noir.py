from drinki import Drinks

class Pinot_noir(Drinks):
    _name = "Pinot Noir"
    def __init__(self):
        super().__init__(grupa = "wino", nazwa = "Pinot Noir", cena = 30)