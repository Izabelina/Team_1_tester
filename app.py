from generuj_drinka import GenerujDrinka

#funkcja sprawdzajaca plec
def plec():
    plec = input("Wybierz plec: M/K   ").upper()
    if (plec == "K"):
        return "K"
    elif (plec == "M"):
        return "M"
    else:
        exit ("Niepoprawny wybor plci - zamykam program")

#funkcja sprawdzajaca region
def region():
    region = input ("Program obsluguje tylko Europe i USA, wybierz swoj region: EUR/USA   ").upper()
    if (region == "EUR"):
        print ("W Europie picie alkoholu dozwolone jest od 18 r.z.")
        eur()
    elif (region == "USA"):
        print("W USA picie alkoholu dozwolone jest od 21 r.z.")
        usa()
    else:
        exit ("Nie wpisales wlasciwego regionu. Zamykam program")

#funkcja obslugujaca Europe
def eur():
    wiek = input("Podaj wiek użytkownika jako liczbe calkowitą:  ")
    if wiek.isdigit() == False:
        exit("Wiek musi być liczbą albo podana liczba nie jest calkowita")
    wiek = int(wiek)
    if wiek >= 18 and wiek < 30:
        aperol_kobiety3()
    elif wiek >= 30 and wiek <= 39:
        aperol_kobiety()
    elif wiek >= 40 and wiek <= 119:
        aperol_kobiety2()
    elif wiek >= 120:
        exit("Wpisano zbyt wysoki wiek. Zamykam aplikacje")
    else:
        exit("Jesteś za młoda/y na alkohol. Zapraszamy na disney.com")

#funkcja obslugujaca USA
def usa():
    wiek = input("Podaj wiek użytkownika jako liczbe calkowitą:  ")
    if wiek.isdigit() == False:
        exit("Wiek musi być liczbą albo podana liczba nie jest calkowita")
    wiek = int(wiek)
    if wiek >= 21 and wiek < 30:
        aperol_kobiety3()
    elif wiek >= 30 and wiek <= 39:
        aperol_kobiety()
    elif wiek >= 40 and wiek <= 119:
        aperol_kobiety2()
    elif wiek >= 120:
        exit("Wpisano zbyt wysoki wiek. Zamykam aplikacje")
    else:
        exit("Jesteś za młoda/y na alkohol. Zapraszamy na disney.com")

#funkcja oferujaca darmowy aperol dla pan
def aperol_kobiety():
    if plec() == "K":
        print("Witaj w naszej apce z alkoholem, zapraszamy na darmowy Aperol.")
    else:
        print("Witaj w naszej apce z alkoholem, zapraszamy do zakupów.")

def aperol_kobiety2():
    if plec() == "K":
        print("Witaj w naszej apce z alkoholem - zapraszamy na darmowy Aperol, ale w Twoim wieku nie przesadzaj ze spozyciem")
    else:
        print("Witaj w naszej apce z alkoholem, zapraszamy do zakupów")
        print("Uważaj w Twoim wieku nie przasadzaj ze spożyciem")

def aperol_kobiety3():
    if plec() == "K":
        print("Witaj w naszej apce z alkoholem, zapraszamy do zakupów")
    else:
        print("Witaj w naszej apce z alkoholem, zapraszamy do zakupów")

#funkcja losujaca losowy drink
generuj_drinka = GenerujDrinka()
def losuj_drinka():
    #Moze sie zdarzyc, ze wylosuje takie same drinki :P
    wybor = input("Czy chcesz wygenerowac losowe drinki? T/N   ").upper()
    if wybor == "T":
        ilosc = input("Ile losowych drinkow Ci wyswietlic? (max 5)   ")
        if ilosc.isdigit() == False:
            exit("Nie podales prawidlowej wartosci. Zamykam program")
        ilosc = int(ilosc)
        if ilosc >= 0 and ilosc <= 5:
            print("Oto sugerowana lista drinkow:")
            lista_drinkow = generuj_drinka.losuj_drinki(ilosc)
            generuj_drinka.wypisz_drinki(lista_drinkow, ilosc)
        else:
            print("Mozna wylosowac max 10 drinkow!")


    #TODO: Warto w sumie zrobic tez cos dalej w naszej apce :)
    elif wybor == "N":
        print("W takim razie zapraszamy dalej")
    else:
        exit("Nie wybrales T lub N - zamykam program")



####START PROGRAMU####
print("Witamy w naszym sklepie z alkoholem")
region()
losuj_drinka()