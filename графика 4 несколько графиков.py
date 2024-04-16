import matplotlib.pyplot as plt
import numpy as np
t = np.linspace(0, 2*np.pi, 1000)
y_sin = np.sin(t)+0.05*np.random.randn(1000)
#y_cos = np.cos(t)+0.05*np.random.randn(1000)
y_cos =4

plt.figure(figsize=(12, 6))

plt.subplot(121)

plt.plot(t, y_sin, color='deepskyblue', label=r'$y=\sin(x)+\mathrm{noise}$')
plt.plot(t, y_cos, color='salmon', label=r'$y=\cos(x)+\mathrm{noise}$')
plt.grid(alpha=0.75, linestyle=':')
points = np.array([0, np.pi, 2*np.pi])
labels = [r'$0$', r'$\pi$', r'$2\pi$']
plt.xticks(points, labels)
plt.title('График в декартовой системе')
plt.legend(loc=3)

plt.subplot(122, projection='polar')

ax = plt.gca()
ax.set_rgrids(np.arange(0, 1.5, 0.5))
ax.set_rlabel_position(210)
plt.polar(t, y_sin, color='deepskyblue', label=r'$y=\sin(x)+\mathrm{noise}$')
plt.polar(t, y_cos, color='salmon', label=r'$y=\cos(x)+\mathrm{noise}$')
plt.ylim(bottom=0)
plt.grid(alpha=0.75, linestyle=':')
plt.title('График в полярной системе')
plt.legend(loc=8)

plt.show()
