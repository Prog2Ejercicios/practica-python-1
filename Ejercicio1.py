print("Ingrese los dos numeros")
n1=int(input())
n2=int(input())

print("Ingrese 1= Suma -- 2= Resta -- 3= Multiplicación -- 4= División")
n3=int(input())

if n3==1:
    print("La suma es: " + str(n1+n2))
if n3==2:
    print("La Resta es: " + str(n1-n2))
if n3==3:
    print("La Multiplicacion es: " + str(n1*n2))
if n3==4:
    if n1>n2:
        print("La División es: " + str(n1/n2))
    else:
        print("La División es: " + str(n2/n1))