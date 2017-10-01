def ticker():
    dict = {}
    file = open('ticker.txt')
    content = file.readlines()
    file.close()
    for i in content:
        i = i.strip().split(':')

        bedrijfsnaam = i[1]
        symbol = i[0]
        dict[symbol] = bedrijfsnaam



    while True:
        invoer = input('Enter Company name: ')
        if invoer in dict:
            regel = 'Ticker symbol: '
            print(regel + dict[invoer])


ticker()