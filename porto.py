from drinki import Drinks

class Porto(Drinks):
    _name = "Porto"
    def __init__(self):
        super().__init__(grupa = "wino", nazwa = "Porto", cena = 27)