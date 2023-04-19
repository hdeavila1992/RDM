import RDM

"""
El tubo de latón AB (E = 105 GPa) tiene un área en su sección transversal 
de 140 mm2 y se fija mediante un tapón en A. El tubo está unido en B a una 
placa rígida que a su vez está unida en C a la parte baja de un cilindro de 
aluminio (E = 72 GPa) con un área en su sección transversal de 250 mm2
. 
El cilindro después se suspende de un soporte en D. A fin de cerrar el cilindro
el tapón debe moverse hacia abajo, a través de 1 mm. Determine la 
fuerza P que debe aplicarse al cilindro.
"""

#Desplazamiento total esperado.
Delt_total=1/1000

TL=RDM.objeto()
TL.add("E",105E9),TL.add("A",140E-6),TL.add("L",375/1000)
TL.add("P",RDM.sp.symbols("P_TL"))
TL.delta()

CA=RDM.objeto()
CA.add("E",72E9),CA.add("A",250E-6),CA.add("L",375/1000)
CA.add("P",RDM.sp.symbols("P_CA"))
CA.delta()

SUMA=RDM.objeto()
SUMA.add("P",CA.pro["P"]-TL.pro["P"])
SUMA.add("Delt",CA.pro["Delt"]+TL.pro["Delt"]-Delt_total)

#Solver:

SUMA.solve(CA,TL)

Enunciados=["La fuerza P que debe aplicarse al cilindro"]
Respuestas=[CA.pro["P"]]

RDM.Respuesta(Enunciados,Respuestas)


#Dict1={"E":105E9,"A":140E-6,"L":375/1000,"P":RDM.sp.symbols("P_TL")}
#NewObjt=RDM.objeto()
#NewObjt.asignar(Dict1)
#NewObjt.delta()

#print(Dict1.keys())

#---------------------------------------------------




