import matplotlib.pyplot as plt
import numpy as np



def spiral(x):
    return np.exp(0.1*x)


x_spiral = np.linspace(0, 8*np.pi, 1000)
y_spiral = spiral(x_spiral)


plt.figure(figsize=(6, 6))

plt.polar(x_spiral, y_spiral, color='deepskyblue',
          label=r'$y=\sin(x)+\mathrm{noise}$')

x_bot = np.linspace(4*np.pi, 6*np.pi)
x_top = np.linspace(6*np.pi, 8*np.pi)
plt.fill_between(x_bot, spiral(x_bot), spiral(x_top), color='gray')

plt.legend(loc=8)
plt.title('Логарифмическая спираль')
plt.ylim(bottom=0)
plt.grid(alpha=0.75, linestyle=':')

plt.show()
