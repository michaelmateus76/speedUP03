## Universidad Sergio Arboleda
## Materia: Computacion Paralela
## Profesor: John Corredor
## Ingenieria de sistemas y telecomunicaciones
## Autor: Michael Steven Pinilla Mateus

import functionE
import Cy_functionE
import numpy as np
import time

### Inicializar variebles
D = 5
N = 1500
X = np.array([np.random.rand(N) for d in range(D)]).T
beta = np.random.rand(N)
theta = 10


### Tiempos
inicio = time.time()
result = functionE.rbf_network(X, beta, theta)
tiempoPy = time.time() - inicio
#print(result)

inicio = time.time()
result = Cy_functionE.rbf_network(X, beta, theta)
tiempoCy = time.time() - inicio
#print(np.asarray(result))

speedUp = round(tiempoPy/tiempoCy,3)

print("Tiempo Python: {} \n".format(tiempoPy))
print("Tiempo Cython: {} \n".format(tiempoCy))
print("SpeedUp: {} \n".format(speedUp))