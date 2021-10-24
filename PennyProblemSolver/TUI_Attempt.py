#109x40 for some bizzare reason.
import py_cui

def my_function():
    total = int(tboxStack._text) * float(tboxCoinWeight._text)
    tboxTotal.set_text(str(round(total,2)))

root = py_cui.PyCUI(8, 2)
root.set_title('Penny Problem Solver')
label = root.add_block_label('______                       ______          _     _                \n| ___ \                      | ___ \        | |   | |               \n| |_/ /__ _ __  _ __  _   _  | |_/ / __ ___ | |__ | | ___ _ __ ___  \n|  __/ _ \ \'_ \| \'_ \| | | | |  __/ \'__/ _ \| \'_ \| |/ _ \ \'_ ` _ \ \n| | |  __/ | | | | | | |_| | | |  | | | (_) | |_) | |  __/ | | | | |\n\_|  \___|_| |_|_| |_|\__, | \_|  |_|  \___/|_.__/|_|\___|_| |_| |_|\n                       __/ |                                        \n                      |___/', 0, 0, column_span=2, row_span=4, padx=0, center=False)
label2 = root.add_block_label('Take your stacks of penny\'s and line them up. Take 1 penny from the first pile and put it to the side. \nNow take 2 pennies from the next pile, then 3 from the third and so on. Once you get to the end of the \nline of stacks, take all of the pennies and weigh them. Now fill in the below:', 2, 0, column_span=2, row_span=2, padx=1, center=True)
tboxStack = root.add_text_box('Enter how many in each Stack:',3,0)
tboxCoinWeight = root.add_text_box('Weight of each Coin: ',3,1)
tboxCoinFake = root.add_text_box('Weight of the Fake: ',4,0)
tboxGivenWeight = root.add_text_box('The Weight of removed Coins: ',4,1)
tboxTotal = root.add_text_box('Total prot.', 5,0)
button = root.add_button('Get', 7, 1, column_span=1, row_span=1, command=my_function)
root.start()


