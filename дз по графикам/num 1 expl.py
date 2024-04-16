
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,5*np.pi,1000)
y1 = 4
y2 = np.log(x)
plt.figure(figsize=(18,4))

points=np.array([0, np.pi, 2*np.pi, 3*np.pi, 4*np.pi, 5*np.pi ])
labels = [r'$0$', r'$\pi$',r'$2\pi$',r'$3\pi$',r'$4\pi$',r'$5\pi$']
plt.xticks(points, labels)

plt.xlim(0, 4*np.pi)
plt.ylim(-1.5, 1.5)

plt.grid(alpha=0.75, linestyle=':')

plt.subplot(121)
plt.plot(x, y1, color='deepskyblue', label=r'$y=4$')
plt.plot(x, y2, color='salmon', label=r'$y=\ln(x)$')
plt.fill_between(x,0,y,color='pink')

plt.legend()

plt.title('График в декартовой системе')
plt.legend(loc=3)
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.show()
