names = [{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}]

def namelist(names):
    #your code here
    names.reverse()
    output = ""
    listlen = len(names)
    #print(listlen)
    while listlen > 0:
        if listlen == 1:
            output = output + names[listlen - 1]['name']
        if listlen == 2:
            output = output + names[listlen - 1]['name'] + " & "
        if listlen >= 3:
            output = output + names[listlen - 1]['name'] + ", "
            
        listlen -= 1
    
    print(output)

namelist(names)