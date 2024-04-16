def vvod (n,mass):
    for _ in range (n*n):
            mass.append(0)
    for i in range (n):
        mass[i]=1
    for j in range (n-1):
        mass[n*j-1]=1
    for i in range(1,n):
        mass[n*(n-2)+i]=1
    for j in range (2,n-1):
        mass[n*j+2]=1
    for i in range(1,n-2):
        mass[n*2+i]=1
    mass[n*n-1]=0
    print(mass)
    ''' for i in range (n):
        if (i%2==0) and (i!=n):
            for j in range(i,n):
                mass[i*n+j]=1
                
        for i in range (n):     
        for j in range (n):
                print(mass[i*n+j])
        print("      ")'''
    





mass=[]
n=int(input())
y=vvod(n, mass)
