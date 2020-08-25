x = input()
for i in range(int(x)):
    myInput = input()
    command = myInput[11:]
    if "Simon says" in myInput:
        print(command)
