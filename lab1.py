lst1 = []
print("Выберите пункт меню: ",  "\n")
print("Ваш пункт: ")
s = int(input())
while s!=0:
   if s==1:
      print("Введите число, чтобы добавить в конец списка: ") 
      a = int(input())
      lst1.append(a)
   if s==2:
      print("Введите число, чтобы добавить в начало списка: ") 
      a = int(input())
      lst1.insert (0, a) 
   if s==3:
      print(f"Введите число и индекс от 0 до {len(lst1)+1} для добавления: ") 
      a = int(input())
      i = int(input())
      if i in (0,len(lst1)+1):
         lst1.insert (i,a)
      else:
         print("Несуществующий индекс. Не добавлено.")
   if s==4:
      print("Среднее арифметическое списка:")
      sar=sum(lst1) / len(lst1)
      print(sar)
   if s==5:
      print("Среднее геометрическое списка:")
      sgeo = 1
      for i in range(0, len(lst1)) :
         sgeo = sgeo * lst1[i]
      sgeo2 = sgeo**(1 / len(lst1))
      print (sgeo2)
   if s==6:
      print("Среднее гармоническое списка:")
      sum = 0
      for i in lst1:
         sum += 1 / i  
      srg = len(lst1)/sum
      print(srg)
   if s==7:
      print ('Минимальное число в списке: ')
      min_number = min (lst1) 
      print(min_number)
   if s==8:
      print ('Максимальное число в списке: ')
      max_number = max (lst1) 
      print(max_number)
   if s==9:
      print ('Введите элемент чтобы узнать количество: ')
      u=int(input())
      c=lst1.count(u)
      print(f"Элемент {u} в списке встречается {c} раз.")
   if s==10:
      print ('Количество отрицательных элементов: ')
      neg=0
      for num in lst1:
         if num <= 0:
            neg += 1
      print(neg)
   if s==11:
      print ('Удалить элемент из списка: ')
      a=int(input())
      if a in lst1:
         lst1.remove(a)
      else:
         print("Такого элемента нет.")
   if s==12:
      print ('Удалить все четные элементы из списка: ') 
      lst1 = [x for x in lst1 if x%2!=0]
      print(lst1)
   if s==13:
      print ('Удалить все нечетные элементы из списка: ') 
      lst1 = [x for x in lst1 if x%2==0]
      print(lst1)
   if s==14:
      print ('Удалить все элементы кратные k из списка (введите k): ') 
      k=int(input())
      lst1 = [x for x in lst1 if x%k!=0]
      print(lst1)
   print("Выберите пункт меню: ",  "\n")
   print("Ваш пункт: ")
   s = int(input())
