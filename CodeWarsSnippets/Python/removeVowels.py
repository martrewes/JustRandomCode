import re

def disemvowel(string_):
    removed = re.sub("a", "", string_, flags=re.IGNORECASE)
    removed = re.sub("e", "", removed, flags=re.IGNORECASE)
    removed = re.sub("i", "", removed, flags=re.IGNORECASE)
    removed = re.sub("o", "", removed, flags=re.IGNORECASE)
    removed = re.sub("u", "", removed, flags=re.IGNORECASE)
    return removed