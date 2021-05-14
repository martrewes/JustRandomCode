

def get_count(input_str):
    num_vowels = 0
    # your code here
    vowels = ["a","e","i","o","u"]
    for char in input_str:
        if char in vowels:
            num_vowels += 1
    return num_vowels
    
get_count("Hello")