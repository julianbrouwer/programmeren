def convert(cel):
    far = cel *1.8+32
    return far

def table():
    for i in range(-30, 40, 10):
        print('{0:8},{1:8}'.format(convert(i),i))
print('{0:8},{1:8}'.format('     C', '      F'))

table()















































