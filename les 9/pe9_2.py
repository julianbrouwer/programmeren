import datetime
import csv
bestand = 'inloggers.csv'
vandaag = datetime.datetime.today()
s = vandaag.strftime("%a %d %b %Y, at %X")

with open('bestand', 'a', newline='') as myCSVFile:
    writer = csv.writer(myCSVFile, delimiter=';')
    writer.writerow(('datum','naam', 'voorletters', 'geboortedatum', 'email'))

    while True:
            naam = input("Wat is je achternaam? ")
            if naam == 'einde':
                break
            voorl = input("Wat zijn je voorletters? ")
            gbdatum = input("Wat is je geboortedatum? ")
            email = input("Wat is je e-mail adres? ")

            writer.writerow((s,naam,voorl,gbdatum,email))