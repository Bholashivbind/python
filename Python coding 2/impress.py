import pyautogui as py
import time

message = "Hello Rahul sir kaise ho "

count = 1
time.sleep(2)

for i in range(200):
   py.typewrite(message + " " + str(count))
   py.press('Enter')
   count = count + 1

py.typewrite("Rahul sir ")
py.press('Enter')

