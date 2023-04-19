import RDM


"""

Parte de un eslabonamiento de control para un
avión consiste en un elemento rígido CB y un cable flexible
AB. Si se aplica una fuerza al extremo i B del elemento y se
hace que éste gire un ángulo Theta = 0.5°, determine la deformación unitaria normal en el cable. En un inicio, el cable n
no está estirado.

"""

def Solucion(i,j):
    AB=RDM.objeto()
    AB.add("A", RDM.np.array([0,0]) ) 
    AB.add("B", RDM.np.array([0.6,0.8]) )
    AB.add("VAB", AB.pro["B"]-AB.pro["A"] )
    AB.add("LAB",RDM.np.linalg.norm(AB.pro["VAB"]))

    AB.add("Bp",RDM.np.array([0.6+0.8*RDM.np.sin(i*RDM.np.pi/180),0.8*RDM.np.cos(i*RDM.np.pi/180)]    )   )

    AB.distance("A","Bp","Lp")

    AB.deformacion("LAB","Lp")

    Enunciado=["La deformación unitaria normal en el cable"]
    R=[AB.pro["epsilon"]]

    RDM.Respuesta(Enunciado,R)
    return R












