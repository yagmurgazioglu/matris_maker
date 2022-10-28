# import matplotlib.pyplot as plt
# import numpy as np
# x = np.arange(-5,5.1,0.5)
# y= ((3*x)**3)-((2*x)**2)
# plt.plot(x, y,"o-.g")
# plt.show()
# -----------------------------
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-5,5.1,0.5)
y= ((3*x)**3)-((2*x)**2)
z= x**2
plt.plot(x, y,"o-.g")
plt.plot(x, z,"x-.g")
plt.show()