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

#--------------------------------
#AACR: Alamanbre de acero.
#L: Loargo en pulgadas
#D: Diámetro del alambre en pulgadas
#fuerza: Fuerza axial del alambre en libras
#E: Modulo de youngs en psi

AACR=objeto()

AACR.add("L",4.8*12), AACR.add("D",1/4), AACR.add("fuerza",750), AACR.add("E",29E6)
AACR.add("A",A(AACR.pro["D"]))

AACR.add("Delt",(AACR.pro["L"]*AACR.pro["fuerza"])/( AACR.pro["A"]*AACR.pro["E"] )  )
AACR.add("Esf",AACR.pro["fuerza"]/AACR.pro["A"])

print("*******************")
print("a) El alargamiento del alambre es:")
print(AACR.pro["Delt"])
print("b) El esfuerzo normal correspondiente es:")
print(AACR.pro["Esf"])
print("**************************")






