#!/usr/bin/python
################ PENNY PROBLEM SOLVER #################
# Take your stacks of penny's and line them up. Take  #
# 1 penny from the first pile and put it to the side. #
# Now take 2 pennies from the next pile, then 3 from  #
# the third and so on. Once you get to the end of the #
# line of stacks, take all of the pennies and weigh   #
# them. Now fill in the below:                        #
# --------------------------------------------------- #

stackCount = int(input("# Enter amount of Stacks: ", end = \r))

stackContents = int(input("Enter how many in each Stack: "))
coinWeight = float(input("Weight of each Coin: "))
coinFake = float(input("Weight of the Fake: "))
givenWeight = float(input("The Weight of removed Coins: "))

targetWeight = (stackCount / 2) * (stackCount + 1)
stackDifference = targetWeight - givenWeight
pileNumber = int(stackDifference / coinFake)


print("Pile Number: " + str(pileNumber))