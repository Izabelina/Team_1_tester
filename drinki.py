class Drinks:
    _name = "Drinki"
    def __init__(self, grupa, nazwa, cena):
        self.nazwa = nazwa
        self.cena = int(cena)
        self.grupa = grupa

    def get_grupa(self):
        return self.grupa

    def get_nazwa(self):
        return self.nazwa

    def get_cena(self):
        return self.cena
