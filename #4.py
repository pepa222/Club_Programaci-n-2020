print ("Ejercicio 4")
while(True):
    n=int(input())
    regiones=0
    
    if(1<=n <=1000 ):
        regiones=((n**4-6*n**3+23*n**2-18*n)/24)+1
        print (int(regiones))
    
