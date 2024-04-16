
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0.01,100,1000)
x1=np.linspace(-1,100,1000)
y= np.log(x)
y1=-4*x1**0
plt.figure(figsize=(20,3))

plt.subplot(111)
points=np.array([0, 1, 2, 3, 4, 5,6,7,8,9,10 ])
labels = [r'$0$', r'$1$',r'$2$',r'$3$',r'$4$',r'$5$', r'$6$',r'$7$',r'$8$',r'$8$',r'$9$']
plt.xticks(points, labels)

plt.xlim(-1.5, 15)
plt.ylim(-5, 3)

plt.grid(alpha=0.75, linestyle=':')

plt.plot(x,y, color='deepskyblue', label=r'$y=\ln(x)$')
plt.plot(x1, y1, color='salmon', label=r'$y=4$')
plt.fill_between(x,y, y1,color='pink')

plt.legend()

plt.title('График')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.show()
