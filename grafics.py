
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,5*np.pi,1000)
y=np.sin(x)+0.05*np.random.randn(1000)
plt.figure(figsize=(18,4))

points=np.array([0, np.pi, 2*np.pi, 3*np.pi, 4*np.pi, 5*np.pi ])
labels = [r'$0$', r'$\pi$',r'$2\pi$',r'$3\pi$',r'$4\pi$',r'$5\pi$']
plt.xticks(points, labels)

plt.xlim(0, 4*np.pi)
plt.ylim(-1.5, 1.5)

plt.grid(alpha=0.75, linestyle=':')

plt.plot(x,y, color='deepskyblue', label=r'$y=\sin(x)+\mathrm{noise}$')
plt.fill_between(x,0,y,color='pink')

plt.legend()

plt.title('График')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.show()
