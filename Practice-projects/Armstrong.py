n = int(input("Enter a number: ")) 
Num = n
temp = 0
while Num!=0:
  digit = Num % 10
  temp += (digit)**3
  Num //= 10

if temp == n:
  print("It is an ARMSTRONG number")
else:
  print("It is NOT an ARMSTRONG number")
