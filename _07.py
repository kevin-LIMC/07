capacidad = 10
elementos = [0] * capacidad
Temp = 0

print("Teclea elementos de la pila(termina el programa con -1)")

for i in range (capacidad):
    try:
        
        elementos[i] = float(input("ingresa el valor N" + str(i +1) + ": "))
    
        if elementos[i] == -1:
            print("PROGRAMA FINALIZADO")
            break
        else:
            Temp +=1
        
    except ValueError:
        print("Valor Invalido")
        break
 
if Temp > 0:
    while Temp >= 1:
        Temp -= 1
        print(int(elementos[Temp]), end = " ")
        
else:
    print("Pila Vacia")
