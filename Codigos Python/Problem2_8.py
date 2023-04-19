import RDM

"""
Un tubo de hierro fundido se usa para soportar una carga de compresión. Si 
se sabe que E = 10 X 10^6psi y que el cambio permisible máximo en longitud 
es de 0.025%, determine a) el esfuerzo normal máximo en la tubería, b) el 
grosor de pared mínimo para una carga de 1 600 lb si el diámetro exterior 
del tubo es de 2.0 in.
"""

TH=RDM.objeto()

TH.add("E",10E6), TH.add("epsilon",0.025/100), TH.add("P",1600), TH.add("D_e",2)
TH.add("Esf_p",TH.pro["E"]*TH.pro["epsilon"])
#Esp_p=P/A--> A=P/Esf_p
TH.add("A_min",TH.pro["P"]/TH.pro["Esf_p"])
TH.add("A_e",RDM.A(TH.pro["D_e"]))
#A_e-A_i=A_min--> A_e-A_min=A_i
TH.add("A_i",TH.pro["A_e"]-TH.pro["A_min"])
TH.add("D_i",RDM.D(TH.pro["A_i"]))
TH.add("t",(TH.pro["D_e"]-TH.pro["D_i"])/2)

Enunciados=["a) el esfuerzo normal máximo en la tubería","b) el grosor de pared mínimo para una carga de 1 600 lb si el diámetro exterior del tubo es de 2.0 in,"]
Respuestas=[TH.pro["Esf_p"],TH.pro["t"]]
RDM.Respuesta(Enunciados,Respuestas)