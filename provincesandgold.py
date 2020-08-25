x = input()
mylist = x.split()
G = int(mylist[0])*3
S = int(mylist[1])*2
C = int(mylist[2])*1
toSpend = G + S + C
if toSpend >= 8:
    victoryCard = "Province"
    treasureCard = "Gold"
elif toSpend >= 6:
    victoryCard = "Duchy"
    treasureCard = "Gold"
elif toSpend >= 5:
    victoryCard = "Duchy"
    treasureCard = "Silver"
elif toSpend >= 3:
    victoryCard = "Estate"
    treasureCard = "Silver"
elif toSpend >= 2:
    victoryCard = "Estate"
    treasureCard = "Copper"
else:
    treasureCard = "Copper"
if toSpend >= 2:
    print(victoryCard, "or", treasureCard)
else:
    print(treasureCard)