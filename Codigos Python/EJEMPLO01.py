import RDM


Eje=RDM.objeto()

Eje.add("T1",100),Eje.add("T2",200),Eje.add("T3",300)

D=[8,10,12,16,20,25,30,31,38]
T=[2550]#,5,300]

for j in T:
  Eje.add("T",j)
  for i in D:
    Eje.add("d",i/1000)#Diametro
    Eje.add("c",i/2000)#Radio
    Eje.tau("tau1","T","d","c","J")
    if Eje.pro["tau1"] < 250E6:
      print("El diametro es:"+str(Eje.pro["d"])+" Con torque de "+str(Eje.pro["T"]))
      break




