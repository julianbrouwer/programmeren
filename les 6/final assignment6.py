import random

opties = int(input('1: Ik wil weten hoeveel kluizen nog vrij zijn \n2: Ik wil een nieuwe kluis \n3: Ik wil even iets uit mijn kluis halen \n\nVoer hier uw optie in: '))

def toon_aantal_kluizen_vrij():
    infile = open('kluizen.txt', 'r')
    regels = infile.readlines()
    bezet = len(regels)
    vrij = 12 - bezet
    if vrij >0:
        print("Er zijn", vrij, "kluisjes beschikbaar")
    else:
        print("Er zijn geen kluizen beschikbaar")

def nieuwe_kluis():
    with open('kluizen.txt') as kluizen:
        regels = kluizen.read()
        inhoud = regels.splitlines()
        kluisnummers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    for nummer in inhoud:
        if nummer != '':
            kluizen = open('kluizen.txt', 'a')
            kluis = nummer.split(";")
            nummer = int(kluis[0])
            kluisnummers.remove(nummer)
    if len(kluisnummers) != 0:
        wachtwoord = input("Vul een wachtwoord in voor je kluis: ")
        welkekluis = random.choice(kluisnummers)
        kluizen.write(str(welkekluis) + ';' + wachtwoord + '\n')
        print('Kluis' , welkekluis,'is van u')

def kluis_openen():
    kluisnummer = input("Voer uw kluisnummer in: ")
    wachtwoord = input("Voer uw kluiscode in: ")
    combinatie = kluisnummer + ';' + wachtwoord
    with open("kluizen.txt") as kluizen:
        regels = kluizen.read()
        inhoud = regels.splitlines()
        if combinatie in inhoud:
            print("De kluis is open")
        else:
            print("De combinatie is niet correct, probeer opnieuw")


if opties == 1:
    toon_aantal_kluizen_vrij()

if opties == 2:
    nieuwe_kluis()

if opties == 3:
    kluis_openen()

