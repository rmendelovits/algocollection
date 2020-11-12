from enum import Enum

class DLogTime(Enum):
    constant = 0 # O(1)
    logarithmic = 1 # O(log n)

class DTime(Enum):
    linear = 2 # O(n)
    linearithmic = 3 # O(n log n)
    quadratic = 4 # O(n^2)
