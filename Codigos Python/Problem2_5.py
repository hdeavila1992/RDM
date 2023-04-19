import RDM

"""
Un tubo de aluminio no debe estirarse más de 0.05 in cuando se le aplique 
una carga de tensión. Si se sabe que E = 10.1x10^6 psi y que el esfuerzo 
normal permisible máximo es de 14 ksi, determine a) la longitud permisible 
máxima del tubo, b) el área requerida para el tubo si la carga de tensión es 
de 127.5 kips.
"""

TA=RDM.objeto()

TA.add("Delt",0.05), TA.add("E",10.1E6), TA.add("Esf_p", 14E3), TA.add("P",127.5E3)
#l=E*Delta/Esf_p
TA.add("L",TA.pro["E"]*TA.pro["Delt"]/TA.pro["Esf_p"])
#Esf=P/A--> A=P/Esf_p
TA.add("A",TA.pro["P"]/TA.pro["Esf_p"])

Enunciados=["a) la longitud permisible máxima del tubo","b) el área requerida para el tubo si la carga de tensión es de 127.5 kips,"]
Respuestas=[TA.pro["L"],TA.pro["A"]]
RDM.Respuesta(Enunciados,Respuestas)