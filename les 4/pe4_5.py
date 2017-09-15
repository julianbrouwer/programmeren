def kwadraten_som(grondgetallen):
    som = int()
    for getal in grondgetallen:
        if getal > 0:
            som = som + getal**2
    return som

print(kwadraten_som([4,5,3,-81]))







