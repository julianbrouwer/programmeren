infile = open('hardlopers.txt', 'a')
import datetime
vandaag = datetime.datetime.today()
s = vandaag.strftime("%a %d %b %y, %X,")
outfile = open('hardlopers.txt', 'a')
next = '\n'

while True:
    invoer = input('Vul hier je naam in: ')
    if invoer == 'quit':
        outfile.close()
        break
    outfile.write(s + invoer + next)
