import random
import numpy as np
from matplotlib import pyplot as plt

def distribucion_normal(num_obstaculos=12):
    '''
    Función que define el numero de veces que la cánica va a tener que decidir si irse de un lado o de otro
    '''
    prob = 0.50
    posicion = np.empty(num_obstaculos)
    posicion[0]= 6
    pos_counter = 6
    for i in range(1,num_obstaculos):
        test = random.random()
        if test >= prob:
            pos_counter += 1
        else:
            pos_counter -=1
        posicion[i] = pos_counter    
    return pos_counter

def graficar_canicas(num_canicas, num_obstaculos):
    '''
    Función que grafica los resultados de las canicas utilizadas en el experimenta
    '''
    canicas = []
    for i in range(num_canicas):
        i = distribucion_normal(num_obstaculos)
        canicas.append(i)
    plt.hist(canicas)
    plt.xlabel('Distribución de Canicas')
    plt.ylabel('Número de Canicas')
    plt.title('Simulación de la Máquina de Galton')
    plt.show()

graficar_canicas(3000,12)


