#   NOTES:
#   
#   humanYears >= 1
#   humanYears are whole numbers only
#   Cat Years
#   15 cat years for first year
#   +9 cat years for second year
#   +4 cat years for each year after that
#   Dog Years
#   15 dog years for first year
#   +9 dog years for second year
#   +5 dog years for each year after that

def human_years_cat_years_dog_years(human_years):
    # Your code here

    if human_years > 2:
        cat_y3 = (human_years - 2) * 4
        dog_y3 = (human_years - 2) * 5
        cat_y2 = 9
        dog_y2 = 9
        cat_y1 = 15
        dog_y1 = 15
        catYears = cat_y1+cat_y2+cat_y3
        dogYears = dog_y1+dog_y2+dog_y3
    elif human_years == 2:
        catYears = 24
        dogYears = 24
    elif human_years == 1:
        catYears = 15
        dogYears = 15

    return [human_years, catYears, dogYears]

human_years_cat_years_dog_years(4)
   # return [0,0,0]