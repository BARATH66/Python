# Gussing Number 
from random import *
import time 

def Guessing(N, Guess):
    count = 0
    while Guess != N:
        if Guess < N:
            print("Lesser")
            Guess = int(input("Try again: \N{Thinking face} "))
            count += 1
        elif Guess > N:
            print("Greater")
            Guess = int(input("Try Again\N{Thinking face}"))  
            count += 1
        else:
            print("You got right number") 
            count += 1
    return count 

def Performance(name, count):
    C = count
    if C == 1:
        print(f"Excellent, {name}")
    elif C >1 and C <=5:
        print(f"Good, {name}")
    elif C >5 and C <10:
        print("Not bad, {name}")
    else: 
        print("Better luck next time, {name}")  

Name = input("Enter your name").upper()
print(f"Hi {Name}")
time.sleep(0.2)
N = randint(1,100)
Guess = int(input("Guess a number between 1 and 100 \N{Grinning face}")) 
Performance(Name, Guessing(N, Guess)) 
