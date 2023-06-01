# import pyautogui as gui
# import time
# import random, string

# number = input("Enter the number: ")

# time.sleep(5)

# for i in range(int(number)):
#     str = string.ascii_lowercase
#     message = "".join(random.sample(string, 10))
#     gui.typewrite(message)
#     gui.press('Enter')


import pyautogui as gui
import time
import random
import string

number = input("Enter the number: ")

time.sleep(5)

for i in range(int(number)):
    message = "".join(random.sample(string.ascii_lowercase, 10))
    gui.typewrite(message)
    gui.press('Enter')

