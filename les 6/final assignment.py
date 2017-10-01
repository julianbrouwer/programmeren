lijst_kluizen = [1,2,3,4,5,6,7,8,9,10,11,12]
waarde = 0

def menu_opties(waarde):
    print('Hoofdmenu:')
    print('1. Ik wil een nieuwe kluis')
    print('2. Ik wil mijn kluis openen')
    print('3. Ik wil weten hoeveel kluizen nog vrij zijn')
    print('4. Ik wil graag het programma afsluiten')

menu_opties(waarde)

def keuze_maken(waarde):
    keuze = int(input('Kies een optie: '))

    if keuze == 1:
        input_kluisnummer = input('Nieuw kluisnummer: ')
        nieuwe_kluis(input_kluisnummer)

    elif keuze == 2:
        kluis_openen(0)

    elif keuze == 3:
        aantal_kluizen_vrij(0)

    elif keuze == 4:
        exit()

    else:
        print('Sorry. Onjuiste keuze gevonden.')

with open('kluizen.txt', 'r+') as open_kluizen:
        aantalkluizen = 0
        for kluis in open_kluizen:
            aantalkluizen += 1

def aantal_kluizen_vrij(waarde):
    print('Aantal vrije kluizen zijn: ', aantalkluizen )

def nieuwe_kluis(waarde):

    with open('kluizen.txt', 'r+') as nieuwekluis:

        found = False
        kluisnummer = input('Welke kluis wil je aanmaken: ')
        pincode = input('Welke pincode wil je instellen: ')

        for lines in nieuwekluis:
            if pincode in lines:

                nieuwe_tekst = str(lines)
                nieuwe_lijst = list(nieuwe_tekst.split(','))
                nummer = nieuwe_tekst[0].strip()
                password = nieuwe_tekst[1].strip()

                if kluisnummer == nummer:
                    nieuwe_lijst.append()
                    found = True

        if not found:
            print('Kluisnummer', kluisnummer, 'is niet gevonden')

def kluis_openen(waarde):

    with open('kluizen.txt', 'r') as kluizen:

        found = False
        kluisnummer = input('Welk kluisnummer wil je openen: ')
        pincode = input('Wat is je pincode: ')

        for lines in kluizen:
            if pincode in lines:

                nieuwe_tekst = str(lines)
                nieuwe_lijst = list(nieuwe_tekst.split(','))
                nummer = nieuwe_tekst[0].strip()
                password = nieuwe_tekst[1].strip()

                if kluisnummer == nummer:
                    print('Je kluisnummer is gevonden')
                    print('Kluis', nummer, 'is geopend')
                    found = True

        if not found:
            print('Kluisnummer', kluisnummer, 'is niet gevonden')

keuze_maken(waarde)

