x = input()
for i in range(int(x)):
    y = input().split()
    numOne = int(y[0])
    numTwo = int(y[1])
    numThree = int(y[2])
    if numOne + numTwo == numThree:
        print("Possible")
    elif numOne - numTwo == numThree:
        print("Possible")
    elif numTwo - numOne == numThree:
        print("Possible")
    elif numOne * numTwo == numThree:
        print("Possible")
    elif numOne / numTwo == numThree:
        print("Possible")
    elif numTwo / numOne == numThree:
        print("Possible")
    else:
        print("Impossible")