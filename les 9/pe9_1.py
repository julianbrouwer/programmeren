def personen():
    try:
        hotelkosten = 4356
        invoer = int(input('Hoeveel personen gaan mee op reis? '))
        if invoer > -1:
            y = hotelkosten / invoer
            print('Iedereen betaald {} euro.'.format(y))
        else:
            print('Geen negatieve getallen!')

    except ZeroDivisionError:
        print('Delen door nul kan niet!')
    except ValueError:
        print('Gebruik cijfers voor het invoeren van getallen!')
    except:
        print('Onjuiste invoer.')



personen()