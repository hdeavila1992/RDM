import RDM 

"""
Un tubo de aluminio (E = 70 GPa) con una longitud de 250 mm, un diámetro exterior de 36 mm y un diámetro interior de 28 mm puede cerrarse en 
ambos extremos por medio de tapas roscadas de hilo sencillo con un paso 
de 1.5 mm. Con una tapa completamente enroscada, en el interior del tubo 
se coloca una varilla de latón sólido (E = 105 GPa) de 25 mm de diámetro 
y después se enrosca la segunda tapa. Como la varilla es ligeramente más 
larga que el tubo, se observa que la tapa debe forzarse contra la varilla girándola un cuarto de vuelta antes de que pueda estar enroscada por completo. 
Determine a) el esfuerzo normal promedio en el tubo y en la varilla, b) las 
deformaciones del tubo y de la varilla
"""
def Solucion(i,j):
    TA=RDM.objeto()
    #TA.add("E",70E9),TA.add("L",250/1000),TA.add("De",36/1000),TA.add("Di",28/1000)
    TA.add("E",i),TA.add("L",250/1000),TA.add("De",36/1000),TA.add("Di",28/1000)
    TA.add("A",RDM.A(TA.pro["De"])-RDM.A(TA.pro["Di"]) )
    TA.add("paso",1.5/1000), TA.add("vuelta",1/4)
    TA.add("P",RDM.sp.symbols("P_TA"))
    #TA.add("Delt",TA.pro["P"]*TA.pro["L"]/(TA.pro["A"]*TA.pro["E"]  )  )
    TA.delta()

    VL=RDM.objeto()
    #VL.add("E",105E9),VL.add("D",25/1000),VL.add("L", TA.pro["L"] + TA.pro["paso"]*TA.pro["vuelta"] )
    VL.add("E",j),VL.add("D",25/1000),VL.add("L", TA.pro["L"] + TA.pro["paso"]*TA.pro["vuelta"] )
    VL.add("A",RDM.A(VL.pro["D"]))
    VL.add("P",RDM.sp.symbols("P_VL"))
    #VL.add("Delt",VL.pro["P"]*VL.pro["L"]/(VL.pro["A"]*VL.pro["E"]  )  )
    VL.delta()


    SUMA=RDM.objeto()
    SUMA.add("S_f",VL.pro["P"]-TA.pro["P"])
    SUMA.add("Delt",VL.pro["Delt"]+TA.pro["Delt"]-TA.pro["paso"]*TA.pro["vuelta"])
    #SUMA.add("Delt")

    R=RDM.sp.solve([SUMA.pro["S_f"],SUMA.pro["Delt"]],dict=True)

    TA.pro["P"]=R[0][TA.pro["P"]]
    VL.pro["P"]=R[0][VL.pro["P"]]

    #Calculo de esfuerzo
    TA.Esf()
    VL.Esf()
    #Calculo de deformaciones
    TA.epsilon()
    VL.epsilon()

    Enunciados=["a) el esfuerzo normal promedio en el tubo y en la varilla","b) las deformaciones del tubo y de la varilla"]
    Respuestas=[[TA.pro["Esf"],VL.pro["Esf"]], [TA.pro["epsilon"],VL.pro["epsilon"] ]  ]
    RDM.Respuesta(Enunciados,Respuestas)
    return Respuestas
