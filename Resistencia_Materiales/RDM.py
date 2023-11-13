"""
# Modulo de Resistencia de materiales.

Permite solucionar multiples problemas de resistencia de materiales.
Tiene el siguiente objeto principal: 
1. Objeto: Permite guardar las variables del problema, para prevenir la creación constante de nuevas varaiables en el codigo.
Tiene las siguientes funciones:
2. A(): Función para calculo de Área basado en Diámetros.
3. D(): Función para calculo de Diámetro basado en Área.
 

"""

import numpy as np
import pandas as pd
import sympy as sp

class objeto():
    

    """
#.pro:  Atributo de propiedades de objeto.

 Alguna de las convenciones son: 

#L: Longitud en metros
#D: Diámetro en metros
#Delt: Desplazamiento del alambre en metros.
#E: Modulo de youngs
#P: Fuerza axial en el alambre.
#Esf: Esfuerzo axialñ del alamabre
#SU: Resistencia última en Pascales.
#epsilon: Deformación unitaria 
#n: Factor de seguridad.
"""
    def __init__(self) -> None:
        """Este el el objeto principal donde están guardadas las funciones 
            .pro (dic): guarda todas las propiedades que tiene el objeto
            "Contorno_f" (numpy array): lista de las condiciones de contorno de fuerzas.
            "Contorno_m" (numpy array): lista de las condiciones de contorno de momento.  
        """
        self.pro={}
        self.pro["Contorno_f"]=np.array([])
        self.pro["Contorno_m"]=np.array([])
    def asignar(self,dict):
        """_Asing a dictionary of variables to the main object _

        Args:
            dict (_dict_): _Dictionary with al the variables used in the example._
        """
        self.pro=dict
    def add(self,name,propertie,printed=False):
        """_Add new variable to the main object _

        Args:
            name (_string_): _Name of the new variable example: Fuerza1, Torq1, stress0 _
            propertie (_float_): _Numerical value of the new variable_
            printed (bool, optional): _Determine if you want to print (True) or not (False) the information about the main object_. Defaults to False.
        """
        if type(name)==type(np.array([0])):
            c=0
            for i in name:
                self.pro[i]=propertie[c]
                c+=1
        else:
            self.pro[name]=propertie
        if (printed==True):
            print("++++++++++++++++++++++")
            print("------------!Información!-------------")
            print("Se agrega la propiedad "+str(propertie))
            print("Al diccionario del objeto 'RDM' con la key: "+name)
    def delta(self,name="Delt",P="P",L="L",A="A",E="E"):
        """Function that allows me to calculate the displacement in millimeters, caused by a central axial force on an object.

        Args:
            name (str, optional): Name of the contained object who you wish to calculate displacement.. Defaults to "Delt".
            P (str, optional): Axial force on the object surface.  . Defaults to "P".
            L (str, optional): Longitude of the interest object. Defaults to "L".
            A (str, optional): Area of the interest object . Defaults to "A".
            E (str, optional): Young’s module of the interest object material. Defaults to "E".
        """
        try:
            self.pro[name]=(self.pro[P]*self.pro[L])/(self.pro[A]*self.pro[E])
        except:
            print("Falla al cacular el desplazaminto, verifique los valores o intente manualmente")
        else:
            print("Calculo de desplazamiento "+name+" exitoso, su valor es: "+str(self.pro[name]))

    def Esf(self,name="Esf",P="P",A="A",E="E",epsilon="epsilon"):
        """Function that calculate de axial stress of the interest object 

        Args:
            name (str, optional): Name of the dictionary key who save the Stress value.. Defaults to "Esf".
            P (str, optional): Axial force. Defaults to "P".
            A (str, optional): Area of the interest object. Defaults to "A".
            E (str, optional): Young’s module of the interest object material. Defaults to "E".
            epsilon (str, optional): Axial strain of the interest object. Defaults to "epsilon".
        """
        try:
            self.pro[name]=self.pro[P]/self.pro[A]
        except:
            self.pro[name]=self.pro[E]*self.pro[epsilon]
        else:
            print("Trate de asignar variables como numeros reales o símbolos para calcular el esfuerzo")

    def epsilon(self,name="epsilon",Delt="Delt",L="L",Esf="Esf",E="E"):
        """Calculate the strain of a element subject to an eccentric axial load.

        Args:
            name (str, optional): Name of the key that save the strain value. Defaults to "epsilon".
            Delt (str, optional): Displacement of the object of interest.  . Defaults to "Delt".
            L (str, optional): Longitude of the interest object. Defaults to "L".
            Esf (str, optional): Axial stress of the object of interest. Defaults to "Esf".
            E (str, optional): Young’s module of the interest object material. Defaults to "E".
        """
        try:
            self.pro[name]=self.delta(Delt)/self.pro[L]
            quit()
        except:
            self.pro[name]=self.pro[Delt]/self.pro[L]
        else:
            print("Calculo de deformación sin problemas")
        try:
            self.pro[name]=self.pro[Esf]/self.pro[E]
        except:
            print("Calculo de esfuerzo con problemas, verificar manualmente")             
        try:
            self.pro[name]=self.Esf(Esf,P="P",A="A",E=E,epsilon=name)/self.pro[E]
        except:
            print("Calculo automatico de esfuerzo a fallado, verificar manualmente")
        else:
            print("Calculo de esfuerzo automatico sin problemas")
    def sum(self,Contorno_f="Contorno_f",Contorno_m="Contorno_m",print=False):
        Sf=np.array([0,0])
        for i in self.pro[Contorno_f]:
            Sf=Sf+i[1:]
        Sm=np.array([0,0])
        for j in self.pro[Contorno_m]:
            Sm=Sm+j[1:]
        self.add("S",[Sf,Sm])
        if print==True:
            print("+++++++++++++++++++++++++++++++++++++++++++++")
            print("Sistemas de ecuación de fuerza:\n "+str(Sf))
            print("Sistemas de ecuación de momento:\n "+str(Sm))
            print("Agregados al diccionario con la Key: 'S' ")
            print("+++++++++++++++++++++++++++++++++++++++++++++")

    def Unitarian(V,VM):
        Lambda=np.array([])
        c=0
        for i in VM:
            if i!=0:
                if c==0:
                    Lambda=np.array(V[c,:]/i)
                else:
                    Lambda=np.c_[Lambda,V[c,:]/i]
            else: 
            #Lambda=np.append(Lambda,np.array([0,0]),axis=0)
                if c==0:
                    Lambda=np.array([0,0])
                else:
                    Lambda=np.c_[Lambda,np.array([0,0])]
            c+=1
            Lambda=Lambda.transpose()
            return Lambda


    def momento(self,Nnodo,S="S",Contorno="Contorno_f"):
        """
        ## Momento de una fuerza en un nodo
        ### Esta función permite calcular el momento de una fuerza asignando 
        ### un nodo específico que debe estar en el listado de nodos.

        1. Nnodo: Valor del nodo donde se calculara el momento de una fuera.

        2. Por defecto la Key para las ecuaciones de sumatoria de fuerza es "S"
            pero se puede cambiar bajo consideración 

        3. Se recomienda realizar la suma de fuerza en unop de los apoyos
            para eliminar una incognita del sistemas
        """
        def vector_dist(Nnodo,M):
            index=np.where(M[:,0]==Nnodo)
            try:
                A=M[index[0],1:]
                B=M[:,1:]-A
            except:
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print("No se encuentra nodo en listado de índices, asegúrese de que el listado este bien armado o que el nodo sobre el cual quiere calculas la sumatoria de momentos este dentro del listado.")
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                exit()
            return B
        def vector_mag(V):
            VC=V**2
            VM=np.sqrt(VC[:,0]+VC[:,1])
            return VM


        
        Sf,Sm=self.pro[S]
        try:
            M=self.pro["Nodos"]
        except:
            print("Error inesperado ha ocurrido, el valor de los nodos sera asignado a array vacía ")
            M=np.array([])
        V=vector_dist(Nnodo,M)
        VM=vector_mag(V)
        #Lambda=self.Unitarian(V,VM)
        c=0
        Det=0
        Momento=np.array([])
        for i in V:
            try:
                fuerzas=self.pro[Contorno][c,1:]
            except:
                print("La propiedad con la Key 'Contorno_f' no fue encontrada o no existe\n Trate de asignar la Key manualmente en: ")
                print(" 'momento(self,Nnodo,S='S',Contorno='Contorno_f'):'    ")
                break
            Matriz=np.c_[i,fuerzas].transpose()
            Det+=Matriz[0,0]*Matriz[1,1]-Matriz[1,0]*Matriz[0,1]
            #Momento=np.append(Momento,np.linalg.det(   ))
            c+=1
        self.add("Sm",Det)

    def build(self):
        [Sf,Sm]=self.pro["S"]
        R=sp.solve(np.append(Sf,np.array([Sm[0]+Sm[1]+self.pro["Sm"]]) ),dict=True)   
        k1,k2=R[0].keys()
        c=0
        for i in self.pro["Contorno_f"]:
            Nnode=i[0]
            if k1==i[1]:
                self.pro["Contorno_f"][c,1]=R[0][k1]
            if k1==i[2]:
                self.pro["Contorno_f"][c,2]=R[0][k1]
            if k2==i[1]:
                self.pro["Contorno_f"][c,1]=R[0][k2]
            if k2==i[2]:
                self.pro["Contorno_f"][c,2]=R[0][k2]
            c+=1
        #Sm+self.pro["Sm"]





    def Area(self,tipo,D="D",AREA="A",t="t",anch="Anch"):
        if tipo=="c":
            self.pro[AREA]=A(self.pro[D])
            print("Área "+AREA+" asignada como: "+str(self.pro[AREA])+" en "+D)
        else:
            if (tipo=="r"):
                self.pro[AREA]=self.pro[t]*self.pro[anch]
            else:
                print("Calcule el Área manualmente")
    def Info(self):
        lista=self.pro.keys()
        c=0
        print("------Informa de Propiedades-----------")
        for i in lista:
            print(str(c)+")      La propiedad "+i+" tiene los valores: \n"+"       "+str(self.pro[i]))
            c+=1
        print("------  Fin   -------------")
    def distance(self,A,B,L="L"):
        """
        ## Función distancia.
        Esta función permite calcular la distancia desde un puntos existente en el objeto hasta otro:
        A: String que contiene el nombre del primer Vector de tipo numpy array, 
            contiene las coordenadas cartecianas del primer punto.
        B: String que contiene el nombre del segundo Vector de tipo numpy array, contiene las 
            coordenadas cartecianas del segundo punto.
        L: Nombre en string de la variable donde deseas almacenar la longitud del vector.
        """
        V=self.pro[B]-self.pro[A]
        LV=np.linalg.norm(V)
        self.add(L,LV)
        return
    def deformacion(self,L="L",Lp="Lp",epsilon="epsilon"):
        """"
        ## Calculo de deformación unitaria.
        Determina la deformación de un elemento introduciendo como variable de entrada.
        L: string-->Nombre de la longitud inicial. expl{"L","L0","L1",...}
        Lp: string--->Nombre de la longitud final. expl{"Lf","Lp","L2",...}
        epsilon: string---> es el lugar por defecto, donde se guarda la variable calculada.
        """
        try:
            e=(self.pro[Lp]-self.pro[L])/self.pro[L]
        except:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print(self.pro[Lp])
            print(self.pro[L])
            print(self.pro[L])
            print("Se han presentando problemas  con las longitudes, porfavor verifica typo")
            print("Las variables introducidas son: \n"+L+"\n"+Lp+"\n"+epsilon)
            return
        self.add(epsilon,e)
        return
    def J(self,Jindex="J",d="d"):
        """
        ##Esta función permite cálcular la inercia polar de un elemento circular masiso
        Como parametro de entrada tiene el diametro de la sección circular, su valor por defecto
        es "d" pero puede ser modificado:
        Entradas:
        * Jindex="J" : Variable que almacena la inercia polar.
        * d="d": Diametro esperado del eje.
        """
        J=0.5*np.pi*((self.pro[d]*0.5)**4)
        self.add(Jindex,J)
        return
    def tau(self,tau="tau",T="T",d="d",c="c",J="J"):
        """
        ## El codigo permite calcular el esfuerzo cortante Tau conociendo el diametro de la figura,
        el torque y el lugar donde se quiere medir.

        * tau: Variable que almacena el esfuerzo cortante, su nombre por defecto es "tau"
        * T: Torque de entrada del eje, su nombre por defecto es "T"
        * d: Dinametro del eje, su nombre por defecto es "d"
        * c: Radio de interes para el analisis de esfuerzo cortante.
        * J: Momento polar de inercia de un circulo, su valor por defecto es "J"
        """
        Tor=self.pro[T]
        c=self.pro[c]
        self.J(J,d)
        self.add(tau,Tor*c/self.pro[J])

            

#Función de calculo de área.
def A(D):
    """Function that calculates the transversal area of a cylindrical object.

    Args:
        D (_float_): Diameter of the circle. 

    Returns:
        _float_: area  
    """
    return (np.pi*(D**2))/4
#Función de diámetro de circulo
def D(A):
    return sp.sqrt(4*A/np.pi)

#Constructor de resultados:
def Respuesta(Enunciados,Respuestas):
    c=0
    print("*********************")
    for i in Enunciados:
        print(i+" es:")
        print(Respuestas[c])
        c+=1
    print("*********************") 