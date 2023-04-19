import RDM

"""
Una barra de control hecha de latón amarillo no debe estirarse más de 3 mm 
cuando la tensión en el alambre sea de 4 kN. Si se sabe que E = 105 GPa y 
que el esfuerzo normal permisible máximo es de 180 MPa, determine a) el 
menor diámetro de varilla que debe usarse, b) la longitud máxima correspondiente de la varilla.
"""

BC=RDM.objeto()

BC.add("Delt",3/1000),BC.add("P",4E3), BC.add("E",105E9), BC.add("Esf_p",180E6)
#Esf_p=E*epsilon-->epsilon=Esf_p/E
BC.add("epsilon",BC.pro["Esf_p"]/BC.pro["E"])
#epsilon=Delt/L--> L=Delt/epsilon
BC.add("L",BC.pro["Delt"]/BC.pro["epsilon"])
BC.add("A",BC.pro["P"]/BC.pro["Esf_p"])
BC.add("D",RDM.D(BC.pro["A"]))

Enunciados=["a) el menor diámetro de varilla que debe usarse", "b) la longitud máxima correspondiente de la varilla" ]
Respuestas=[BC.pro["D"],BC.pro["L"]]
RDM.Respuesta(Enunciados,Respuestas)