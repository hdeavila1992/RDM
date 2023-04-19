import RDM

"""

Para  el  eje  cilíndrico  hueco  que  se  muestra  en  la  figura,  
determine  el esfuerzo  cortante  máximo  causado  por  un  par  de  torsión 
de  magnitud  T = 800 N∙m

"""
JOSE=RDM.objeto()
JOSE.Area(25.4)
JOSE.Info()
#JOSE.deformacion(20,25)

def solve(i):
    Cilindroh=RDM.objeto()

    Cilindroh.add("T",i)
    Cilindroh.add("c",18e-3)
    Cilindroh.add("d",18e-3*2)
    Cilindroh.tau()

    Answ=["el esfuerzo  cortante  máximo es: ", Cilindroh.pro["tau"]]
    return Answ


i=800
r=solve(i)

print(r)
