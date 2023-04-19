import RDM

"""
Para la armadura de acero (E = 200 GPa) y las cargas mostradas en la figura, determine las 
deformaciones de los elementos AB y AD, si se sabe que sus 
áreas de sección transversal respectivas son de 2 400 mm2 y 1 800 mm2
"""

ARM=RDM.objeto()#Armadura.

ARM.add("L1",4),ARM.add("L2",2.5),ARM.add("P",228E3)
ARM.add("Suport1","Fix"),ARM.add("Suport2","roll")
ARM.add("A_AB",2400E-6),ARM.add("A_AD",1800E-6)


#Porlema de estructura.
ARM.add("Nodos",RDM.np.array([[1,0,0],[2,4,0],[3,8,0],[4,4,2.5]]) )
ARM.add("Contorno_f",RDM.np.array([[1,0,RDM.sp.symbols("Ay")],
                               [1,0,0],[3,0,RDM.sp.symbols("Cy")],[4,0,-228E3]] ) )
ARM.add("Conectividad",RDM.np.array([ [1,1,2],[2,2,3],[3,3,4],[4,4,1],[5,4,2]  ])  )

ARM.sum()
ARM.momento(1)
ARM.build()#No tiene nada 



#ARM.Info()


#------------------------------------------------

#SUM=RDM.objeto()

#SUM.add("Sf",ARM.pro["P1"]+ARM.pro["P2"]-ARM.pro["P"])
#SUM.add("Sm_A",ARM.pro["P2"][1]*ARM.pro["L1"]*2-ARM.pro["P"]*ARM.pro["L1"])

#R=RDM.sp.solve([SUM.pro["Sf"][1],SUM.pro["Sm_A"]])

#print(R)

#ARM.pro["P1"][1]=R[ARM.pro["P1"][1]]
#ARM.pro["P2"][1]=R[ARM.pro["P2"][1]]

#------------------------------


#ARM.add("epsilon_AB",)

#Enunciados=["las deformaciones de los elementos AB y AD"]
#Respuestas=[]
#RDM.Respuesta(Enunciados,Respuestas)