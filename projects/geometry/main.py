# ============================
# Import packet modules
# ============================
# pkt_geometry -> "store"
# line.py      -> "warehouse"
# slope()      -> "product"
# 
# The file __init__.py is necessary in packet folder, this make moudle folder becaome a packet.
# Declare some import in __init__.py make the main.py look cleaner.
# 
# Useage:
#   [__init__.py]
#       from .warehouse import product as product_name
#   [main.py]
#       from store import product_name

# import pkt_geometry.point as geo_point
# import pkt_geometry.line as geo_line
from pkt_geometry import line_distance, slope, point_distance
import sys

# ============================
# Private
# ============================
print(f"The path = \n{sys.path}")
print("\n")
print(f"The distance between point 3 and 4 = {point_distance(3,4)}")
print(f"The slope between point (1, 1) and (3, 3) = {slope(1, 1, 3, 3)}")
