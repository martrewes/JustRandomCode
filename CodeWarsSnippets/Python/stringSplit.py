def spin_words(sentence):
    # Your code goes here
    index = sentence.split()
    new = []
    temp = ""
    for each in index:
        if len(each) > 4:
            each = "".join(reversed(each))
            new.append(each)
        else:
            new.append(each)
    string = " ".join(new)
    print(string)
    return string

spin_words("Hey fellow warriors")