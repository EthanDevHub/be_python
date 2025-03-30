def power(base, exp=0):
    return base**exp

# def divid(n1=0, n2=1):  ERROR: Once an arg is assign default vaule , then  arg(s) after it need to assign default value too.
def divid_two_num(n1=0, n2=1):
    return n1/n2

def covert_arg_2_tuple(*arg):
    return arg

def find_odd_elements_in_tuple_type(*arg):
    odd_entry=[]
    sum=0
    for x in arg:
        if(x%2 == 0):
            odd_entry.append(x)

    return tuple(odd_entry)

def average_score(*arg):
    sum=0
    for x in arg:
        sum+=x
    
    return sum/len(arg)

print(f"power(2, 3) = {power(2, 3)}")
print(f"power(2) = {divid_two_num(2)}")
print(f"divid_two_num(4, 2) = {divid_two_num(4, 2)}")
print(f"divid_two_num(n2=4, n1=2) = {divid_two_num(n2=4, n1=2)}")
print(f"divid_two_num(2) = {divid_two_num(2)}")
print(f"covert_arg_2_tuple(1, 3, 5) = {covert_arg_2_tuple(1, 3, 5)}")
print(f"find_odd_elements_in_tuple_type(1, 2, 3, 4, 5, 6, 7, 8) = {find_odd_elements_in_tuple_type(1, 2, 3, 4, 5, 6, 7, 8)}")
print(f"average_score(1, 2, 3, 4, 5, 6, 7, 8) = {average_score(1, 2, 3, 4, 5, 6, 7, 8)}")