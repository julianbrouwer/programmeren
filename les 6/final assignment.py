def nieuwe_kluis():
    with open('kluizen.txt', 'r') as f:
        lines = f.readlines()
    for x in lines:
        pn_record = x.split(';')
        kluisnummer.remove(int(pn_record[0]))
    if len(kluisnummer) != 0:
        with open('kluizen.txt', 'a') as f:
            ww = input("voer een wachtwoord in")
            welkekluis = random.choice(kluisnummer)
            f.write(str(welkekluis) + ";" + ww + "\n")
            print("uw kluis is kluisnummer " + str(welkekluis))
            f.close()
    if len(kluisnummer) <= 0:
        print("er zijn geen kluizen beschikbaar")