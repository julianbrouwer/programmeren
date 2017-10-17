import xmltodict
with open('artikelen.xml','r') as file:
    inhoud=file.read()
    artikelen=xmltodict.parse(inhoud)
    for artikelen in file:
        print(artikelen['naam'])

print(artikelen)

