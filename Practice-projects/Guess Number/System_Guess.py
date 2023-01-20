from random import *
import time  

class system:
    def __init__(self, n, max, min):
        self.Max = max
        self.Min = min 
        self.N = n 
    
    def Guessing(self):
        count = 0
        max = self.Max
        min = self.Min 
        N = self.N 
        while True:
            
            Guess = randint(min,max)
            if Guess > N:
                max = Guess-1
                print("Try Again \N{Thinking face}", Guess, sep=':')
                print("Greater")
                time.sleep(2)
                count += 1
            elif N > Guess:
                min = Guess+1
                print("Try Again \N{Thinking face}", Guess, sep=":") 
                print("Lesser") 
                time.sleep(2)
                count += 1
            elif Guess == N:
                print("You got it \N{Grinning face}", Guess, sep=":")  
                print("{}=={}".format(Guess, N)) 
                time.sleep(2)
                count += 1
                break 
        return count 

    def Performance(self):
        C = self.Guessing() 
        if C == 1: 
            print("Excellent")
        elif C > 1 and C <=5:
            print('Good')
        elif C >5 and C <10:
            print("Not bad")
        elif C >=10:
            print("Better luck next time") 
