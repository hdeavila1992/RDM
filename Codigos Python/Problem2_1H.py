import RDM


"""
Determine las deformaciones unitarias normales promedio en los dos 
alambres de la figura si el anillo en A se mueve hacia A':
"""

B=RDM.objeto()
C=RDM.objeto()
A=RDM.objeto()
Ap=RDM.objeto()

B.add("pos",RDM.np.array([0,0]))
C.add("pos",RDM.np.array([6,0]))
A.add("pos",RDM.np.array([3,-4]))
Ap.add("pos",RDM.np.array([3-0.01,4+0.02]))

LBA=RDM.np.linalg.norm (A.pro["pos"]-B.pro["pos"])
LCA=RDM.np.linalg.norm (A.pro["pos"]-C.pro["pos"])

LBAp=RDM.np.linalg.norm (Ap.pro["pos"]-B.pro["pos"])
LCAp=RDM.np.linalg.norm (Ap.pro["pos"]-C.pro["pos"])

epsilon_BA=(LBAp-LBA)/LBA
epsilon_CA=(LCAp-LCA)/LCA

Enunciados=["las deformaciones unitarias normales promedio en los dos alambres"]
Respuestas=[[epsilon_BA,epsilon_CA]]
RDM.Respuesta(Enunciados,Respuestas)
