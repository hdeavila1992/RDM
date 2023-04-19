import RDM

#Aplicación de conceptos 3.1

"""

Un eje cilíndrico hueco de acero mide 1.5m de longitud y tiene diámetro interior y exterior iguales a 40 y 60mm, respectivamente(figura 3.15)
a) Cual es  el máximo par de torsión que puede apllicarse al eje si el esfuerzo cortante no debe exceder 120Mpa
b) ¿Cual es el valor mínimo correspondiente del esfuerzo cortante en el eje?

"""

EJE=RDM.objeto()

EJE.add("L",1.5)
EJE.add("di",40e-3)
EJE.add("de",60e-3)

#Valor maximo de esfuerzo cortante
EJE.add("tau",120e6)

#Como calcular la inercia polar de un objeto circular?
EJE.J("Ji","di")
EJE.J("Je","de")
EJE.add("J",EJE.pro["Je"]-EJE.pro["Ji"])

#Respuesta:
EJE.add("T", (EJE.pro["J"]*EJE.pro["tau"])/(0.5*EJE.pro["de"])  )
EJE.add("tau_min",EJE.pro["tau"]*(EJE.pro["di"]*0.5)/(EJE.pro["de"]*0.5)) 


Respuestas=[EJE.pro["T"],EJE.pro["tau_min"]]
Enunciados=["el máximo par de torsión","l valor mínimo correspondiente del esfuerzo cortante en el eje"]

RDM.Respuesta(Enunciados,Respuestas)







