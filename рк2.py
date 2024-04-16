
def func1(m,n): #ввод
  a=[]
  for i in range(n):
    a.append(list(map(int, input().split()))[:m])
  return a

def func4(a):#максимальный
  max_matr= max(map(max, a))
  return(max_matr)

def func2_1(a, n1, m1): #снег
  for i in range(0,n1):
    for j in range(0, m1):


      print( a[i][j],sep=" ", end=" ")
    print()
  print()

def func6(a, x, y):#Поменять местами столбец x и y
  for i in range(len(a)):
    b=a[i][x]
    a[i][x]=a[i][y]
    a[i][y]=b
  return a

def func610(a, m,n):#транспонировать
  b = [ [0]*m for i in range(n) ]
  for i in range(m):
      for j in range(n):
          b[j][i]=a[i][j]
  a = b

print("Введите количество строк и стобцов через пробел")
m, n=map(int, input().split())
print ("Введите матрицу размера n на m.", "\n")
matr=func1(n,m)
max1 = func4(matr)
for i in range (m):
  for j in range (n):
    if matr[i][j]==max1:
      i1=i
      j1=j
      break
print(i1, j1)

###############снежинк
'''print("введите n")
n1=int(input())

matr2=[["."]*n1 for i in range(n1)]
print (matr2)
#func2_1(matr2, n1)
st=n1//2
stb=st
for i in range(0, n1):
  matr2[st][i]='*'
  matr2[i][stb] = '*'
  matr2[i][i] = '*'
  matr2[i][n1-i-1] = '*'
func2_1(matr2, n1, n1)'''

'''
print("Введите количество строк и стобцов через пробел")
n, m=map(int, input().split())
matr3=[["."]*m for i in range(n)]
#func2_1(matr3, n, m)
for i in range(0, n):
  for j in range(0, m):
    if (i+j)%2==1:
      matr3[i][j]="*"
func2_1(matr3, n, m)'''
'''
n1=int(input())
matr4=[]
matr4=[[0]*n1 for i in range(n1)]
for i in range(0, n1):
  for y in range(n1-i):
    matr4[i][i+y]=y
for i in range(0, n1):
  for y in range(n1-i):
    matr4[i+y][i ] = y'''



'''
m, n=map(int, input().split())
print ("Введите матрицу размера n на m.", "\n")
matr6=func1(n,m)
print ("Введите x y.", "\n")
x, y=map(int, input().split())
func6(matr6, x, y)
func2_1(matr6, m, n)'''

'''
m, n=map(int, input().split())
print ("Введите матрицу размера n на m.", "\n")
matr10=func1(n,m)
func2_1(matr10, m, n)
'''
