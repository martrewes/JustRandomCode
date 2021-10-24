def nextChar(string):
    int = 0
    i = 0
    checkChar = True
    length = len(string)
    while i < length:
        if i + 1 == length - 1:
            checkChar = False
        if string[i] == "I":
            if checkChar == True and string[i+1] == 'V':
                    int = int + 4
            int = int + 1
        i+=1
        print(int)
    return int

print(nextChar('IV'))