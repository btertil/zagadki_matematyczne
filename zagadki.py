# -*- coding: utf-8 -*-

import random
import numpy as np
import matplotlib.pyplot as plt


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
    
    print("\n\n\nTwoje wyniki\n\n")
    
    
    # Przygotowanie danych do wykresów

    # Wykres 1: rozkłady działań (barplot, stacked dla poprawnych i błędnych odpowiedzi)

    # Ze słownika do zmiennych (dodawanie dobrze / źle, odejmowanie dobrze źle itd)
    d_d = np.array(dzialania[1]).sum()
    d_z = np.array(dzialania[1]).size - d_d
    o_d = np.array(dzialania[2]).sum()
    o_z = np.array(dzialania[2]).size - o_d
    m_d = np.array(dzialania[3]).sum()
    m_z = np.array(dzialania[3]).size - m_d
    z_d = np.array(dzialania[4]).sum()
    z_z = np.array(dzialania[4]).size - z_d

    # Listy potrzebne do wykresów (stacked barplots)
    goods = []
    bads = []

    # Seria poprawnych odpowiedzi, dla 4 działań
    goods.append(d_d)
    goods.append(o_d)
    goods.append(m_d)
    goods.append(z_d)

    # Seria błędnych odpowiedzi, dla 4 działań
    bads.append(d_z)
    bads.append(o_z)
    bads.append(m_z)
    bads.append(z_z)

    # Wykres 2: Odsetek błędów
    ds = np.array(dzialania[1]).mean()
    os = np.array(dzialania[2]).mean()
    ms = np.array(dzialania[3]).mean()
    zs = np.array(dzialania[4]).mean()

    srednie = np.array([ds, os, ms, zs])



    # Rysowanie wykresów

    fig, ax = plt.subplots(1, 2, figsize=(17, 6))


    # potrzebne aby sformatować słupki i ich opisy (kolejność i labelki!)
    bars = np.arange(len(dzialania_opis))

    # plt.xticks(range(len(dzialania_opis)), dzialania_opis) <- tak może być bez subplots, ale tu nie da rady!
    # i trzeba 2 poleceniami:
    # ax[0].set_xticks(bars)
    # ax[0].set_xticklabels(dzialania_opis, fontsize=13)

    plt.suptitle("Twoje prawidłowe odpowiedzi to: %d / %d (%.2f%%), największa poznana liczba: %d"
                 % (dobre, dobre+zle, 100*dobre/(dobre+zle), rekord), fontsize=16)

    ax[0].bar(bars, goods, label="poprawne")
    ax[0].bar(bars, bads, bottom=goods, color='red', label="błędne")
    ax[0].set_ylabel('Liczba Działań', fontsize=14)
    ax[0].set_xticks(bars)
    ax[0].set_xticklabels(dzialania_opis, fontsize=12)
    ax[0].legend(fontsize=12)
    ax[0].grid()

    ax[1].bar(bars, srednie)
    ax[1].bar(bars, 1-srednie, bottom=srednie, color='red')
    ax[1].set_ylabel('Poprawne vs błędne odpowiedzi', fontsize=14)
    ax[1].set_ylim([0, 1])
    ax[1].set
    ax[1].set_xticks(bars)
    ax[1].set_xticklabels(dzialania_opis, fontsize=12)
    ax[1].grid()

    plt.show()
