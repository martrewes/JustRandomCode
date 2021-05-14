def count_sheeps(sheep):
  # TODO May the force be with you
    num_sheep =0
    for statement in sheep:
        if statement is True:
            num_sheep += 1
        else:
            pass
    return num_sheep

array1 = [True,  True,  True,  False,
          True,  True,  True,  True ,
          True,  False, True,  False,
          True,  False, False, True ,
          True,  True,  True,  True ,
          False, False, True,  True ];
              
count_sheeps(array1)