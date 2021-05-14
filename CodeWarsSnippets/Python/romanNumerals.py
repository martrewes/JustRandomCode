def solution(n):
    # TODO convert int to roman string
    stringRoman = ''
    
    while n > 0:
        if n >= 1000:
            stringRoman = stringRoman + 'M'
            n = n - 1000
            continue
        if n >= 900:
            stringRoman = stringRoman + 'CM'
            n = n - 900
            continue
        if n >= 500:
            stringRoman = stringRoman + 'D'
            n = n - 500
            continue
        if n >= 400:
            stringRoman = stringRoman + 'CD'
            n = n - 400
            continue
        if n >= 100:
            stringRoman = stringRoman + 'C'
            n = n - 100
            continue
        if n >= 90:
            stringRoman = stringRoman + 'XC'
            n = n - 90
            continue
        if n >= 50:
            stringRoman = stringRoman + 'L'
            n = n - 50
            continue
        if n >= 40:
            stringRoman = stringRoman + 'XL'
            n = n - 40
            continue
        if n >= 10:
            stringRoman = stringRoman + 'X'
            n = n - 10
            continue
        if n >= 9:
            stringRoman = stringRoman + 'IX'
            n = n - 9
            continue
        if n >= 5:
            stringRoman = stringRoman + 'V'
            n = n - 5
            continue       
        if n >= 4:
            stringRoman = stringRoman + 'IV'
            n = n - 4
            continue
        if n >= 1:
            stringRoman = stringRoman + 'I'
            n = n - 1
    return stringRoman

print(solution(1889))

#   Symbol    Value
#   I          1
#   V          5
#   X          10
#   L          50
#   C          100
#   D          500
#   M          1,000