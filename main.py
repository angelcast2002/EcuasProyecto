import math as ma
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
    k = calcularK(664009,667731,4)
    print("El valor de k es: ", k)
    print(calculoPoblacionFinal(664009,k,365))

def calculoPoblacionFinal(Pzero, k, t):
    return Pzero * (ma.e**(k*t))

def calcularK(Pzero, Pfinal, t):
    valorLog = Pfinal/Pzero
    k = ma.log(valorLog, ma.e)/t
    return k

if __name__ == '__main__':
    main()
