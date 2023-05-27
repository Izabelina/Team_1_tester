#funkcja sprawdzajaca plec
def plec():
    plec = input("Wybierz plec: M/K   ").upper()
    if (plec == "K"):
        return "K"
    elif (plec == "M"):
        return "M"
    else:
        exit ("Niepoprawny wybor plci - zamykam program")

#funkcja sprawdzajaca wiek
def wiek():
    wiek = input("Podaj wiek użytkownika jako liczbe calkowitą:  ")
    if wiek.isdigit() == False:
        exit("Wiek musi być liczbą albo podana liczba nie jest calkowita")
    wiek = int(wiek)
    return wiek

#funkcja sprawdzajaca region
def region():
    region = input ("Program obsluguje tylko Europe i USA, wybierz swoj region: EUR/USA   ")
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
    age = wiek()
    if age >= 18 and age < 40:
        print("Witaj w naszej apce z alkoholem, zapraszamy do zakupów")

    elif age >= 40 and age <= 119:
        print("Witaj w naszej apce z alkoholem, zapraszamy do zakupów")
        print("Uważaj w Twoim wieku nie przasadzaj ze spożyciem")

    elif age >= 120:
        exit("Wpisano zbyt wysoki wiek. Zamykam aplikacje")
    else:
        exit("Jesteś za młoda/y na alkohol. Zapraszamy na disney.com")

#funkcja obslugujaca USA
def usa():
    age = wiek()
    if age >= 21 and age < 40:
        print("Witaj w naszej apce z alkoholem, zapraszamy do zakupów")

    elif age >= 40 and age <= 119:
        print("Witaj w naszej apce z alkoholem, zapraszamy do zakupów")
        print("Uważaj w Twoim wieku nie przasadzaj ze spożyciem")

    elif age >= 120:
        exit("Wpisano zbyt wysoki wiek. Zamykam aplikacje")
    else:
        exit("Jesteś za młoda/y na alkohol. Zapraszamy na disney.com")



#funkcja oferujaca darmowy aperol dla pan

###TODO: ogarnac, zeby dwa razy sie nie pytalo o wiek
def aperol_kobiety():
    if plec() == "K" and wiek() >= 30:
        print("Zapraszamy na darmowy Aperol")

####START PROGRAMU####
print("Witamy w naszym sklepie z alkoholem")
region()
aperol_kobiety()
