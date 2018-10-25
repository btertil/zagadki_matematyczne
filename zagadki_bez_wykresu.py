# -*- coding: utf-8 -*-

import random


# dictionary dla działań
dzialania = dict()
dzialania[1] = []
dzialania[2] = []
dzialania[3] = []
dzialania[4] = []
dzialania_opis = ['dodawanie', 'odejmowanie', 'mnożenie', 'dzielenie']


# większa przez mniejszą, lub 0 przez dowolną.
# nie powinno być sytuacji że obie są 0 (wcześniejszy warunek) ale na wszelki wypadek obsługa: warning i (1,1)
def do_dzielenia(l1, l2):
    if (l1 >= l2 and l2 > 0) or l1 == 0:
        return(l1, l2)
    elif (l2 >= l1 and l1 > 0) or l2 == 0:
        return(l2, l1)
    else:
        print("Warning! both numbers are zeros!")
        print("l1 = %d, l2 = %d" % (l1, l2))
        return(1, 1)

    
maxl = 3
liczby = [i for i in range(maxl+1)]

print("Witaj!")
print("Wylosuję dla Ciebie jakąś zagadkę matematyczną, zobaczymy czy potrafisz prawidłowo odpowiedzieć, hi, hi, hi!")
print("Na razie znam tylo liczby: %s, ale jak będziesz dobrze odpowiadać poznam ich więcej!" % liczby)
print("W każdej chwili możesz zakończyć wpisując \"koniec\", to zaczynajmy :)\n")

dobre = 0
zle = 0
rekord = maxl

run = True
while (run):
    
    # Losowania liczby 1 i liczby 2
    l1 = random.randint(0, maxl)
    l2 = random.randint(0, maxl)
    
    # Losujemy działania matematyczne: 1+, 2-, 3*, 4/
    # Aby dzielenia nie było za mało to mały boost! ;)
    if (l1 + l2 > 0) and ((l2 != 0 and l1 % l2 == 0) or (l1 != 0 and l2 % l1 == 0)):
        # Jeśli dzielenie to większej liczby przez mniejszą dla Ninki
        if l1 != 0:
            l1, l2 = do_dzielenia(l1, l2)
        dzialanie = 4
        correct = l1 / l2
        znak = '/'
    else:
        dzialanie = random.randint(1, 3)
        if dzialanie == 1:
            correct = l1 + l2
            znak = '+'
        elif dzialanie == 2:
            correct = l1 - l2
            znak = '-'
        elif dzialanie == 3:
            correct = l1 * l2
            znak = '*'

    try:
        odp = input("Ile to jest %d %s %d?: " % (l1, znak, l2))
        if odp.lower() == "koniec":
            print("Ok, do zobaczenia następnym razem!")
            run = False
            pass

        elif int(odp) == correct:
            print("Brawo! tak to jest ta liczba, dzięki Tobie poznałem liczbę %s\n" % str(maxl+1))
            dzialania[dzialanie].append(1)
            maxl += 1
            dobre += 1
            if maxl > rekord: rekord = maxl
        else:
            dzialania[dzialanie].append(0)
            zle += 1
            if maxl > 3:
                print("Ojej, nie udało się! Prawidłowy wynik to %s, zapominam liczbę %s :(\n" % (str(correct), str(maxl)))
                maxl -= 1
            else:
                print("Ojej, nie udało się! Prawidłowy wynik to %s :(\n" % (str(correct)))
    except:
        print("Można wpisać tylko liczby całkowite lub słowo \"koniec\"")

if dobre + zle >= 1:
    print("Prawidłowe odpowiedzi: %d / %d (%.2f%%)" % (dobre, dobre+zle, 100*dobre/(dobre+zle)))
    print("Nasz najlepszy wynik to liczba %d" % rekord)
