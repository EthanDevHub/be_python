# x = int(input("Please enter a number: "))

# if x > 20:
#     print("Your input > 20")
# elif x > 10:
#     print("Your input between 10 ~ 20")
# else:
#     print("Your input < 10")



num_1 = int(input("Please enter 1st number (num_1): "))
num_2 = int(input("Please enter 2nd number (num_2): "))
op = (input("Please enter the operation (+-*/): "))

if op == "+":
    print(f"num_1+num_2 = {num_1+num_2}")
elif op == "-":
    print(f"num_1-num_2 = {num_1-num_2}")
elif op == "*":
    print(f"num_1*num_2 = {num_1*num_2}")
elif op == "/":
    print(f"num_1/num_2 = {num_1/num_2}")
else:
    print("Invalid operaion, abort...")


print("Help you to fine the square root if it is an integer")
num_3 = int(input("Please enter an integer: "))

for x in range(num_3):
    if x**2 == num_3:
        print(f"The square root of {num_3} is {x}")
        break
else:
    print(f"{num_3} doesn't have integer square root...")