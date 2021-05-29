def small_enough(array, limit):
    for each in array:
        if each > limit:
            return False
        else:
            pass
    return True
    

print(small_enough([78, 33, 22, 44, 88, 9, 6] ,87))