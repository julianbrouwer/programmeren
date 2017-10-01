studentencijfers = [[95, 92, 86], [66, 75, 54], [89, 72, 100], [34, 0, 0]]

def gemiddelde_per_student(studentencijfers):
    kind = 0
    lst_gemiddelde = []
    for cijfers in studentencijfers:
        gemiddelde = int(sum(cijfers)/3)
        kind += 1
        antwoord = 'kind %d: gemiddelde %d' %(kind, gemiddelde)
        lst_gemiddelde.append(antwoord)
    anderelijst = []
    anderelijst.append(gemiddelde)
    return lst_gemiddelde


print(gemiddelde_per_student(studentencijfers))
