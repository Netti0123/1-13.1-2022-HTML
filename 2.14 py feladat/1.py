szoveg = "Lustaság fél egézség"
szovegFeloszt = []

for i in range(0, len(szoveg)):
   szovegFeloszt.append(1)
   szovegFeloszt[i] = szoveg[i:i+1]

for i in range(0, len(szovegFeloszt)):
   print(szovegFeloszt[i])
