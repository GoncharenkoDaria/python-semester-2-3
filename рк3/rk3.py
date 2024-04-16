import matplotlib.pyplot as plt
import numpy as np

mode = "r+"
try:
  file = open("rk3.txt", mode)
except FileNotFoundError:
  print("Ошибка: Файл не найден")
else:
  print("Файл для чтения открыт успешно")
n=3
A=[]
file_data=[]
x_values=[]
y_values1=[]
y_values2=[]
y_values3=[]
y_values4=[]
for line in file:
  A.append([int(x1) for x1 in line.split()])
print(A)

for i in range(3):

    x_values.append(A[i][0])
    y_values1.append(A[i][1])
    y_values2.append(A[i][2])
    y_values3.append(A[i][3])
    y_values4.append(A[i][4])
print(x_values, y_values1,y_values2,y_values3,y_values4)

'''
point1=[]
point2=[]
point3=[]
point4=[]

point1.append(x_values[0])
point1.append(y_values1[0])
point2.append(x_values[1])
point2.append(y_values1[1])'''


plt.scatter (x_values, y_values1)
z1 = np.polyfit (x_values, y_values1, 1 )
p = np.poly1d (z1)
print(z1)
plt.plot (x_values, p(x_values), color="cyan", label="набор 1")

plt.scatter (x_values, y_values2)
z2 = np.polyfit (x_values, y_values2, 1 )
p = np.poly1d (z2)
print(z2)
plt.plot (x_values, p(x_values), color="blue", label="набор 2")

plt.scatter (x_values, y_values3)
z3 = np.polyfit (x_values, y_values3, 1 )
p = np.poly1d (z3)
print(z3)
plt.plot (x_values, p(x_values), color="red", label="набор 3")

plt.scatter (x_values, y_values4)
z4 = np.polyfit (x_values, y_values4, 1 )
p = np.poly1d (z4)
print(z4)
plt.plot (x_values, p(x_values), color="orange", label="набор 4")

plt.title('График')
plt.legend()
plt.show()