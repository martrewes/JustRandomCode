def find_it(seq):
    d = {}
    for each in seq:
        if not str(each) in d:
            d[str(each)] = 1
        else:
            updated = d.get(str(each))
            updated +=1
            d1 = {str(each): updated}
            d.update(d1)
    for val in d.values():
        #print(val)
        if not val % 2 == 0:
            return list(d.keys())[list(d.values()).index(val)]
                #return 2
print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))