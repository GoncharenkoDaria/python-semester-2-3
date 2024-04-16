#n-столбцов, m-строк
"""
1 2 3 4 5
5 6 7 8 9
1 3 5 7 9
2 4 6 8 2
'''
4 5 6 7
1 2 3 5
6 7 2 3
9 8 3 2
1 4 2 8
"""
m, n=map(int, input().split())
def func1(m,n): #ввод
  a=[]
  for i in range(n):
    a.append(list(map(int, input().split()))[:m])
  return a
def func2(a): #вывод
  for i in range(len(a)):
    for j in range(len(a[0])):
      print("%3d" % a[i][j], end=" ")
    print()
  print()
def func3(a):# минимальный
  print(min(a))
def func4(a):#максимальный
  print(max(a))
def func5(a):# обрезать по короткой стороне
  b=[]
  if m>n:
    for i in range(n):
      b.append(a[i].copy())
    a=b.copy()
  else:
    for i in range(m):
      a[i]=a[i][:m]
  return a, min(n,m), min(n,m)
def func6(a):#транспонировать
  c=[]
  for i in range(len(a)):
    b=[]
    for j in range(len(a[0])):
      b.append(a[j][i])
    c.append(b.copy())
  a=c.copy()
  return a
def func7(a):#заменить элементы на сумму цифр элементов
  for i in range(len(a)):
    for j in range(len(a[0])):
      sum=0
      while a[i][j]>0:
        d=a[i][j]%10
        sum+=d
        a[i][j]=a[i][j]//10
      a[i][j]=sum
  return a
def func8(a): #Дополнить нулями по длинной стороне
  if m>n:
    for i in range(n+1):
      a[i].append(0)
  else:
    a.append(list([0]*(m+1)))
  return a
def func9(a, x, y):#Поменять местами столбец x и y
  for i in range(len(a)):
    b=a[i][x]
    a[i][x]=a[i][y]
    a[i][y]=b
  return a
def func10(a,x,y):#Поменять местами строки x и y
  for i in range(len(a[0])):
    b=a[x][i]
    a[x][i]=a[y][i]
    a[y][i]=b
  return a
def func11(a):#Сумма элементов главной диагонали
  s=0
  for i in range(len(a)):
    s+=a[i][i]
  return s
def func12(a):#Произведение элементов побочной диагонали
  s=1
  for i in range(len(a)):
    s*=a[i][len(a)-i-1]
  return s
def func13(a):#Глав. диагональ арифм. прогрессия проверка
  b=[]
  for i in range(len(a)):
    b.append(a[i][i])
  p=True
  d=b[1]-b[0]
  for i in range(1,len(b)-1):
    if b[i+1]-b[i]!=d:
      p=False
  return p
def func14(a):#Сумма элементов верхнего треугольника
  s=0
  for i in range(len(a)//2):
    for j in range(i+1, len(a)-i-1):
      s+=a[i][j]
  return s
def func15(a):#Нижнего
  s = 0
  for i in range(len(a) // 2, len(a)):
    for j in range(len(a) - i, i):
      s += a[i][j]
  return s
def func16(a):#Правого
  s = 0
  for j in range(len(a) // 2, len(a)):
    for i in range(len(a) - j, j):
      print(a[i][j],i,j)
      s += a[i][j]
  return s
def func17(a):#Левого
  s=0
  for j in range(len(a[0])//2):
    for i in range(j+1, len(a[0])-j-1):
      s+=a[i][j]
  return s
def func18(a):#Повернуть на 90 градусов по часовой
  b=[]
  for i in range(len(a)):
    c=[]
    for j in range(len(a[0])):
      c.append(0)
    b.append(c.copy())
  for i in range(len(a)):
    for j in range(len(a[0])):
      b[i][j]=a[len(a[0])-j-1][i]
  a=b.copy()
  return a
def func19(a):#Повернуть на 90 градусов против часовой
  b=[]
  for i in range(len(a)):
    c=[]
    for j in range(len(a[0])):
      c.append(0)
    b.append(c.copy())
  for i in range(len(a)):
    for j in range(len(a[0])):
      b[i][j]=a[j][len(a[0])-i-1]
  a=b.copy()
  return a
def func20(a,x,y): #поменять треуг. х на у
  if x==y:
    return a
  elif (x==1 or x==3) and (y==1 or y==3):
    for i in range(len(a) // 2):
      for j in range(i + 1, len(a) - i - 1):
        b=a[i][j]
        a[i][j]=a[len(a)-i-1][j]
        a[len(a) - i - 1][j]=b
    return a
  elif (x==2 or x==4) and (y==2 or y==4):
    for j in range(len(a[0]) // 2):
      for i in range(j + 1, len(a[0]) - j - 1):
        b=a[i][j]
        a[i][j]=a[i][len(a[0])-j-1]
        a[i][len(a[0]) - j - 1]=b
    return a
  elif (x==4 or x==1) and (y==4 or y==1):
    for j in range(len(a[0]) // 2):
      for i in range(j + 1, len(a[0]) - j - 1):
        b=a[i][j]
        a[i][j]=a[j][i]
        a[j][i]=b
    return a
  elif (x==4 or x==3) and (y==4 or y==3):
    for j in range(len(a[0]) // 2):
      for i in range(j + 1, len(a[0]) - j - 1):
        b=a[i][j]
        a[i][j]=a[len(a)-j-1][i]
        a[len(a)-j-1][i]=b
    return a
  elif (x==2 or x==3) and (y==2 or y==3):
    for j in range(len(a) // 2, len(a)):
      for i in range(len(a) - j, j):
        b=a[i][j]
        a[i][j]=a[j][i]
        a[j][i]=b
    return a
  elif (x==2 or x==1) and (y==2 or y==1):
    for i in range(len(a) // 2):
      for j in range(i + 1, len(a) - i - 1):
        b = a[i][j]
        a[i][j] = a[j][len(a) - i - 1]
        a[j][len(a) - i - 1] = b
    return a
def func21(a): #массив элементов матрицы в порядке змейки
  b=[]
  for i in range(len(a)):
    for j in range(len(a[0])):
      if i%2==0:
        b.append(a[i][j])
      else:
        b.append(a[i][len(a[0])-j-1])
  return b
def func22(a):#массив элементов диагоналей
  k=0
  b=[a[0][0]]
  for i in range(1, len(a)):
    k=i
    while k!=-1:
      b.append(a[abs(i-k)][k])
      k-=1
  for i in range(len(a), len(a)+len(a[0])-1):
    k=len(a)-1
    while (i-k)<len(a):
      b.append(a[i-k][k])
      k-=1
  return b
print ("Введите матрицу размера n на m.", "\n")
H=func1(n,m)
s = int(input("Введите пункт меню: "))
print()
while s!=0:
  if s==1:
    H=func1(n,m)
  if s==2:
    func2(H)
  if s==3:
    func3(H)
  if s==4:
    func4(H)
  if s == 5:
    func5(H)
  if s == 6:
    func5(H)
  if s == 7:
  if s == 8:
  print("Выберите пункт меню: ",  "\n")
  print("Ваш пункт: ")
  s = int(input())



