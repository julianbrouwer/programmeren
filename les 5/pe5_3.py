with open('kaartnummers.txt', 'r') as f:

    data = f.readlines()

    print('Er zijn %d regels in het bestand.' % len(data))
    print('Het maximale nummer is: %s.' % max(line.split(',')[0] for line in data))


