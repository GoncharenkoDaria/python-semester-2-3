import matplotlib.pyplot as plt
import numpy as np

lst_znach=[]
lst_labels=[]
n1=int(input())
while n1!=0:
    print("введите название и значение ")
    a1 = str(input())
    lst_labels.append(a1)
    a2 = int(input())
    lst_znach.append(a2)
    n1=n1-1

plt.bar(lst_labels, lst_znach, color="cyan", label="значение1")
plt.plot(lst_labels, lst_znach, color="red", label="значение2")
plt.title('График')
plt.legend()
plt.show()
