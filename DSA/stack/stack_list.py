from random import *

class stack:

    def __init__(self, container) -> None:
        self.container = container 

    def push(self, val):
        self.container.append(val)
    
    def pop(self):
        try:
            return self.container.pop()
        except IndexError:
            print("Stack is empty")
            print("Enter an element") 
            ch = int(input())
            return s.push(ch)

    def empty(self):
        if len(self.container) ==0:
            print(True)
        else:
            print(False, f'stack has {len(self.container)} element')     
    
    def show(self):
        for val in self.container:
            print(val)

def stackoperation (n):
    stacklist = [randint(10, 99) for i in range(n)] 
    return stacklist 
tot = int(input("How many elements you want in the list"))
s = stack(stackoperation(tot))
while True:
    print("""
        Enter 1 to add element
        Enter 2 to remove element
        Enter 3 to check is stack empty
        Enter 4 to display stack
        Enter 5 to stop the process
    """)
    choice = int(input())
    if choice == 1:
        ele = int(input("Enter a number"))
        s.push(ele)
    elif choice == 2:
        s.pop()
    elif choice == 3:
        s.empty()
    elif choice ==4:
        s.show() 
    elif choice == 5:
        break
    else:
        print("Enter correct number") 
