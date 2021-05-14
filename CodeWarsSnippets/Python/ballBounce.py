def bouncing_ball(h, bounce, window):
    if not h > 0:
        return -1
    if bounce == 0:
        return -1
    if window > h:
        return -1
    # your code
    passes = 0
    while h > window:
        passes +=1
        h = h * round(bounce, 2)
        if h > window:
            passes +=1
    return passes


print(bouncing_ball(158475154, 0.9584, 12546))