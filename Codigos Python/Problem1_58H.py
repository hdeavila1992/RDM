import RDM

""""

Las barras AB y BC tienen diámetros de 4 mm y 
6 mm, respectivamente. Si la fuerza de 3 kN se aplica al
anillo en B, determine el ángulo theta tal que el esfuerzo normal promedio en cada barra sea equivalente. ¿Cuál es este 
esfuerzo?

"""
def Solucion(i,j):
  AB=RDM.objeto()
  AB.add("D",i/1000)
  AB.add("P",RDM.sp.symbols("P_AB"))
  AB.add("Landa",RDM.np.array([-1,0]))
  AB.add("A",RDM.A(AB.pro["D"]))
  AB.add("Esf",AB.pro["P"]/AB.pro["A"])

  BC=RDM.objeto()
  BC.add("D",j/1000)
  BC.add("P",RDM.sp.symbols("P_BC"))
  BC.add("Landa",RDM.np.array([4/5,3/5]))
  BC.add("A",RDM.A(BC.pro["D"]))
  BC.add("Esf",BC.pro["P"]/BC.pro["A"])


  B=RDM.objeto()
  B.add("P",3000)
  B.add("theta",RDM.sp.symbols("theta"))
  B.add("Landa",RDM.np.array([-RDM.sp.sin(B.pro["theta"]),-RDM.sp.cos(B.pro["theta"]) ]) )
  B.add("S",AB.pro["Landa"]*AB.pro["P"] + BC.pro["Landa"]*BC.pro["P"]+B.pro["Landa"]*B.pro["P"] )


  Ecuation=RDM.objeto()
  Ecuation.add("Ec1",B.pro["S"])
  Ecuation.add("Ec2",RDM.np.array([AB.pro["Esf"]-BC.pro["Esf"]])  )


  R=RDM.sp.solve([Ecuation.pro["Ec1"][0],Ecuation.pro["Ec1"][1],Ecuation.pro["Ec2"][0] ],dict=True)

  B.pro["theta"]=R[0][B.pro["theta"]]
  AB.pro["P"]=R[0][AB.pro["P"]]
  BC.pro["P"]=R[0][BC.pro["P"]]

  AB.pro["Esf"]=AB.pro["P"]/AB.pro["A"]
  BC.pro["Esf"]=BC.pro["P"]/BC.pro["A"]


  Respuestas=[B.pro["theta"]*180/RDM.np.pi,BC.pro["Esf"]]
  Enunciado=[" el ángulo theta tal que el esfuerzo normal promedio en cada barra sea equivalente",
             "el esfuerzo"]
  RDM.Respuesta(Enunciado,Respuestas)
  return Respuestas


