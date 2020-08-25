x = input()
mylist = [int(x) for x in x.split()]
left = mylist[0]
right = mylist[1]
if left == 0 and right == 0:
    print("Not a moose")
elif left != right:
    if left > right:
        total = left + left
    else:
        total = right + right
    print("Odd", total)
else:
    total = left + right
    print("Even", total)
