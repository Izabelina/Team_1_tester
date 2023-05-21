plec = input("Wybierz płeć (m/k):  ")
# Sprawdzenie wyboru płci
if plec == "m":
    print("Wybrałeś mężczyznę.")
    while True:
        region = input("Wybierz swoj region: EUR/USA  ")
        if region == "EUR":
            print("W Europie picie alkoholu dozwolone jest od 18 r.z.")
            wiek = input("Podaj wiek użytkownika jako liczbe calkowitą:  ")
            if wiek.isdigit() == False:
                exit("Wiek musi być liczbą albo podana liczba nie jest calkowita")
            wiek = int(wiek)
            if wiek >= 18 and wiek < 40:
                print("Witaj w naszej apce z alkoholem, zapraszamy do zakupów")
                break
            elif wiek >= 40 and wiek <= 119:
                print("Witaj w naszej apce z alkoholem, zapraszamy do zakupów")
                print("Uważaj w Twoim wieku nie przasadzaj ze spożyciem")
                break
            elif wiek >= 120:
                exit("Wpisano zbyt wysoki wiek. Zamykam aplikacje")
            else:
                exit("Jesteś za młoda/y na alkohol. Zapraszamy na disney.com")
        elif region == "USA":
            print("W USA picie alkoholu dozwolone jest od 21 r.z.")
            wiek = input("Podaj wiek użytkownika jako liczbe calkowitą:  ")
            if wiek.isdigit() == False:
                exit("Wiek musi być liczbą albo podana liczba nie jest calkowita")
            wiek = int(wiek)
            if wiek >= 21 and wiek < 40:
                print("Witaj w naszej apce z alkoholem, zapraszamy do zakupów")
                break
            elif wiek >= 40 and wiek <= 119:
                print("Witaj w naszej apce z alkoholem, zapraszamy do zakupów")
                print("Uważaj w Twoim wieku nie przasadzaj ze spożyciem")
                break
            elif wiek >= 120:
                exit("Wpisano zbyt wysoki wiek. Zamykam aplikacje")
            else:
                exit("Jesteś za młoda/y na alkohol. Zapraszamy na disney.com")
        else:
            print("Wybrales nieprawidlowy region. Sprobuj jeszcze raz.  ")

elif plec == "k":
    print("Wybrałaś kobietę.")
    while True:
        region = input("Wybierz swoj region: EUR/USA  ")
        if region == "EUR":
           print("W Europie picie alkoholu dozwolone jest od 18 r.z.")
           wiek = input("Podaj wiek użytkownika jako liczbe calkowitą:  ")
           if wiek.isdigit() == False:
               exit("Wiek musi być liczbą albo podana liczba nie jest calkowita")
           wiek = int(wiek)
           if wiek >= 30 and wiek <120:
               print("Zapraszamy na darmowy Aperol")
               break
           elif wiek >= 18 and wiek < 40:
               print("Witaj w naszej apce z alkoholem, zapraszamy do zakupów")
               break
           elif wiek >= 40 and wiek <= 119:
               print("Witaj w naszej apce z alkoholem, zapraszamy do zakupów")
               print("Uważaj w Twoim wieku nie przasadzaj ze spożyciem")
               break
           elif wiek >= 120:
               exit("Wpisano zbyt wysoki wiek. Zamykam aplikacje")
           else:
               exit("Jesteś za młoda/y na alkohol. Zapraszamy na disney.com")
        elif region == "USA":
           print("W USA picie alkoholu dozwolone jest od 21 r.z.")
           wiek = input("Podaj wiek użytkownika jako liczbe calkowitą:  ")
           if wiek.isdigit() == False:
               exit("Wiek musi być liczbą albo podana liczba nie jest calkowita")
           wiek = int(wiek)
           if wiek >= 30 and wiek <120:
               print("Zapraszamy na darmowy Aperol")
               break
           elif wiek >= 21 and wiek < 40:
               print("Witaj w naszej apce z alkoholem, zapraszamy do zakupów")
               break
           elif wiek >= 40 and wiek <= 119:
               print("Witaj w naszej apce z alkoholem, zapraszamy do zakupów")
               print("Uważaj w Twoim wieku nie przasadzaj ze spożyciem")
               break
           elif wiek >= 120:
               exit("Wpisano zbyt wysoki wiek. Zamykam aplikacje")
           else:
               exit("Jesteś za młoda/y na alkohol. Zapraszamy na disney.com")
        else:
            print("Wybrales nieprawidlowy region. Sprobuj jeszcze raz.")
else:
    exit("Niepoprawny wybór płci.")