def series_summation(bound):
    sum = 0
    n = 0

    for n in range(bound+1):
        sum+=n
    
    return sum 
    # end of series_summation()



margin = input("Please enter the margin: ")

if margin == "":
    print("No input provided!")
else:
    try:
        margin = int(margin)  # covert to integer
        print(f"The SUM from 0 to {margin} = {series_summation(margin)}")
    except ValueError: # non-integer
        print("Invalid input! Please enter a valid number.")
print("\n")



