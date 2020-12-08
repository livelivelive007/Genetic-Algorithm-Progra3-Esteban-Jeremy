import math
from math import pi, sin, cos
import random
from abc import abstractmethod

CANT_ABEJAS = 20
CANT_FLORES = 50
MARGEN_EVOLUCION = 2

#oeste,este,norte,sur
angulos_direcciones = [0, pi*3/4, pi/2, pi/4, pi, -pi/4, -pi/2, -pi*3/4]
largo_angulos_posibles = len(angulos_direcciones)-1

#                  rojo,    naranja         amarillo       verde        celeste        azul         morado        fuchsia
colores_rgb = [(255, 0, 0), (255, 128, 0), (255, 255, 0), (0, 255, 0), (0, 255, 255), (0, 0, 255), (127, 0, 255), (255, 0, 255)]
largo_colores_rgb = len(colores_rgb)-1

"""
Generic Logic

Tipo de recorrido:
    1-) Random.
    2-) ...
    3-) ...
"""
class AbejaIndividuo:    
    def __init__(self, padre=None, madre=None):
        direccion_random_indice = random.randint(0, largo_angulos_posibles)
        direccion_random = angulos_direcciones[direccion_random_indice]
        color_random_indice = random.randint(0, largo_colores_rgb)
        color_random = colores_rgb[color_random_indice]

        if padre == None or madre == None:
            #desviacionMaxima = random.randit(30, 40)
            direccionFavorita = direccion_random
            colorFavorito = color_random
            toleranciaAlColor = random.randint(0,1)
            anguloDesviacion = random.randint(30, 40)
            distanciaMaxima = random.randint(0, 71)
            recorrido_de_flores = []  
            nectar_recolectado = []
            
            #self.desviacionMaxima = desviacionMaxima
            self.direccionFavorita = direccionFavorita
            self.colorFavorito = colorFavorito
            self.toleranciaAlColor = toleranciaAlColor
            self.anguloDesviacion = anguloDesviacion
            self.distanciaMaxima = distanciaMaxima
            self.recorrido = recorrido_de_flores
            self.nectar_recolectado = nectar_recolectado
            
        else:
            return 0
            #reproducir a papá y mamá XD

    @abstractmethod
    def simularRecorrido(self):
        """
        Debe simular el recorrido y devolver la información necesaria 
        para hacer el cálculo de adaptabilidad
        """

    def cruce(self, otraAbeja):
        return 0

class AbejaRandom(AbejaIndividuo):
    def simularRecorrido(self):
        distanciaDesdeElCentro = random()*self.distanciaMaxima
        angulo = random.randint(self.direccionFavorita-self.desviacionMaxima,
                                self.direccionFavorita+self.desviacionMaxima)
        x = 50+sin(angulo)*distanciaDesdeElCentro
        y = 50+cos(angulo)*distanciaDesdeElCentro

class AbejaAnchura(AbejaIndividuo):
    def simularRecorrido(self):
        pass

class AbejaProfundidad(AbejaIndividuo):
    def simularRecorrido(self):
        pass

"""
Garden Logic
"""
class Flor:
    def __init__(self, pRadio, pAngulo, pMuestras):
        self.radio = pRadio
        self.anagulo = pAngulo
        self.muestras = pMuestras

def jardin():
    cacheCalificaciones = {}

    def hayEvolucion(abejas):
        """
        Esta función determina si la generación actual de abejas
        ha mejorado lo suficiente respecto de la generación anterior
        Sacando la calificación promedio de las abejas de esta 
        generación y comparandola con las calificaciones de la 
        generación anterior
        """
        suma = 0
        for abeja in abejas:
            suma += pow(pow(calificacion(abeja.padre)-calificacion(abeja), 2) +
                        pow(calificacion(abeja.madre)-calificacion(abeja), 2), 0.5)
        return suma/CANT_ABEJAS > MARGEN_EVOLUCION

    def calificarAbejas(abejas):
        nonlocal cacheCalificaciones
        suma = 0
        for abeja in abejas:
            suma += calificacion(abeja)
        cacheCalificaciones['total'] = suma
        for abeja in abejas:
            cacheCalificaciones[abeja] = calificacion(abeja)/suma

    def reproducirAbejas(abejas):
        nonlocal cacheCalificaciones
        nuevasAbejas = []
        for _ in range(CANT_ABEJAS):
            abejaPadre = 0
            abajaMadre = 0
            nuevasAbejas.append(Abeja(abejaMadre, abejaPadre))

    abejas = [
        AbejaIndividuo()
        for _ in range(CANT_ABEJAS)
    ]
    flores = [
        Flor()
        for _ in range(CANT_FLORES)
    ]
    while hayEvolucion(abejas):
        for abeja in abejas:
            abeja.simularRecorrido(flores)
        nuevasFlores = [
            flor.reproducir()  # nueva flor si su lista de muestras está vacía
            for flor in flores
        ]
        calificarAbejas(abejas)  # debe conservarse el linaje
        reproducirAbejas(abejas)  # debe conservarse el linaje
        flores = nuevasFlores


"""
Setup
"""
ancho = 100
alto = 100






def convertColorBinarioToInt(pColor):
    return int(pColor, 2)



def float_bin(number, places=3):
    whole, dec = str(number).split(".")
    whole = int(whole)
    dec = int(dec)
    res = bin(whole).lstrip("0b") + "."

    for x in range(places):
        whole, dec = str((decimal_converter(dec)) * 2).split(".")
        dec = int(dec)
        res += whole

    return res

def decimal_converter(num):
    while num > 1:
        num /= 10
    return num

#n = input("Enter your floating point value : \n")
#p = int(input("Enter the number of decimal places of the result : \n"))
#print(float_bin(n, places=p))

def get_float(x, nP): return '{0:.{n}f}'.format(x, n=nP)

def get_bin(x): return format(x, 'b')

def convertColorIntToBinario(pColor: int):
    return get_bin(pColor)

def createColor(pColor1, pColor2):
    binario_1 = []
    binario_2 = []
    binario_hijo = []

    for i in pColor1:
        binario_1.append(convertColorIntToBinario(i))

    for o in pColor2:
        binario_2.append(convertColorIntToBinario(o))

    for u in range(len(binario_1)):
        binario_11 = binario_1[u]
        binario_22 = binario_2[u]
        binario_slice1 = [binario_11[i:i+4] for i in range(0, len(binario_11), 4)]
        binario_slice2 = [binario_22[i:i+4] for i in range(0, len(binario_22), 4)]
        
        binario_hijo.append(binario_slice1[0]+binario_slice2[1])

    return binario_hijo

def createDireccion(direccion_1, direccion_2):
    cantidad_decimales = 4

    dic1 = get_float(direccion_1, cantidad_decimales)
    dic2 = get_float(direccion_2, cantidad_decimales)

    dic11 = float_bin(dic1, cantidad_decimales)
    dic22 = float_bin(dic2, cantidad_decimales)
    
    largo1 = int(len(dic11)/2)
    dic111 = [dic11[i:i+largo1] for i in range(0, len(dic11), largo1)]

    largo2 = int(len(dic22)/2)
    dic222 = [dic22[i:i+largo2] for i in range(0, len(dic22), largo2)]

    return dic111[0]+dic222[1]

def createTolerancia(x, y): 
    tolerancia1 = convertColorIntToBinario(x)
    tolerancia2 = convertColorIntToBinario(y)

    largo1 = int(len(tolerancia1)/2)
    tolerancia11 = [tolerancia1[i:i+largo1] for i in range(0, len(tolerancia1), largo1)]

    largo2 = int(len(tolerancia2)/2)
    tolerancia22 = [tolerancia2[i:i+largo2] for i in range(0, len(tolerancia2), largo2)]

    result = convertColorBinarioToInt(tolerancia11[0]+tolerancia22[1])

    return result


def createAngulo(x, y):
    angulo1 = convertColorIntToBinario(x)
    angulo2 = convertColorIntToBinario(y)

    largo1 = int(len(angulo1)/2)
    angulo11 = [angulo1[i:i+largo1]
                    for i in range(0, len(angulo1), largo1)]

    largo2 = int(len(angulo2)/2)
    angulo22 = [angulo2[i:i+largo2]
                    for i in range(0, len(angulo2), largo2)]


    result = convertColorBinarioToInt(angulo11[0]+angulo22[1])

    return result


def createDistanciaMaxima(x, y):
    distancia1 = convertColorIntToBinario(x)
    distancia2 = convertColorIntToBinario(y)

    largo1 = int(len(distancia1)/2)
    distancia11 = [distancia1[i:i+largo1]
                for i in range(0, len(distancia1), largo1)]

    largo2 = int(len(distancia2)/2)
    distancia22 = [distancia2[i:i+largo2]
                for i in range(0, len(distancia2), largo2)]

    result = convertColorBinarioToInt(distancia11[0]+distancia22[1])

    return result

def prueba1(abeja_1, abeja_2):
    #Entra sin datos...????    
    #abeja_1.distanciaMaxima
    #abeja_2.distanciaMaxima

    binario_hijo = []

    direccion_favorita_hijo = createDireccion(pi*3/4, pi/2)
    binario_hijo.append(direccion_favorita_hijo)

    color_hijo = createColor((255, 128, 200), (100, 150, 125))
    binario_hijo.append(color_hijo)

    tolerancia_hijo = createTolerancia(20, 22)
    binario_hijo.append(tolerancia_hijo)

    angulo_desviacion_hijo = createAngulo(30, 39)
    binario_hijo.append(angulo_desviacion_hijo)

    distanciaMaxima_hijo = createDistanciaMaxima(40, 56)
    binario_hijo.append(distanciaMaxima_hijo)


    return binario_hijo


"""
Prueba1 pasa todos los parametros de padre y madre a binario para hacer el cruce.
Agarra la primera mitad del padre y la segunda mitad de la madre.
"""

abeja1 = AbejaIndividuo()
abeja2 = AbejaIndividuo()

abeja_hijo = prueba1(abeja1, abeja2)

for j in range(len(abeja_hijo)):
    print("binario_hijo[%s]=%s" % (j, abeja_hijo[j]))









"""
Pasar de un binario a entero.
print(int('01010', 2))
"""


""" cromosomas de las abejas:
direccion favorita (norte, noreste, etc)
color favorito (rojo, anaranjado, etc)
0 FF/16 rojo
forma de recorrido (en anchura, aleatorio, en profundidad)
                    0 - FF/3, FF/3 - 2*FF/3, 2*FF/3 - FF
margen máximo de desviación

cromosomas de las flores:
 color
 posicion
"""
