import RDM


"""
Dos varillas cilíndricas, una de acero y la otra de latón, se unen en 
C y están restringidas por soportes rígidos en A y en E. Para la 
carga mostrada y sabiendo que Es = 200 GPa y Eb = 105 GPa, determine 
a) las reacciones en A y en E,
 b) la deflexión del punto C.
"""

#i=200E9
#j=105E9

def Solucion(i,j):
    VA=RDM.objeto()
    VL=RDM.objeto()

    VA.add("E",i)
    VA.add("L",300/1000)
    VA.add("D",40/1000)
    VA.add("A",RDM.A(VA.pro["D"]))
    VA.add("P",60E3)
    VA.add("R",RDM.sp.symbols("Ra"))


    VL.add("E",j)
    VL.add("L",200/1000)
    VL.add("D",30/1000)
    VL.add("A",RDM.A(VL.pro["D"]))
    VL.add("P",40E3)
    VL.add("R",RDM.sp.symbols("Ra"))
    VL.add("R2",RDM.sp.symbols("Re"))

    S=RDM.objeto()

    S.add("Sx",-VA.pro["R"]+VA.pro["P"]+VL.pro["P"]-VL.pro["R2"])
    VA.add("Pi1",0)
    VA.add("Pi2",VA.pro["P"])
    VL.add("Pi3",VA.pro["P"])
    VL.add("Pi4",VA.pro["P"]+VL.pro["P"])

    VA.add("L1",180/1000)
    VA.add("L2",120/1000)
    VL.add("L3",100/1000)
    VL.add("L4",100/1000)



    VA.delta("Delt1","Pi1","L1","A","E")
    VA.delta("Delt2","Pi2","L2","A","E")

    VL.delta("Delt3","Pi3","L3","A","E")
    VL.delta("Delt4","Pi4","L4","A","E")

    VA.delta("Delt1R","R","L","A","E")
    VL.delta("Delt2R","R","L","A","E")

    Delta_L=VA.pro["Delt1"]+VA.pro["Delt2"]+VL.pro["Delt3"]+VL.pro["Delt4"]
    Delta_R=VA.pro["Delt1R"]+VL.pro["Delt2R"]

    S.add("SDelt",Delta_L-Delta_R)

    R=RDM.sp.solve([S.pro["SDelt"],S.pro["Sx"]],dict=True)

    VA.pro["R"]=R[0][VA.pro["R"]]
    VL.pro["R2"]=R[0][VL.pro["R2"]]

    VA.add("Pi2",VA.pro["P"])

    VA.pro["Pi1"]=VA.pro["R"]
    VA.pro["Pi2"]=VA.pro["R"]-VA.pro["P"]

    VA.delta("Delt1","Pi1","L1","A","E")
    VA.delta("Delt2","Pi2","L2","A","E")

    Delt_c=VA.pro["Delt1"]+VA.pro["Delt2"]


    Enunciados=["las reacciones en A"," y en E","la deflexión del punto C"]
    Respuestas=[VA.pro["R"],VL.pro["R2"],Delt_c]
    RDM.Respuesta(Enunciados,Respuestas)
    return Respuestas

#Solucion(i,j)





