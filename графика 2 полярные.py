import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0,5*np.pi,1000)
y=np.sin(x)+0.05*np.random.randn(1000)

plt.figure(figsize=(6, 6))

plt.polar(x, y, color='deepskyblue', label=r'$y=\sin(x)+\mathrm{noise}$')

plt.fill_between(x, 0, y, color='gray')
plt.title('Название графика')
plt.ylim(bottom=0)
plt.grid(alpha=0.75, linestyle=':')
plt.legend(loc=8)

ax = plt.gca()
ax.set_rgrids([0.2*i for i in range(7)])
ax.set_rlabel_position(210)

plt.show()
