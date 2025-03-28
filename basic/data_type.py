# Data Structure Comparison Table
# -------------------------------------------------------------------------------------------------------------------------------
# | Data Structure | Sequential |   Allows Duplicates?   | Mutable | Lookup (in)          | Main Usage                          |
# |----------------|------------|------------------------|---------|----------------------|-------------------------------------|
# | list           | Yes        | Yes                    | Yes     | O(n)                 | Storing ordered data, modifiable    |
# | tuple          | Yes        | Yes                    | No      | O(n)                 | Immutable collection, used as keys  |
# | set            | No         | No                     | Yes     | O(1) avg, O(n) worst | Unique elements, set operations     |
# | dict           | Yes        | Keys: No, Values: Yes  | Yes     | O(1) avg, O(n) worst | Fast lookups, key-value mapping     |
# -------------------------------------------------------------------------------------------------------------------------------

#number
1024

# String
"Hello World"

# Bool
True
False

# List - Sequential, Mutable, Slower
[128, 256, 512]
name_a = ["Alice", "Bob", "Carl"]
print(name_a[0])

# Tuple - Sequential, Immutable, Faster
(8, 16, 32, 48)
nato_a = ["Alpha", "Bravo", "Charlie"]
print(nato_a[1])


# Set - non-sequential, but it is O(1) for serach, no same element in one set
{1024, 2048, 4096}
fruit_a = {"Apple", "Banana", "Cherry"}

# Dictionary
{"Alice":"female", "Bob":"male"}

# Var
x=1024
print("The x = " + str(x))
print(f"The x = {x}")

