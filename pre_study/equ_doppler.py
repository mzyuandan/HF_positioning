import math
import numpy as np
import matplotlib as mpl
mpl.use('tkagg')

import matplotlib.pyplot as plt

def fun_fd(x, v, f0, fd, c):
    tp = ((v*f0) / (c*fd)) ** 2 - 1
    y = x * np.sqrt(tp)
    return y

c = 3e5
v = 10
f0 = 1e9
fd = 3e4
x = np.arange(-50, 51, 1)
print(x)

y = np.zeros((101,1))
for i in range(0, 101):
    y[i] = fun_fd(x[i], v, f0, fd, c)
print(y)

fig = plt.figure()
plt.plot(x, y)
plt.show()