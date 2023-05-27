from random import randint
from aperol import Aperol
from black_russian import Black_russian
from chardonnay import Chardonnay
from cydr import Cydr
from greyhound import Greyhound
from lech import Lech
from merlot import Merlot
from pinot_noir import Pinot_noir
from porto import Porto
from pszeniczne import Pszeniczne
from sommersby import Sommersby
from tyskie import Tyskie
from white_russian import White_russian
from drinki import Drinks

class GenerujDrinka:
    #DRINKI:
    APEROL=0
    BLACK_RUSSIAN=1
    CHARDONNAY=2
    CYDR=3
    GREYHOUND=4
    LECH=5
    MERLOT=6
    PINOT_NOIR=7
    PORTO=8
    PSZENICZNE=9
    SOMMERSBY=10
    TYSKIE=11
    WHITE_RUSSIAN=12

    def generuj_losowego_drinka(self):
        drink_id = randint(self.APEROL, self.WHITE_RUSSIAN)
        if(drink_id == self.APEROL):
            drink = Aperol()
        elif(drink_id == self.BLACK_RUSSIAN):
            drink = Black_russian()
        elif (drink_id == self.CHARDONNAY):
            drink = Chardonnay()
        elif (drink_id == self.CYDR):
            drink = Cydr()
        elif (drink_id == self.GREYHOUND):
            drink = Greyhound()
        elif (drink_id == self.LECH):
            drink = Lech()
        elif (drink_id == self.MERLOT):
            drink = Merlot()
        elif (drink_id == self.PINOT_NOIR):
            drink = Pinot_noir()
        elif (drink_id == self.PORTO):
            drink = Porto()
        elif (drink_id == self.PSZENICZNE):
            drink = Pszeniczne()
        elif (drink_id == self.SOMMERSBY):
            drink = Sommersby()
        elif (drink_id == self.TYSKIE):
            drink = Tyskie()
        elif (drink_id == self.WHITE_RUSSIAN):
            drink = White_russian()
        else:
            print("Losowanie nie powiodlo sie")

        return drink

    def losuj_drinki(self, ilosc):
        lista_drinkow = []
        for i in range (0, ilosc):
            drink = self.generuj_losowego_drinka()
            lista_drinkow.append(drink)
        return lista_drinkow

    def wypisz_drinki(self, lista_drinkow, ilosc):
        for drinki in lista_drinkow:
            print(f"{drinki.get_nazwa()}, z listy napoi: {drinki.get_grupa()}, w cenie: {drinki.get_cena()} PLN")