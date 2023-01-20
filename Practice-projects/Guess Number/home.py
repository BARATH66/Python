from Player_Guess import player
from System_Guess import system 
import time
from random import *

name = input("Enter your name: ").upper()
print(f"Welcome {name}")
time.sleep(2)
print("""
    S -- to set a number
    P -- to find the number
""")
while True:
    start = input("Enter S/P: ").upper()
    if start == 'S':
        N = int(input("Enter a number: "))
        s = system(n=N, max=100, min=1) 
        s.Performance() 
        break
    elif start == 'P':
        N = randint(1,100)
        p = player(n=N, name=name) 
        p.Performance()
        break 
    else:
        print('Enter right letter (S/P)') 
        start = input("Enter S/P").upper()
