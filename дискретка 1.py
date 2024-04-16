A=[0]*7
k=0
p=0
for i1 in range (0, 8, 1):
    for i2 in range (0, 8, 1):
        for i3 in range (0, 8, 1):
            for i4 in range (0, 8, 1):
                for i5 in range (0, 8, 1):
                    for i6 in range (0, 8, 1):
                        for i7 in range (0, 8, 1):
                            A[0]=i1
                            A[1]=i2
                            A[2]=i3
                            A[3]=i4
                            A[4]=i5
                            A[5]=i6
                            A[6]=i7
                           
                            p=0

                        
                            for j1 in range (0,2,1):
                                if A[j1]<A[j1+1]:
                                    p=p+1
                            
                            for j2 in range (3,4,1):
                                if A[j2]<=A[j2+1]:
                                    p=p+1
                            if p==5:
                                k=k+1
print(k)

                                    
                                        
                                

