import RDM

"""
La probeta que se muestra en la figura fue cortada de una hoja de vinilo (E = 0.45x10^6psi) con 
1/4 in de espesor y está sometida a una carga de tensión de 350 lb. Determine a) el alargamiento total de la probeta, b) la 
deformación de su porción central BC
"""

probeta=RDM.objeto()

def Solucion(i,j):
    probeta.add("L",1.6+2+1.6),probeta.add("L1",1.6),probeta.add("L3",1.6),probeta.add("L2",2)
    probeta.add("t",j),probeta.add("A1",1*j),probeta.add("A2",0.4*j),probeta.add("A3",1*j)
    probeta.add("E",i),probeta.add("P",350)
    #Desplazamientos
    probeta.delta(name="Delt1",A="A1",L="L1")
    probeta.delta(name="Delt2",A="A2",L="L2")
    probeta.delta(name="Delt3",A="A3",L="L3")
    #Deformaciones
    probeta.epsilon(name="epsilon1",Delt="Delt1",L="L1")
    probeta.epsilon(name="epsilon2",Delt="Delt2",L="L2")
    probeta.epsilon(name="epsilon3",Delt="Delt3",L="L3")

    probeta.add("Delt_total",probeta.pro["Delt1"]+probeta.pro["Delt2"]+probeta.pro["Delt3"])

    Enunciados=["a) el alargamiento total de la probeta","b) el desplazamiento de su porción central BC"]
    Respuestas=[probeta.pro["Delt_total"],probeta.pro["Delt2"]]
    RDM.Respuesta(Enunciados,Respuestas)
    return Respuestas






