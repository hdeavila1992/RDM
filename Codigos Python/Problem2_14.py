import RDM
from RDM import np
from RDM import sp
from turtle import *

"""
 El cable BC de 4 mm de diámetro es de un acero con E = 200 GPa. Si se 
sabe que el máximo esfuerzo en el cable no debe exceder 190 MPa y que la 
elongación del cable no debe sobrepasar 6 mm, encuentre la carga máxima 
P que puede aplicarse como se muestra en la figura.
"""

def FlechaVector(Ampl,b,a):
  begin_fill()
  fd(b*Ampl),lt(120),fd(a*Ampl),bk(a*Ampl),rt(240),fd(a*Ampl),bk(a*Ampl),lt(120),bk(b*Ampl)
  end_fill()


def figura():
    color('blue', 'gray')
    Ampl=30
    begin_fill()
    fd(5*Ampl),bk(0.5*Ampl)
    lt(135),fd(0.5*  Ampl),dot(0.2*Ampl)
    lt(90),fd(0.5*Ampl)
    rt(45),fd(3*Ampl)
    rt(45),fd(0.5*Ampl)
    lt(90),fd(0.5*Ampl),bk(0.5*Ampl)
    rt(135),dot(0.2*Ampl)
    end_fill()
    pensize(5),fd(3.5*Ampl)
    lt(90),color("red","red"),pensize(1),fd(1*Ampl)
    FlechaVector(Ampl,0.1,0.2)
    bk(1*Ampl),rt(90),color("blue"),pensize(5),fd(2.5*Ampl)
    color("black"), dot(0.3*Ampl)
    color("blue"),pensize(1),rt(149),fd(7*Ampl)
    done()

#figura()

#Cable BC
BC=RDM.objeto()
BC.add("D",4/1000),BC.add("E",200E9),BC.add("Esf_p",190E6),BC.add("Delt",6/1000)
BC.add("A",RDM.A(BC.pro["D"]))
BC.add("L",np.sqrt(6**2+4**2))
BC.add("Lambda",np.array( [4/BC.pro["L"],6/BC.pro["L"]] )  )

BC.add("Esf_d",BC.pro["E"]*BC.pro["Delt"]/BC.pro["L"]  )
if BC.pro["Esf_d"]>BC.pro["Esf_p"]:
   BC.pro["Esf_p"]=BC.pro["Esf_d"]

BC.pro["P"]=BC.pro["A"]*BC.pro["Esf_p"]

AB=RDM.objeto()
AB.add("P",sp.symbols("P"))

S=3.5*AB.pro["P"]-6*BC.pro["P"]

P=sp.solve(S)

Enunciados=["La carga máxima P que puede aplicarse como se muestra en la figura"]
Respuestas=[P]
RDM.Respuesta(Enunciados,Respuestas)

