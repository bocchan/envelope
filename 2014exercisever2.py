# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt

#変数をx、パラメタをtとする直線
def f(x, t):
    return t * x - t**2

#quant-econより引用、一部改変
def subplots():
    "Custom subplots with axes throught the origin"
    fig, ax = plt.subplots()

    # Set the axes through the origin
    for spine in ['left', 'bottom']:
        ax.spines[spine].set_position('zero')
    for spine in ['right', 'top']:
        ax.spines[spine].set_color('none')
    return (fig, ax)

#包絡線を描く
fig, ax = subplots()  # Call the local version, not plt.subplots()
#xの定義域と描写個数を設定
x = np.linspace(-5, 5, 1000)
for u in range(31):
    t = -3 + 0.2 * u
    y = f(x, t)
    ax.plot(x, y, 'black', linewidth=0.5)
#gridの範囲を設定
plt.axis([-5, 5, -5, 10])
plt.tick_params(
    axis='both',which='both',labelbottom='off',labelleft='off')
#
for tic in ax.xaxis.get_major_ticks():
    tic.tick1On = tic.tick2On = False
for tic in ax.yaxis.get_major_ticks():
    tic.tick1On = tic.tick2On = False
plt.show()