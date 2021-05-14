def find_outlier(int):
    odds = 0
    evens = 0
    index = 0
    for i in int:
        if i % 2 == 0:
            evens +=1
            index +=1
        else:
            odds +=1
            index +=1
    
    if evens > odds:
        for i in int:
            if i % 2 == 1:
                return i
    else:
        for i in int:
            if i % 2 == 0:
                return i



print(find_outlier([12, 15, 14, 16]))