import RDM


"""
La barra que se muestra en la figura tiene un ancho constante de
35 mm y un espesor de 10 mm. Determine el esfuerzo normal promedio máximo en la barra cuando está sometida a las cargas mostradas.
"""

B=RDM.objeto()
B.add("Pi",RDM.np.array([0,0,0]))
B.add("P",RDM.sp.symbols("P"))
B.add("P1",-12E3)
B.add("P2",-2*9E3)
B.add("P3",2*4E3)
B.add("P4",22E3)
B.add("A",0.035*0.010)

#Corte 1---------------------------------------------
B.add("Sx_c1",B.pro["P1"]+B.pro["P"])
R=RDM.sp.solve([B.pro["Sx_c1"]],dict=True)
print(R)
B.pro["Pi"][0]=R[0][B.pro["P"]]
#---------------------------------------------------
#Corte 2---------------------------------------------
B.add("Sx_c2",B.pro["P1"]+B.pro["P2"]+B.pro["P"])
R=RDM.sp.solve([B.pro["Sx_c2"]],dict=True)
print(R)
B.pro["Pi"][1]=R[0][B.pro["P"]]
#Corte 3---------------------------------------------
B.add("Sx_c3",B.pro["P1"]+B.pro["P2"]+B.pro["P3"]+B.pro["P"])
R=RDM.sp.solve([B.pro["Sx_c3"]],dict=True)
print(R)
B.pro["Pi"][2]=R[0][B.pro["P"]]

#El esfuerzo normal prmedio es:

B.add("Esfi",B.pro["Pi"]/B.pro["A"])

Enunciado=["el esfuerzo normal promedio máximo en la barra"]
Respuestas=[B.pro["Esfi"].max()]
RDM.Respuesta(Enunciado,Respuestas)


