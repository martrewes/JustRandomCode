def kaprekar_split(n):
    #write code here...
    i = 1
    sq = n*n
    num_dig = len(str(sq))
    
    while i < num_dig:
        eq_parts = pow(10,i)
        if eq_parts == n:
            return -1
        num1 = int(str(sq)[:(i)])
        num2 =  int(str(sq)[(i - num_dig):])
        sum = num1+num2
        if sum == n:
            return i 
            break
        i +=1
    return -1

print(kaprekar_split(2223))