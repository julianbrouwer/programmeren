def namen():

    counters = {}
    while True:
        invoer = input('Volgende naam: ')
        if invoer == '':
            for value in counters:
                if counters[value] == 1:
                    print('Er is {} student met de naam {}'.format(counters[value], value))
                else:
                    print('Er zijn {} studenten met de naam {}'.format(counters[value], value))
            break

        if invoer in counters:
            counters[invoer] += 1
        else:
            counters[invoer] = 1



namen()