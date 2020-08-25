x = input()
mylist = x.split()
A = mylist[0]
B = mylist[1]
revA = A[::-1]
revB = B[::-1]
if int(revA) > int(revB):
    print(revA)
else:
    print(revB)