from drinki import Drinks

class White_russian(Drinks):
    _name = "White Russian"
    def __init__(self):
        super().__init__(grupa = "drinki", nazwa = "White Russian", cena = 27)