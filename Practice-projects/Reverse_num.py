# Method 1
Num = int(input())
Rev = 0
while Num != 0:
  Rev = Rev * 10 + (Num%10)
  Num //= 10
print(Rev) 

# Method 2 
Num = int(input("Enter a number: ")) 
R = ""
S = str(Num)
for s in S[::-1]:
  R+=s
Rev = int(R)
print(Rev)
