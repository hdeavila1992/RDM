import RDM

"""
Una sola carga axial de magnitud P = 15 kips se aplica al extremo C de la 
varilla de acero ABC. Si se sabe que E = 30x10^6psi, determine el diámetro 
d de la porción BC para el cual la deflexión del punto C será 0.05 in
"""
def Solucion(i,j):
    ABC=RDM.objeto()
    ABC.add("P",i),ABC.add("RA",ABC.pro["P"]),ABC.add("A1",RDM.A(1.25)),ABC.add("A2",RDM.sp.symbols("A2"))
    ABC.add("L1",4*12),ABC.add("L2",3*12),ABC.add("E",j), ABC.add("Delt",0.05)

    ABC.add("Delt_AB", (ABC.pro["RA"]*ABC.pro["L1"])/(ABC.pro["A1"]*ABC.pro["E"] ) )
    ABC.add("Delt_BC",(ABC.pro["RA"]*ABC.pro["L2"])/(ABC.pro["A2"]*ABC.pro["E"] )  )

    S=ABC.pro["Delt_AB"]+ABC.pro["Delt_BC"]-ABC.pro["Delt"]

    ABC.pro["A2"]=RDM.sp.solve(S)
    ABC.add("D2",RDM.D(ABC.pro["A2"][0]))

    Enunciados=["el diámetro de la porción BC para el cual la deflexión del punto C será 0.05 in"]
    Respuestas=[ABC.pro["D2"]]
    RDM.Respuesta(Enunciados,Respuestas)
    return Respuestas


