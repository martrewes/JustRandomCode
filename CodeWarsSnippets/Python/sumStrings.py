def sum_str(a, b):
    # happy coding !
    if a == "":
        intA = 0
    else:
        intA = int(a)
    
    if b == "":
        intB = 0
    else:
        intB = int(b)
    sum = intA + intB
    return str(sum)

print(sum_str(2342, 9234))