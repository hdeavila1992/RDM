import RDM

"""
Una varilla de control hecha de acero con 5.5 ft de longitud no debe estirarse más de 0.04 in cuando se le aplica una carga de tensión de
2 kips. Si se sabe que E = 29 x 10^6psi, determine a) el diámetro mínimo de varilla que 
debería usarse, b) el esfuerzo normal correspondiente causado por la carga.
"""

VC=RDM.objeto()

VC.add("L",5.5*12), VC.add("Delt",0.04), VC.add("P",2E3), VC.add("E",29E6)
#Esf=E*Delt/L=P/A-->A=L*P/E*Delt
VC.add("Esf",VC.pro["E"]*VC.pro["Delt"]/VC.pro["L"])
VC.add("A",(VC.pro["L"]*VC.pro["P"])/(VC.pro["E"]*VC.pro["Delt"]) )
VC.add("D",RDM.D(VC.pro["A"])) 

Enunciados=["a) el diámetro mínimo de varilla que debería usarse","b) el esfuerzo normal correspondiente causado por la carga"]
Respuestas=[VC.pro["D"],VC.pro["Esf"]]

RDM.Respuesta(Enunciados,Respuestas)
