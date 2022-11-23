import math as ma
import matplotlib.pyplot as plt
# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def main():
    print('''
   #######  #####     #####             #####   ##   ##  ######    #####              ##     ##   ##    ##     ####      ####    #######  #######  ######
    ##   #   ## ##   ##   ##           ##   ##  ##   ##   ##  ##  ##   ##            ####    ###  ##   ####     ##        ##     #   ##    ##   #   ##  ##
    ## #     ##  ##  ##   ##           #        ##   ##   ##  ##  #                 ##  ##   #### ##  ##  ##    ##        ##        ##     ## #     ##  ##
    ####     ##  ##  ##   ##            #####   ##   ##   #####    #####   ######   ##  ##   ## ####  ##  ##    ##        ##       ##      ####     #####
    ## #     ##  ##  ##   ##                ##  ##   ##   ##  ##       ##           ######   ##  ###  ######    ##   #    ##      ##       ## #     ## ##
    ##   #   ## ##   ##   ##           ##   ##  ##   ##   ##  ##  ##   ##           ##  ##   ##   ##  ##  ##    ##  ##    ##     ##    #   ##   #   ##  ##
   #######  #####     #####             #####    #####   ######    #####            ##  ##   ##   ##  ##  ##   #######   ####    #######  #######  #### ### ''')
    
    
    print("Población inicial")
    print("Ingrese 1 si desea ingresar el dato en millones, o 2 si desea ingresar normalmente el dato")
    if int(input()) == 1:
        Pzero = float(input("Ingrese la cantidad de subscriptores inicial en millones: ")) * 1000000
    else:
        print("Ingrese la cantidad de subscriptores inicial: ")
        Pzero = float(input())
    print("Población final")
    print("Ingrese 1 si desea ingresar el dato en millones, o 2 si desea ingresar normalmente el dato")
    if int(input()) == 1:
        Pfinal = float(input("Ingrese la cantidad de subscriptores final en millones: ")) * 1000000
    else :
        print("Ingrese la cantidad de subscriptores final: ")
        Pfinal = float(input())
    print("Ingrese el tiempo en el que se registro este cambio, en días")
    t = int(input())
    
    k = calcularK(Pzero,Pfinal,t)
    print("El valor de k es: ", k)
    
    salir = False
    while (salir == False):
        print("Ingrese: \n1 para calcular la cantidad de subscriptores final \n2 para salir")
        opcion = int(input())
        match opcion:
            case 1:
                print("Ingrese el tiempo en que se quiere estimar la cantidad de subscriptores, en días")
                tiempoAestimar = int(input())
                print("La cantidad de subscriptores estimada en ", tiempoAestimar, " días es: ", round(calculoPoblacionFinal(Pzero, k, tiempoAestimar)))
                graficarCrecimiento(Pzero, k, tiempoAestimar)
            case 2:
                salir = True
        
        
    
    
    

def calculoPoblacionFinal(Pzero, k, t):
    potencia = ma.e**(k*t)
    resultado = Pzero * (potencia)
    return resultado

def calcularK(Pzero, Pfinal, t):
    valorLog = Pfinal/Pzero
    k = ma.log(valorLog, ma.e)/t
    return k

def graficarCrecimiento(Pzero, k, t):
    arrayPfinal = []
    arrayTiempo = []
    for i in range(t + 1):
        arrayPfinal.append(calculoPoblacionFinal(Pzero, k, i))
        arrayTiempo.append(i)
    fig, ax = plt.subplots()
    ax.plot(arrayTiempo, arrayPfinal)
    ax.set(xlabel='Tiempo (días)', ylabel='Población')
    ax.grid(axis = 'both', color = 'black', linestyle = '--', linewidth = 0.5)
    plt.show()

if __name__ == '__main__':
    main()
