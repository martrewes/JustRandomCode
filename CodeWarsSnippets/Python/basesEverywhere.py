def base_finder(seq):
    #Have fun!
    f = 0
    base = int(seq[f][-1])
    
    while f < 9:
       f +=1
       if base < int(seq[f][-1]):
           base = int(seq[f][-1])
    
    return base + 1    
        
print(base_finder(['1', '2', '3', '4', '5', '6', '10', '11', '12', '13']))