def optellen():
    keer = 0
    getal = 0
    while True:
        toevoegen = input('Geef een getal: ')
        keer += 1
        if toevoegen == '0':
            print('Er zijn ' + str(keer) + ' getallen ingevoerd, de som is: ' + str(getal))
            break

        getal += int(toevoegen)


optellen()