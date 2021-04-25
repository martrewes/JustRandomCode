def solution(number):
    sum = 0
    noThrees = (number - 1) // 3
    noFives = (number - 1) // 5
    while noThrees > 0:
        stable = noThrees
        if ((noThrees*3) % 5 != 0):
            var = noThrees * 3
        else:
            var = 0
        sum = sum + var
        noThrees-=1

    while noFives > 0:
        stable = noFives
        var = noFives * 5
        sum = sum + var
        noFives-=1
    
    print(sum)

print(solution(12))
