from drinki import Drinks

class Black_russian(Drinks):
    _name = "Black Russian"
    def __init__(self):
        super().__init__(grupa = "drinki", nazwa = "Black Russian", cena = 25)