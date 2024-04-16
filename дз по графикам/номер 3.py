import matplotlib.pyplot as plt
import numpy as np
import math as mt
t = np.linspace(0, 2*np.pi, 1000)
y_sin = mt.sqrt(3)*np.sin(t)
y_cos = 1- np.cos(t)


plt.figure(figsize=(12, 6))

"""plt.subplot(121)

plt.plot(t, y_sin, color='deepskyblue', label=r'$y=\sqrt{3}\sin(x)$')
plt.plot(t, y_cos, color='salmon', label=r'$y=1- \cos(x)$')
plt.grid(alpha=0.75, linestyle=':')
points = np.array([0, np.pi, 2*np.pi])
labels = [r'$0$', r'$\pi$', r'$2\pi$']
plt.xticks(points, labels)
plt.title('График в декартовой системе')
plt.legend(loc=3)
plt.fill_between(t,  y_cos, y_sin, color='lightgray')
plt.subplot(122, projection='polar')"""


plt.polar(t, y_sin, color='deepskyblue', label=r'$y=\sqrt{3}\sin(x)$')
plt.polar(t, y_cos, color='salmon', label=r'$y=1- \cos(x)$')
plt.ylim(bottom=0)
plt.grid(alpha=0.75, linestyle=':')
plt.title('График в полярной системе')
plt.legend(loc=8)
plt.fill_between(t,  y_cos, y_sin, color='lightgray')
ax = plt.gca()
ax.set_rgrids(np.arange(0, 1.5, 0.5))
ax.set_rlabel_position(210)
plt.show()
