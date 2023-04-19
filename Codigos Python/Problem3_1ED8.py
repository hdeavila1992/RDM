import RDM

"""
Determine el par de torsión T que causa un esfuerzo cortante máximo de 70 MPa 
en el eje cilíndrico hueco de acero que se muestra en la figura

"""
def solve(i):
    Eje=RDM.objeto()

    Eje.add("r",i)
    Eje.add("d",Eje.pro["r"]*2)
    Eje.add("taup",70e6)
    Eje.add("T",RDM.sp.symbols("T"))
    Eje.J()
    Eje.add("tau",Eje.pro["T"]*Eje.pro["r"]/Eje.pro["J"])

    print(Eje.pro["tau"])

    r=RDM.sp.solve([Eje.pro["taup"]-Eje.pro["tau"]],dict=True)

    print(r[0][Eje.pro["T"]])

    Answ=["El par de torsión T que causa un esfuerzo cortante máximo es:", r[0][Eje.pro["T"]]  ]
    return Answ


r=solve(18e-3)
print(r)
