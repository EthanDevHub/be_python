
print("*************** List practices (Mutable but slower) ***************\n")
# List
list_a=[88, 90, 70, 75]
print(f"list_a={list_a}")
print(f"The 1st element is {list_a[1]}")
print("\n")

list_a[1]=95
print(f"Now change the list_a[1] to {list_a[1]}")
print(f"list_a={list_a}")
print("\n")

#delete element
list_a[1:3]=[]
print("Now delete the list_a[1] and list_a[2]")
print(f"list_a={list_a}")
print("\n")

# add elements
list_a+=[100, 99]
lenth=len(list_a)
print("Now append two elements: 100 and 99")
print(f"list_a={list_a}, now list_a has {lenth} elements")
print("\n")

print("Another way to append element, add a 79 at tail")
list_a.append(79)
lenth=len(list_a)
print(f"list_a={list_a}, now list_a has {lenth} elements")
print("\n")


#multiple list
data=[[1, 2, 3], [4, 5, 6]]
print(f"The data={data}")


# replace data
data[0][0:2]=[9, 9, 9]
print("Now change 1 and 2 to [9, 9, 9]")
print(f"The data become {data}")

print("\n*************** List practices (Mutable but slower) ***************")
print("\n\n")






print("*************** Tuple practices (Immutable but faster) ***************\n")

# Tuple
tuple_a=(1 ,2, 3)
print(f"tuple_a={tuple_a}")
# tuple_a[0]=5 //error
print(f"Try to change {{tuple_a[n]}} will compile error")

print("\n*************** Tuple practices (Immutable but faster) ***************")