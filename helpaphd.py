x = input();
for i in range(int(x)):
    myInput = input();
    if myInput == "P=NP":
        print("skipped")
    else:
        myAddition = myInput.split('+')
        numOne = int(myAddition[0])
        numTwo = int(myAddition[1])
        print(numOne + numTwo)