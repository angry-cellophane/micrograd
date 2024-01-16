import math
import numpy as np
import matplotlib.pyplot as plt

from micrograd.engine import draw_dot, Value

a = Value(2.0)
b = Value(-3.0)
c = Value(10.0)
d = a*b + c
print(d)
draw_dot(d)
