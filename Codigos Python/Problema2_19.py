import RDM

"""
Las dos porciones de la varilla ABC están hechas de un aluminio para el que 
E = 70 GPa. Si se sabe que la magnitud de P es de 4 kN, encuentre a) el 
valor de Q para que la deflexión en A sea cero, b) la deflexión correspondiente de B

"""


def Solucion(i,j):
    #Var={"E":70E9,"P1":4E3,"L1":0.4,"L2":0.5,"D1":20/1000,"D2":60/1000,"P2":RDM.sp.symbols("Q")}
    Var={"E":i,"P1":j,"L1":0.4,"L2":0.5,"D1":20/1000,"D2":60/1000,"P2":RDM.sp.symbols("Q")}
    ABC=RDM.objeto()
    ABC.asignar(Var)
    ABC.Area("c",D="D1",AREA="A1")
    ABC.Area("c",D="D2",AREA="A2")

    ABC.add("Pr",ABC.pro["P1"]-ABC.pro["P2"])
    ABC.delta("Delt1","P1","L1","A1")
    ABC.delta("Delt2","Pr","L2","A2")


    SUMA=RDM.objeto()
    SUMA.add("Delt_total",ABC.pro["Delt1"]+ABC.pro["Delt2"])
    #SUMA.solve()

    R=RDM.sp.solve([SUMA.pro["Delt_total"]],dict=True)
    print(R)

    ABC.pro["P2"]=R[0][ABC.pro["P2"]]
    ABC.pro["Pr"]=ABC.pro["P1"]-ABC.pro["P2"]
    ABC.delta("Delt2","Pr","L2","A2")

    Enunciado=["a) el valor de Q para que la deflexión en A sea cero es", "b) la deflexión correspondiente de B"]
    Respuestas=[ABC.pro["P2"],ABC.pro["Delt2"]]
    RDM.Respuesta(Enunciado,Respuestas)
    return Respuestas


i=70E9
j=4E3

Solucion(i,j)
