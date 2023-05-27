from drinki import Drinks

class Chardonnay(Drinks):
    _name = "Chardonnay"
    def __init__(self):
        super().__init__(grupa = "wino", nazwa = "Chardonnay", cena = 40)