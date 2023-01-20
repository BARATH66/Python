# Gussing Number 

class player:
    def __init__(self, name, n):
        self.Name = name
        self.N = n

    def guess(self):
        Guess = int(input("Guess a number between 1 and 100 \N{Grinning face}")) 
        return Guess 
    def Guessing(self):
        Guess = self.guess() 
        N = self.N
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
            print(f'{N}=={Guess}') 
            count += 1
        return count 

    def Performance(self):
        C = self.Guessing()
        Name = self.Name 
        if C == 1:
            print(f"Excellent, {Name}")
        elif C >1 and C <=5:
            print(f"Good, {Name}")
        elif C >5 and C <10:
            print(f"Not bad, {Name}")
        else: 
            print(f"Better luck next time, {Name}")   
