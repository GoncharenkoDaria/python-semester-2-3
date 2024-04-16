import random


#задача 0
def vvod (n,mass):
    for _ in range (n):
        mass.append(random.randint(0,10))
    print (mass)
    return (mass)

#задача 1
def less (mass,n):
    k=0
    for _ in range (n):
        if (mass[_]<5):
            k=k+1
            print (mass[_])
    if k==0:
        print ("-1")

#задача 2
def common (mass1, mass2, n1, n2):
    k=0;
    for i in mass1:
        for j in mass2:
            if (i==j):
                mass3.append(i)
                mass1.remove(i)
                mass2.remove(j)
                break
    return(mass3)
  


print("---------------0----------------")
mass=[]
n=int(input())

y=vvod(n, mass)


print("---------------1----------------")

print("elements less than 5:")

less(mass,n)

print("---------------2----------------")
mass1=[]
mass3=[]
mass2=[]
n1=int(input())
n2=int(input())
a1=vvod(n1, mass1);
b1=vvod(n2, mass2);
mass3= common (mass1, mass2, n1, n2)
print (mass3)











