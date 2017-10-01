invoer = eval(input('geef lijst met minimaal 10 strings: '))
list = []
for x in invoer:
    if len(x)>0 and len(x)<=4:
        print(x)
        list += [x]
print(list)