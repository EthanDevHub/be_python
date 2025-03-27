print("*************** Set practices (Mutable but slower) ***************\n")
#Set
S1 = {1, 2, 3}
print(f"S1 = {S1}")

print("Practice \"in\" and \"not in\"...")
print(f"Value 1 is in S1: {1 in S1}")
print(f"Value 3 is in S1: {3 in S1}")
print(f"Value 4 is in S1: {4 in S1}")
print(f"Value 5 is NOT in S1: {4 not in S1}")
print("\n")

print("I can collect the same elements from the given sets...")
S2 = {2, 3, 4, 5}
S3 = {6, 7, 8, 9}
print(f"S1 = {sorted(S1)}\nS2 = {sorted(S2)}\nS3 = {sorted(S3)}")
print(f"S1 & S2 = {S1 & S2}")
print(f"S1 & S2 & S3 = {S1 & S2 & S3}")
print("\n")

print("I can collect each element once from the given sets...")
print(f"S1 = {S1}\nS2 = {S2}\nS3 = {S3}")
print(f"S1 | S2 | S3 = {S1 | S2 | S3}")
print("\n")

print("I can remove S1 those duplicate elements from the given sets...")
print(f"S1 = {S1}\nS2 = {S2}\nS3 = {S3}")
print(f"S1 - S2 - S3 = {S1 - S2 - S3}")
print("\n")

print("I can collect those non-duplicate elements in the given sets...")
print(f"S1 = {S1}\nS2 = {S2}\nS3 = {S3}")
print(f"S1 ^ S2 = {S1 ^ S2}")
print(f"S1 ^ S2 ^ S3 = {S1 ^ S2 ^ S3}")
print("\n")

print("I can check whether a character exist in a word...")
S = set("Hello World!!!")
is_found = "h" in S

print(f"The word = {S}")
print(f"h is in the string \"Hello World!!!\": {is_found}")
print("\n")

