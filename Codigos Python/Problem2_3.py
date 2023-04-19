import numpy as np
import pandas as pd
import sympy as sp
#-------------------------
#Prolbem resuleto 2.1.
#-------------------------
#Objeto: Permite guardar las variables del problema, para prevenir la creación constante de nuevas varaiables en el codigo.
#.pro:  Atributo de propiedades de objeto.
class objeto():
    def __init__(self) -> None:
       self.pro={}

    def add(self,name,propertie):
        self.pro[name]=propertie

#Función de calculo de área.
def A(D):
    return (np.pi*(D**2))/4
#Función de diámetro de circulo
def D(A):
    return sp.sqrt(4*A/np.pi)

#Constructor de resultados:
def Respuesta(Enunciados,Respuestas):
    c=0
    print("*********************")
    for i in Enunciados:
        print(i+" es:")
        print(Respuestas[c])
        c+=1
    print("*********************") 

#-._-------------------
#AACR: Alambre de acero
#L: Longitud en metros
#D: Diámetro en metros
#Delt: Desplazamiento del alambre en metros.
#E: Modulo de youngs
#P: Fuerza axial en el alambre.
#Esf: Esfuerzo axialñ del alamabre

AACR=objeto()

AACR.add("L",18), AACR.add("D",5/1000), AACR.add("Delt",45/1000), AACR.add("E",200E9)
AACR.add("A",A(AACR.pro["D"]) )

AACR.add("P", (AACR.pro["Delt"]*AACR.pro["A"]*AACR.pro["E"])/AACR.pro["L"]   )
AACR.add("Esf",AACR.pro["P"]/AACR.pro["A"])


Enunciados=["a) La magnitud de la fuerza P","b) El esfuerzo normal correspondiente"]
Respuestas=[AACR.pro["P"],AACR.pro["Esf"]]
Respuesta(Enunciados,Respuestas)

    






