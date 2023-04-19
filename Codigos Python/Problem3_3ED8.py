import RDM

"""

 Se aplica un par de torsión de 1.75 kN∙m al cilindro sólido que se muestra en la figura.
   Determine (a) el esfuerzo cortante máximo, (b) el porcentaje del par de torsión que 
   soporta el núcleo interno de 25 mm de diámetro.

"""

def solve(i):
    Cilindroh=RDM.objeto()

    Cilindroh.add("T",i)
    Cilindroh.add("d",50e-3)
    Cilindroh.add("d25",25e-3)
    Cilindroh.add("c",Cilindroh.pro["d"]/2)
    Cilindroh.add("c25",Cilindroh.pro["d25"]/2)
    Cilindroh.tau(c="c")
    Cilindroh.tau(tau="tau25",c="c25")
    Cilindroh.add("por",100*Cilindroh.pro["tau25"]/Cilindroh.pro["tau"])
    Answ1=["El esfuerzo  cortante  máximo es: ", Cilindroh.pro["tau"]]
    Answ2=["El porcentaje del par de torsión es: ", Cilindroh.pro["por"]]
    Answ=Answ1+Answ2
    return Answ


r=solve(1.75e3)
print(r)
