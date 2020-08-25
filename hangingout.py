x = input()
mylist = [int(x) for x in x.split()]
cap = mylist[0]
events = mylist[1]
total = 0
turnedAway = 0
for i in range(events):
    curr = input()
    currentList = curr.split()
    if currentList[0] == "leave":
        total = total - int(currentList[1])
    elif currentList[0] == "enter" and cap >= (total + int(currentList[1])):
        total = total + int(currentList[1])
    else:
        turnedAway = turnedAway + 1
print(turnedAway)