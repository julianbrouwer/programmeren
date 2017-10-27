import xmltodict

file = open('stations.xml', 'r')
dict = xmltodict.parse(file.read())
file.close()

print('Dit zijn de codes en types van de 4 stations:')
for station in dict['Stations']['Station']:
    print('{} - {}'.format(station['Code'], station['Type']))

print('\nAlle stations met synoniemen:')
for station in dict['Stations']['Station']:
    if station['Synoniemen'] != None:
        print('{}\n'.format(station['Synoniemen']))

print('De lange naam van elk station:')
for station in dict['Stations']['Station']:
   print(station['Namen']['Lang'])
