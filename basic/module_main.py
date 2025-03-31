# ============================
# Import
# ============================
import sys

# Don't forget to append the path of modules you save before import
sys.path.append("/home/ethan/be_python/basic/modules")
import geometry as geo


# ============================
# Public
# ============================
# Check sys module's var
print(sys.platform)
print(sys.maxsize)

# print the module's search path
print(sys.path)
# print(geo.path)

# Implement geometry module
dis = geo.distance_bwt_two_point(1, 1, 5, 5,)

slope = geo.slope(1, 2, 5, 6)

print(f"The distance between (1, 1) and (5, 5) is {dis}")
print(f"The slope between (1, 2) and (5, 6) is {slope}")

