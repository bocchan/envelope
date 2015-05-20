import numpy as np
import matplotlib.pyplot as plt


#A short-run cost function:C
def C(x, k):
    return  x**3 / (k+1) + 2 * k + 5
#make figure class and axis class
fig, ax = plt.subplots()

#linspace('minimam of x", "max of x", "dots")
x = np.linspace(0, 6, 100)

#grid range, axis(["min x", "max x", "min y", "max y"])
plt.axis([0, 6, 0, 50])

#generate y, n times
for k in range(10):
    y = C(x, k)

#indicate clours and linewidth for each (x, y)
    ax.plot(x, y, 'black', linewidth=0.5)

#show the graph
plt.show()