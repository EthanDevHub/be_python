# while loop
print("A while loop sum test...")
margin = int(input("Please enter the margin: "))
sum = 0
n = 0

while n <= margin: 
    sum+=n
    n+=1

print(f"The SUM from 0 to {margin} = {sum}")
print("\n")

# for loop
print("A for loop sum test...")
margin = int(input("Please enter the margin: "))
sum = 0
n = 0

for n in range(margin+1):
    sum+=n

print(f"The SUM from 0 to {margin} = {sum}")
print("\n")
