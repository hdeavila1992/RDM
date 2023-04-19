import numpy as np
import pandas as pd
import sympy as sp
#-------------------------
#Prolbem resuleto 2.2.
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

#----------------------

CD=objeto()
EF=objeto()
GH=objeto()

#L: Longitud de elemento.
#D: Diametro.
#M: Material
#Delt: Desplazamiento
#fuerza: Fuerza axial de la barra.
#DT: Desplazamiento de tuerca.

Materiales={"Acero":29E6, "Aluminio":10.6E6 }
#DESCRIPCIÓN DEL PROBLEMA
CD.add("L",18), CD.add("D",3/4), CD.add("M","Acero"), CD.add("paso",0.1), CD.add("vuelta", 1/4)
EF.add("L",12), EF.add("D",1.5), EF.add("M","Aluminio")
GH.add("L",18), GH.add("D",3/4), GH.add("M","Acero"), GH.add("paso",0.1), GH.add("vuelta", 1/4)
#ESTÁTICA:

fuerza=sp.numer("P_CD")
CD.add("fuerza",fuerza)
EF.add("fuerza",sp.numer("P_EF"))
GH.add("fuerza",fuerza)

S=-CD.lista["fuerza"]+EF.lista["fuerza"]-GH.lista["fuerza"]

#Desplazaminto=P*l/A*E..

CD.add("Delt",CD.lista["fuerza"]*CD.lista["L"]/(A(CD.lista["D"])*Materiales[CD.lista["M"]])   )
EF.add("Delt",EF.lista["fuerza"]*EF.lista["L"]/(A(EF.lista["D"])*Materiales[EF.lista["M"]])   )

Delt_total=CD.lista["Delt"]+EF.lista["Delt"]

DT=CD.lista["vuelta"]*CD.lista["paso"]

Solution=sp.solve([S,Delt_total-DT],[CD.lista["fuerza"],EF.lista["fuerza"]])


print(Delt_total)
print(DT)
print(S)
print(Solution)


CD.lista["fuerza"]=Solution[CD.lista["fuerza"]]
EF.lista["fuerza"]=Solution[EF.lista["fuerza"]]
GH.lista["fuerza"]=Solution[GH.lista["fuerza"]]

print(CD.lista["fuerza"])
print(EF.lista["fuerza"])
print(GH.lista["fuerza"])

print("******************")
print("Final")
print("*******************")

