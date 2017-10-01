while True:
    invoer = input('Geef een woord: ')
    if len(invoer)==4:
        print('inlezing van correcte string: '+ invoer +' is geslaagd')
        break
    else:
        print(invoer+ ' heeft ' + str(len(invoer))+' letters')