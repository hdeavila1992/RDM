import RDM

"""
La varilla BD está hecha de acero (E = 29X10^6psi) y se utiliza para reforzar 
al elemento axialmente comprimido ABC. La máxima fuerza que puede desarrollarse en el elemento BD es de 0.02P.
Si el esfuerzo no debe exceder 18ksi y el máximo cambio en longitud de BD no debe sobrepasar 0.001 veces 
la longitud de ABC, determine el diámetro mínimo que puede utilizarse para 
la varilla del elemento BD.
"""

def Solucion(i,j):
    BD=RDM.objeto()
    BD.add("E",i),BD.add("P",0.02*(130E3)),BD.add("Esf_p",j) #BD.add("Esf_p",18E3)
    BD.add("Delt",0.001*(72+72)), BD.add("L",54)
    #Esf_p=E*epsilon

    #Para esfuerzo permisible
    BD.add("A",BD.pro["P"]/BD.pro["Esf_p"])
    print(BD.pro["A"])
    BD.add("D",RDM.D(BD.pro["A"]))
    #Para deformación permisible.
    BD.add("Esf",BD.pro["E"]*BD.pro["Delt"]/BD.pro["L"])
    BD.add("A_d",BD.pro["P"]/BD.pro["Esf"])
    BD.add("D_d",RDM.D(BD.pro["A_d"]))
    #Para fuerza permisible
    BD.add("P_p",0.02*BD.pro["Esf_p"])
    #BD.add("A_p",)

    print(BD.pro["D"])
    print(BD.pro["D_d"])

    Enunciados=["El diámetro mínimo que puede utilizarse para la varilla del elemento BD"]
    Respuestas=[BD.pro["D"]]
    RDM.Respuesta(Enunciados,Respuestas)
    return Respuestas