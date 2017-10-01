infile = open('kaartnummers.txt', 'r')
test1 = infile.readlines()

for item in test1:
    item2=item.strip()
    item3=item2.split(', ')
    print('{} heeft kaartnumer: {}'.format(item3[1],item3[0]))






