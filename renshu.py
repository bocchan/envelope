import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots()
x = np.linspace(0, 10, 200)
for t in range(3):
    y = np.sin(x) + t
    ax.plot(x, y, 'b-', linewidth=2)
plt.show()