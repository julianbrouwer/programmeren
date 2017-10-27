def standaardprijs(afstandKM):
    if afstandKM > 50:
        return afstandKM*0.60 + 15

    else:
        if afstandKM <=0:
            return 0
        return afstandKM*0.80


def ritprijs(leeftijd, weekendrit, afstandKM):
    standaardprijs(afstandKM)
    if leeftijd < 12 or leeftijd >= 65:
        if weekendrit == False:
            return standaardprijs(afstandKM) * 0.70
        else:
            return standaardprijs(afstandKM) * 0.65
    else:
        if weekendrit == False:
            return standaardprijs(afstandKM)
        else:
            return standaardprijs(afstandKM)*0.60
print(ritprijs(11,False,10))


