
print("Ejercicio 3")
aux= True
aux2= True
lista=[]
listaFeos=[1]
i=2

while aux ==True and aux2== True:
    n= int (input())
    if n>=1 and n<=1500:
        lista.append(n)
    elif n==0:
        aux=False
    else:
        aux2= False
if aux2== True:
    while len(listaFeos)< max(lista):
        ey=2
        feo=False
        cont=0
        while ey<=i:
            if i%2==0 or i%3==0 or i%5==0:
                feo=True
            if ey!= 2 and ey!= 3 and ey!= 5:
                p=1
                contprimo=0
                while p <= ey:
                    if ey % p == 0:
                        contprimo=contprimo + 1
                    p=p+1
                if contprimo <=2:
                    if i%ey==0:
                        feo=False
            if feo == False:
                cont=cont+1
            ey=ey+1
               
        if feo==True and cont==0:
            listaFeos.append(i)
        i+=1
    print()
    for j in range(0,len(lista)):
        print(listaFeos[lista[j]-1])
    
        




