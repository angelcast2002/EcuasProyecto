import math as ma
import matplotlib.pyplot as plt
import numpy as np
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
    
    
    print('''\n ----------------------------------------------------------------Población inicial----------------------------------------------------------------
    \nIngrese 1 si desea ingresar el dato en millones, o 2 si desea ingresar normalmente el dato''')
    if int(input()) == 1:
        Pzero = float(input("Ingrese la cantidad de subscriptores inicial en millones: ")) * 1000000
    else:
        print("\nIngrese la cantidad de subscriptores inicial: ")
        Pzero = float(input())
    print('''\n ----------------------------------------------------------------Población final----------------------------------------------------------------
    \nIngrese 1 si desea ingresar el dato en millones, o 2 si desea ingresar normalmente el dato''')
    if int(input()) == 1:
        Pfinal = float(input("\nIngrese la cantidad de subscriptores final en millones: ")) * 1000000
    else :
        print("\nIngrese la cantidad de subscriptores final: ")
        Pfinal = float(input())
    print("\nIngrese el tiempo en el que se registro este cambio, en días")
    t = int(input())
    
    k = calcularK(Pzero,Pfinal,t)
    print("\nEl valor de k es: ", k)
    
    salir = False
    while (salir == False):
        print("\nIngrese (1 o 2): \n1. Calcular la cantidad de subscriptores final \n2. Salir")
        opcion = int(input())
        match opcion:
            case 1:
                print("\nIngrese el tiempo en que se quiere estimar la cantidad de subscriptores, en días")
                tiempoAestimar = int(input())
                print("\nLa cantidad de subscriptores estimada en ", tiempoAestimar, " días es: ", round(calculoPoblacionFinal(Pzero, k, tiempoAestimar)))
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
    ax.set_title("Crecimiento de la población")    
    #mostrar la regresión exponencial
    x = np.array(arrayTiempo)
    y = np.array(arrayPfinal)
    z = np.polyfit(x, np.log(y), 1)
    p = np.poly1d(z)
    plt.plot(x, np.exp(p(x)), "r--")

    #mostrar la correlación de los datos
    plt.text(0.5, 0.5, 'Correlación: ' + str(round(np.corrcoef(x, y)[0, 1], 2)), horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)

    #agregar color de fondo
    ax.set_facecolor('xkcd:light grey')

    plt.show()

if __name__ == '__main__':
    main()
