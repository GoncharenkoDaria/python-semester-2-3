1############# функции к файлу
def func_file_matrix(a, m, n):
  print("Внести результат в файл? 1 - да. 2 - нет.")
  s_m=int(input())
  while s_m!=0:
    if s_m==1:
      file1.write(str(m)+" " +str(n) + "\n")
      for i in range(m):
        sep=" "
        for j in range(n):
          file1.write(sep + str(a[i][j]))
          sep=" "
        file1.write("\n")
      file1.write("\n\n")
      break
    if s_m==2:
      print("Не внесено.")
      break

def func_file_digit(m):
  print("Внести результат в файл? 1 - да. 2 - нет.")
  s_d=int(input())
  while s_d!=0:
    if s_d==1:
      
      file1.writelines(str(m)+"\n")
      break
    if s_d==2:
      print("Не внесено.")
      break


def func_file_array(ar):
  print("Внести результат в файл? 1 - да. 2 - нет.")
  s_a=int(input())
  while s_a!=0:
    if s_a==1:
      
      file1.writelines(str(ar)+"\n")
      break
    if s_a==2:
      print("Не внесено.")
      break
############# функции к матрицам
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
  min_matr=min(map(min, a))
  return(min_matr)
def func4(a):#максимальный
  max_matr= max(map(max, a))
  return(max_matr)
def func5(a):# обрезать по короткой стороне
  b=[]
  if m>n:
    for i in range(n):
      b.append(a[i].copy())
    a=b.copy()
  else:
    for i in range(m):
      a[i]=a[i][:m]
  return a
def func6(a):#транспонировать
  b = [ [0]*m for i in range(n) ]
  for i in range(m):
      for j in range(n): 
          b[j][i]=a[i][j]
  a = b
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
  print(b)
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
##############
mode = "r+"
try:
  file = open("text_lab2.txt", mode)
except FileNotFoundError:
  print("Ошибка: Файл не найден")
else:
  print("Файл для чтения открыт успешно")
mode = "w"
try:
  file1 = open("output.txt", mode)
except FileNotFoundError:
  print("Ошибка: Файл не найден")
else:
  print("Файл для записи открыт успешно")
###############
  
print(" Считать матрицу из файла - 1, \n Написать свою - 2")
s1=int(input())
while (s1!=0):
  if s1==1 :
    m,n = map(int, file.readline().split())
    matr=[]
    for i in range (m):
      matr.append(list(map(int, file.readline().split()))[:n])
    print("Считано")
    print(matr)
    break
  if s1==2:
    print("Введите количество строк и стобцов через пробел")
    m, n=map(int, input().split())
    print ("Введите матрицу размера n на m.", "\n")
    matr=func1(n,m)
    print("Считано")
    break
print("Введите пункт меню 1 - 22")#МЕНЮ
s=int(input())
while (s!=0):
  if s==1 :
    print("Введите количество строк и стобцов через пробел")
    m, n=map(int, input().split())
    print ("Введите матрицу размера n на m.", "\n")
    matr=func1(n,m)
    func_file_matrix(matr, m, n)
  if s==2 :
    print("Ваша матрица")
    func2(matr)
  if s==3 :
    print("Минимальный элемент")
    min_matr=func3(matr)
    print(min_matr)
    func_file_digit(min_matr)
  if s==4 :
    print("Пункт 4")
    max_matr=func4(matr)
    print(max_matr)
    func_file_digit(max_matr)
  if s==5 :
    print("Обрезать по короткой стороне")
    matr_obr=func5(matr)
    func2(matr_obr)
    func_file_matrix(matr_obr, min(n,m), min(n, m))
  if s==6 :
    print("Транспонированная матрица")
    matr_transp=func6(matr)
    func2(matr_transp)
    func_file_matrix(matr_transp, n, m)
  if s==7 :
    print("Заменить элементы на сумму цифр элементов")
    matr_sum_ch=func7(matr)
    func2(matr_sum_ch)
    func_file_matrix(matr_sum_ch, m,n)
  if s==8 :
    print("Дополнить нулями по длинной стороне")
    matr_null=func8(matr)
    func2(matr_null)
    if m>n:
      k2=n+1
      k1=m
    else:
      k2=n
      k1=m+1
    func_file_matrix(matr_null, k1,k2)
  if s==9 :
    print(" Поменять местами столбец x и y. \n Введите х и у.")
    x, y=map(int, input().split())
    matr_stolb = func9(matr, x-1, y-1)
    func2(matr_stolb)
    func_file_matrix(matr_stolb, m,n)
  if s==10 :
    print(" Поменять местами строки x и y. \n Введите х и у. ")
    x, y=map(int, input().split())
    matr_stroka = func10(matr, x-1, y-1)
    func2(matr_stroka)
    func_file_matrix(matr_stroka, m,n)
  if s==11 :
    if m==n:
      print("Ваша матрица квадратная")
    else:
      matr11=func5(matr)
      print("Ваша матрица обрезана по короткой строке")
    print("Сумма элементов главной диагонали")
    sum_g=func11(matr11)
    print(sum_g," \n")
    func_file_digit(sum_g)
  if s==12 :
    if m==n:
      print("Ваша матрица квадратная")
    else:
      matr12=func5(matr)
      print("Ваша матрица обрезана по короткой строке")
    print("Произведение элементов побочной диагонали")
    proizv_p=func12(matr12)
    print(proizv_p," \n")
    func_file_digit(proizv_p)
  if s==13 :
    if m==n:
      print("Ваша матрица квадратная")
    else:
      matr13=func5(matr)
      print("Ваша матрица обрезана по короткой строке")
    print("Глав. диагональ арифм. прогрессия проверка")
    p13=func13(matr13)
    print(p13)
  if s==14 :
    if m==n:
      print("Ваша матрица квадратная")
    else:
      matr14=func5(matr)
      print("Ваша матрица обрезана по короткой строке")
    print("Сумма элементов верхнего треугольника")
    sum_verh_t=func14(matr14)
    print(sum_verh_t)
    func_file_digit(sum_verh_t)
  if s==15 :
    if m==n:
      print("Ваша матрица квадратная")
    else:
      matr15=func5(matr)
      print("Ваша матрица обрезана по короткой строке")
    print("Сумма элементов нижнего треугольника")
    sum_nig_t=func15(matr15)
    print(sum_nig_t)
    func_file_digit(sum_nig_t)
  if s==16 :
    if m==n:
      print("Ваша матрица квадратная")
    else:
      matr16=func5(matr)
      print("Ваша матрица обрезана по короткой строке")
    print("Сумма элементов правого треугольника")
    sum_prav_t=func16(matr16)
    print(sum_prav_t)
    func_file_digit(sum_prav_t)
  if s==17 :
    if m==n:
      print("Ваша матрица квадратная")
    else:
      matr17=func5(matr)
      print("Ваша матрица обрезана по короткой строке")
    print("Сумма элементов левого треугольника")
    sum_lev_t=func17(matr17)
    print(sum_lev_t)
    func_file_digit(sum_lev_t)
  if s==18 :
    if m==n:
      print("Ваша матрица квадратная")
    else:
      matr18=func5(matr)
      print("Ваша матрица обрезана по короткой строке")
    print("Повернуть на 90 градусов по часовой")
    matr18=func18(matr18)
    func2(matr18)
    func_file_matrix(matr18, min(n,m), min(n, m))
  if s==19 :
    if m==n:
      print("Ваша матрица квадратная")
    else:
      matr19=func5(matr)
      print("Ваша матрица обрезана по короткой строке")
    print("Повернуть на 90 градусов против часовой")
    matr19=func19(matr19)
    func2(matr19)
    func_file_matrix(matr19, min(n,m), min(n, m))
  if s==20 :
    if m==n:
      print("Ваша матрица квадратная")
    else:
      matr20=func5(matr)
      print("Ваша матрица обрезана по короткой строке")
    print(" Поменять местами треугольники x и y. \n Введите х и у.")
    x, y=map(int, input().split())
    matr20=func20(matr20, x, y)
    func2(matr20)
    func_file_matrix(matr20, min(n,m), min(n, m))
    

    
  if s==21 :
    if m==n:
      print("Ваша матрица квадратная")
    else:
      matr21=func5(matr)
      print("Ваша матрица обрезана по короткой строке")
    print("массив элементов матрицы в порядке змейки")
    matr21=func21(matr21)
    print(matr21)
    func_file_array(matr21)
  if s==22 :
    if m==n:
      print("Ваша матрица квадратная")
    else:
      matr22=func5(matr)
      print("Ваша матрица обрезана по короткой строке")
    print("массив элементов диагоналей")
    matr22=func22(matr22)
    print(matr22)
    func_file_array(matr22)
  print("Выберите пункт меню: ",  "\n")
  print("Ваш пункт: ")
  s = int(input())


file.close() 
file1.close()



