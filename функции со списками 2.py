#задача 3
def pasc_triangle (n):
    r=[1]
    for _ in range(n):
        print (r)
        k=len(r)
        z=[]
        for i in range (k-1):
            z.append(r[i]+r[i+1])
        r=[1]+z+[1]
        
#задача 4
def polyndrome_check (s):
    for i in range (0, int(len(s)/2)):
        if s[i]!=s[len(s)-i-1]:
            return "Not a polyndrome"
            break
    return " a polyndrome"
           
        

    
#задача 5
def time_recount (sec):
    m1=(sec-sec%60)/60
    h1=(m1-m1%60)/60
    d1=(h1-h1%24)/24
    time_mass.append("days: ")
    time_mass.append(int(d1))
    time_mass.append("hours: ")
    time_mass.append(int(h1%24))
    time_mass.append("minutes: ")
    time_mass.append(int(m1%60))
    time_mass.append("seconds: ")
    time_mass.append(sec%60)
    return(time_mass)

    
print("---------------3----------------")
n=int(input())
pasc_triangle(n)

print("---------------4----------------")
s=input()
print(polyndrome_check(s))

print("---------------5----------------")
time_mass=[]
sec=int(input())

time_mass=time_recount(sec)
print(time_mass)























