import numpy as np
import matplotlib

a = np.linspace(0, 100, 20)

b = a.reshape(10, -1)

print(a)
print(b)