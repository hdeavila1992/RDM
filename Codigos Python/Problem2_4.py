import RDM

"""
Dos marcas de calibración se colocan a una separación exacta de 250 mm 
en una varilla de aluminio, que tiene un diámetro de 12 mm, con E = 73 GPa 
y una resistencia última de 140 MPa. Si se sabe que la distancia entre las 
marcas de calibración es de 250.28 mm después de que se aplica una carga, 
determine a) el esfuerzo en la varilla, b) el factor de seguridad

"""
#Varilla de aluminio.
VA=RDM.objeto()
VA.add("L",250/1000),VA.add("D",12/1000), VA.add("E",73E9), VA.add("SU", 140E6) 
VA.add("Delt",(250.28/1000)-VA.pro["L"])
VA.add("epsilon",VA.pro["Delt"]/VA.pro["L"])
VA.add("Esf",VA.pro["E"]*VA.pro["epsilon"])
VA.add("n",VA.pro["SU"]/VA.pro["Esf"])

Enunciados=["a) el esfuerzo en la varilla", "b) el factor de seguridad"]
Respuestas=[VA.pro["Esf"],VA.pro["n"]]
RDM.Respuesta(Enunciados,Respuestas)






