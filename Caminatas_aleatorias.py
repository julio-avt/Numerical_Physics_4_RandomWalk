# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 00:09:31 2021

@author: Julio C. Torreblanca
"""

import numpy as np
import matplotlib.pyplot as plt



############################ Inciso (a)
def pasos_normalizados(n: int):
    """Esta función genera dos arreglos cuyos elementos son los n pasos 
    normalizados generados aleatoriamente en el intervalo [-1,1]"""
    
    x = np.random.uniform(-1,1,n) #genera un arreglo independiente con n elementos para los pasos en x
    y = np.random.uniform(-1,1,n) #genera un arreglo independiente con n elementos para los pasos en y
    
    for i in range(n):
        L = np.sqrt( x[i]**2 + y[i]**2 )
        x[i] = x[i]/L
        y[i] = y[i]/L
    
    return x, y


###################################################################

############################ Inciso (b) y (c)
N = 1000 #Número de pasos
K = int(np.sqrt(N)) #Número de experimentos

R_i = 0.0 #Distancia cuarática del i-ésimo experimento
sumaR_i = 0.0 #Suma de todos distancias cadradas


for i in range(K):
    x, y =  pasos_normalizados(N) #Este crea los arreglos de un experimento
    
    #Se obtienen las sumatorias de los pasos en x, y. 
    suma_x = sum(x)
    suma_y = sum(y)
    
    R_i = sum(x)**2 + sum(y)**2 #Se calcula la distancia cuadrada para el experimento
    print(f'Experimento: {i+1:3} ----- R_{i+1:<3} = {R_i:10.8}')
    
    sumaR_i += R_i #Se suman todas las R_i's cuadradas.

R = sumaR_i/K   
print(f'Distancia cuadrática media de los {K} experiemntos ----- R^2 = {R}')
print("\n\n","*"*80, "\n\n")

####################################################################

############# Inciso (d)
N = 1000 #Número de pasos

x, y =  pasos_normalizados(N) #Se crean los arreglos

R = sum(x)**2 + sum(y)**2 #Se calcula la distancia cuadrada 

for _ in range(10): #Haremos 10 cálculos distintos para ver mejor el resultado
    i = np.random.randint(0,len(x)-1) #escogemos a x_i aleatoriamente
    j = np.random.randint(0,len(x)-1) #escogemos a x_j aleatoriamente
    
    if i != j:
        valor = x[i]*x[j]/(R*N*(N-1)) #Calculamos la estimación deseada
        print(f'Tomando x_{i+1:<3} y  x_{j+1:<3} obtenemos: {valor:10.6}')
          
        valor = y[i]*y[j]/(R*N*(N-1)) #Calculamos la estimación deseada
        print(f'Tomando y_{i+1:<3} y  y_{j+1:<3} obtenemos: {valor:10.6}')
        print("-"*80) 
        

####################################################################

########### Inciso (e)

eje_y = [] #Aquí agregaremos los valores para el eje y
eje_x = [] #Aquí agregaremos los valores para el eje x

for i in range(1,1000): #i es el número de pasos
    K = int(np.sqrt(i)) #Número de experimentos
    R_rms = 0.0
    
    for _ in range(0,K):
        x, y =  pasos_normalizados(i) #Este crea los arreglos de un experimento
        
        R_i = sum(x)**2 + sum(y)**2 #Se calcula la distancia cuadrada para el experimento
        R_rms += R_i #suma todos los cuadrados de R_i^2
        
    R_rms = np.sqrt(R_rms/K)
    print(R_rms)
    
    eje_y.append(R_rms)
    eje_x.append(np.sqrt(i))

m = [x for x in range(1,40)]
n = [x for x in range(1,40)]

plt.plot(eje_x, eje_y, "g*")
plt.plot(m,n, "r")
plt.title('$R_{rms}$ vs $\sqrt{N}$')
plt.xlabel('$\sqrt{N}$')
plt.ylabel('$R_{rms}$')
plt.show()