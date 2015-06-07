%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt


#A short-run cost function:C
def C(x, k):
    return  x**4 / k + k
#The long-run cost fun. for C
def CL(x):
    return 2 * x**2
#
fig, ax = plt.subplots()

#linspace('minimam of x", "max of x", "dots")
x = np.linspace(0, 10, 100)

miny = []
#grid
plt.axis([0, 5, 0, 50])

#generate y n times
for u in range(100):
    k = 0.1 * u + 0.1
    y = C(x, k)
#colors)http://www.w3schools.com/html/html_colornames.asp
    plt.plot(x, y, '#7fffd4', linewidth=0.5)
    for i in x:
        if C(x,k)[i] <= CL(x)[i] + 0.01515:
            miny.append(i)
plt.plot(x,miny,'.', color='r')
            
#show the graph
plt.show()