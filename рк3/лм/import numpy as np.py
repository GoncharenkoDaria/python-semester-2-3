import numpy as np
import matplotlib.pyplot as plt
import array
x = []
y1 = []
y2 = []
y3 = []
try:
    with open("rk3_1.txt") as file:
        x.append(list(map(int,  file.readline().split())))
        y1.append(list(map(int,  file.readline().split())))
        y2.append(list(map(int,  file.readline().split())))
        y3.append(list(map(int,  file.readline().split())))
except FileNotFoundError:
    print("Ошибка: Файл не найден")

    
x=np.array(x[0])
y1=np.array(y1[0])
y2=np.array(y2[0]) 
y3=np.array(y3[0])


plt.plot(x, y1, 'ro')
plt.plot(x, y2, 'ro')
plt.plot(x, y3, 'ro')

x1_t = array.array('i', x)
y1_t = array.array('i', y1)
y2_t = array.array('i', y2)
y3_t = array.array('i', y3)

x_t = x1_t * 3

y_t = y1_t + y2_t + y3_t


z = np.polyfit (x_t, y_t, 1)
p = np.poly1d (z)
plt.plot (x, p(x), color="orange", label="Линия тренда")



plt.title('График')
plt.legend()
plt.show()

