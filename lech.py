from drinki import Drinks

class Lech(Drinks):
    _name = "Lech"
    def __init__(self):
        super().__init__(grupa = "piwo", nazwa = "Lech", cena = 18)