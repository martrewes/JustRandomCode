def rot13(message):
    outstring = ""
    for each in message:
        if each.isalpha():
            if ord(each) > 96 and ord(each) < 110:
                outstring += chr(ord(each)+13)
            elif ord(each) < 78:
                outstring += chr(ord(each)+13)
            else:
                outstring += chr(ord(each)-13)
        else:
            outstring += each
            
    return outstring

print(rot13("How can you tell an extrovert from an\nintrovert at NSA? Va gur ryringbef,\ngur rkgebireg ybbxf ng gur BGURE thl'f fubrf."))