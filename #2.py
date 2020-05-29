print("Ejercicio 2")
N= (int(input()))
suma=0;
if(N<=abs(10**4)):
    if(N>0):
        for i in range (1,N+1):
            suma=suma+i
        print(suma)
    else:
        for i in range (N,-1):
            suma=suma+i
            i=i-1
        print(suma)
    
