ruweInvoer="5-9-7-1-7-8-3-2-4-8-7-9-10"
invoer = ruweInvoer.split('-')
# invoer = [7, 2, 3, 4, 5, 1, 7, 7, 8, 8, 9, 9]
for i in range(len(invoer)):
    invoer[i]=eval(invoer[i])
invoer.sort()
print(invoer)
print(max(invoer))
print(min(invoer))
uitkomst = 0
for x in invoer:
    uitkomst += 1
print(uitkomst)
hoi = 0
for y in invoer:
    hoi += 1
print(hoi)
gemiddelde = hoi/uitkomst
print(gemiddelde)

