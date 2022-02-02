from random import random


import random

numArray = []
i = 0

#Ascii art from patorjk.com
largeLine1 = [".------. ",".------. ",".------. ",".------. ",".------. ",".------. ",".------. ",".------. ",".------. ",".------. "]
largeLine2 = ["|1.--. | ","|2.--. | ","|3.--. | ","|4.--. | ","|5.--. | ","|6.--. | ","|7.--. | ","|8.--. | ","|9.--. | ","|10--. | "]
largeLine3 = ["| :/\: | ","| (\/) | ","| :(): | ","| :/\: | ","| :/\: | ","| (\/) | ","| :(): | ","| :/\: | ","| :/\: | ","| :/\: | "]
largeLine4 = ["| (__) | ","| :\/: | ","| ()() | ","| :\/: | ","| (__) | ","| :\/: | ","| ()() | ","| :\/: | ","| (__) | ","| :\/: | "]
largeLine5 = ["| '--'1| ","| '--'2| ","| '--'3| ","| '--'4| ","| '--'5| ","| '--'6| ","| '--'7| ","| '--'8| ","| '--'9| ","| '--10| "]
largeLine6 = ["`------' ","`------' ","`------' ","`------' ","`------' ","`------' ","`------' ","`------' ","`------' ","`------' "]

#set-up random integers
while i < 100:
    numArray.append(random.randint(1,9))
    i+=1

#fancy printing
for eachInt in numArray:
    print(largeLine1[eachInt-1] + largeLine1[eachInt] + largeLine1[eachInt] + largeLine1[eachInt] + largeLine1[eachInt] + largeLine1[eachInt] + largeLine1[eachInt] + largeLine1[eachInt] + largeLine1[eachInt] + largeLine1[eachInt])
    print(largeLine2[eachInt-1] + largeLine2[eachInt] + largeLine2[eachInt] + largeLine2[eachInt] + largeLine2[eachInt] + largeLine2[eachInt] + largeLine2[eachInt] + largeLine2[eachInt] + largeLine2[eachInt] + largeLine2[eachInt])
    print(largeLine3[eachInt-1] + largeLine3[eachInt] + largeLine3[eachInt] + largeLine3[eachInt] + largeLine3[eachInt] + largeLine3[eachInt] + largeLine3[eachInt] + largeLine3[eachInt] + largeLine3[eachInt] + largeLine3[eachInt])
    print(largeLine4[eachInt-1] + largeLine4[eachInt] + largeLine4[eachInt] + largeLine4[eachInt] + largeLine4[eachInt] + largeLine4[eachInt] + largeLine4[eachInt] + largeLine4[eachInt] + largeLine4[eachInt] + largeLine4[eachInt])
    print(largeLine5[eachInt-1] + largeLine5[eachInt] + largeLine5[eachInt] + largeLine5[eachInt] + largeLine5[eachInt] + largeLine5[eachInt] + largeLine5[eachInt] + largeLine5[eachInt] + largeLine5[eachInt] + largeLine5[eachInt])
    print(largeLine6[eachInt-1] + largeLine6[eachInt] + largeLine6[eachInt] + largeLine6[eachInt] + largeLine6[eachInt] + largeLine6[eachInt] + largeLine6[eachInt] + largeLine6[eachInt] + largeLine6[eachInt] + largeLine6[eachInt])
    print("Bugger it\nLet's try")
    quit()
#print(numArray)
#print(len(numArray))