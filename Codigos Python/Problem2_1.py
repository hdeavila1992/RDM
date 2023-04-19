import numpy as np
import pandas as pd
import sympy as sp
#-------------------------
#Prolbem resuleto 2.1.
#-------------------------
#Objeto: Permite guardar las variables del problema, para prevenir la creación constante de nuevas varaiables en el codigo.
class objeto():
    def __init__(self) -> None:
       self.lista={}

    def add(self,name,propertie):
        self.lista[name]=propertie

#Función de calculo de área.
def A(D):
    return (np.pi*(D**2))/4

#------------------------------------
#E: Modulo de Youngs
#PorD: Porcentaje deformación
#fuerza: Fuerza de tensión en Newtons.
#Esf: Esfuerzo que soporta el cable.
#A: Área circular del cable.
#D: Diámetro del hilo
Nailon=objeto()

Nailon.add("E",3.3E9),Nailon.add("PorD",1.1/100), Nailon.add("fuerza",8.5)
Nailon.add("Esf",Nailon.lista["E"]*Nailon.lista["PorD"])
Nailon.add("A",Nailon.lista["fuerza"]/Nailon.lista["Esf"])
Nailon.add("D",np.sqrt(4*Nailon.lista["A"]/np.pi))

print("******************")
print("a) El diámetro del hilo es:")
print(Nailon.lista["D"])
print("---------------------")
print("b) El esfuerzo en el hilo es:")
print(Nailon.lista["Esf"])
print("**********************")






