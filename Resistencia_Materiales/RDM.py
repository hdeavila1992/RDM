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
#"force": is an indicator that a property is a force. 
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
        """_Es una forma de asignar variables a una propiedad determinada del objeto, el valor de entrada
        tiene que ser un diccionario de modo que para cada key del diccionario existe un valor asignado_

        Args:
            dict (_type_): _Diccionario que contiene las variables a analizar y sus respectivos valores. 
            ## Advertencia: asegurese de utilizar todas las varibales que sonsidere posible al principio del codigo
            si se realiza durante la ehecuación esta función puede borrar las otras variables que se han asignado antes
            con las función add()_
        """
        self.pro=dict
    def add(self,name,propertie,printed=False,unity=None):
        if type(name)==type(np.array([0])):
            c=0
            for i in name:
                self.pro[i]=propertie[c]
                c+=1
        else:
            self.pro[name]=[propertie,unity]
        if (printed==True):
            print("++++++++++++++++++++++")
            print("------------!Información!-------------")
            print("Se agrega la propiedad "+str(propertie)+" "+str(unity))
            print("Al diccionario del objeto 'RDM' con la key: "+name)
    def fill(self,name,unity,printed=False):
        """Esta función agrupa de forma automatica todas las variables que compartan la misma unidad(unity)
        Por ejemplo agrupa todas las fuerzas o todos los momentos que experimenta un cuerpo rígido.

        Args:
            name (_string_): _Nombre de la variable en la que será guardada la sumatoria normalmente como estandas
            se escoge Contorno_f y Contorno_m como nombre de variables para guardar la sumatoria de momento y la 
            sumatoria de fuerzas._
            unity (_string_): _Es la unidad que comparte las diferentes variables dentro del diccionario, puede ser
            fuerza, momento, inercia, velocidad, Área, entre otros.._
            printed (bool, optional): _Herramienta que te permite ver si las asginaciones se realizaron de manera
            correcta. _. Defaults to False.
        """
        if self.pro.get(name) == None:
            self.pro[name]=np.array([])
        hstack=True
        for key in self.pro.keys():
            if len(self.pro[key])>1 and key!=name:
                print("Banderaaa *************")
                print(key)
                print(self.pro[key][1])
                if self.pro[key][1]==unity:
                    if printed==True:
                        print("Se identifica "+str(key)+" como elemento con unidad de "+str(unity))
                    if hstack==True:
                        self.pro[name]=np.hstack((self.pro[name],self.pro[key][0])) 
                        hstack=False
                    else:
                        self.pro[name]=np.vstack((self.pro[name],self.pro[key][0])) 
                    if printed==True:
                        print("Se agrega "+str(self.pro[key][0])+" a "+str(name))
        self.pro[name]=[self.pro[name],unity]
        print("Llenado exitoso")

     
    def delta(self,name="Delt",P="P",L="L",A="A",E="E"):
        """Calcula el desplazamiento en milimetros generado por una fuerza normal en una objeto. 
        Se asume una distribución uniforme del esfuerzo normal. Se asume material isotrópico homogenéo. 

        Args:
            name (str, optional): _description_. Defaults to "Delt".
            P (str, optional): _Valor de la fuerza en Newtons o Libras fuerzas_. Defaults to "P".
            L (str, optional): _Valor de la longitud del objeto que soports la carga axial P_. Defaults to "L".
            A (str, optional): _Área dle objeto que soporta la carga axial "P" con longitud "L"_. Defaults to "A".
            E (str, optional): _Modulo de Rigidez del material_. Defaults to "E".
        """
        try:
            self.pro[name]=(self.pro[P]*self.pro[L])/(self.pro[A]*self.pro[E])
        except:
            print("Falla al cacular el desplazaminto, verifique los valores o intente manualmente")
        else:
            print("Calculo de desplazamiento "+name+" exitoso, su valor es: "+str(self.pro[name]))

    def Esf(self,name="Esf",P="P",A="A",E="E",epsilon="epsilon"):
        """_summary_

        Args:
            name (str, optional): _description_. Defaults to "Esf".
            P (str, optional): _description_. Defaults to "P".
            A (str, optional): _description_. Defaults to "A".
            E (str, optional): _description_. Defaults to "E".
            epsilon (str, optional): _description_. Defaults to "epsilon".
        """
        try:
            self.pro[name]=self.pro[P]/self.pro[A]
        except:
            self.pro[name]=self.pro[E]*self.pro[epsilon]
        else:
            print("Trate de asignar variables como numeros reales o símbolos para calcular el esfuerzo")

    def epsilon(self,name="epsilon",Delt="Delt",L="L",Esf="Esf",E="E"):
        """_summary_

        Args:
            name (str, optional): _description_. Defaults to "epsilon".
            Delt (str, optional): _description_. Defaults to "Delt".
            L (str, optional): _description_. Defaults to "L".
            Esf (str, optional): _description_. Defaults to "Esf".
            E (str, optional): _description_. Defaults to "E".
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
    def solve(self,Obj1,Obj2,Sf="P",Delt="Delt"):
        """_summary_

        Args:
            Obj1 (_type_): _description_
            Obj2 (_type_): _description_
            Sf (str, optional): _description_. Defaults to "P".
            Delt (str, optional): _description_. Defaults to "Delt".
        """
        R=sp.solve([self.pro[Sf],self.pro[Delt]],dict=True)
        Obj1.pro["P"]=R[0][Obj1.pro["P"]]
        Obj2.pro["P"]=R[0][Obj2.pro["P"]]
    def solve1(self,Ecu,Incg):
        """_summary_

        Args:
            Ecu (_type_): _description_
            Incg (_type_): _description_
        """
        R=sp.solve(Ecu,dict=True)
        for i in Incg:
            self.pro[i]=R[0][self.pro[i]]
    def sum(self,Contorno_f="Contorno_f",Contorno_m="Contorno_m",printed=False):
        """_summary_

        Args:
            Contorno_f (str, optional): _description_. Defaults to "Contorno_f".
            Contorno_m (str, optional): _description_. Defaults to "Contorno_m".
            printed (bool, optional): _description_. Defaults to False.
        """
        init=True
        for i in self.pro[Contorno_f][0]:
            if init==True:
                Sf=np.zeros_like(i[0:])
                init=False
            Sf=Sf+i
        #-------------------------------------------------    
        init=True
        for j in self.pro[Contorno_m][0]:
            if init==True:
                try:
                    Sm=np.zeros(len(j))
                except:
                    Sm=self.pro[Contorno_m][0]
                    break
                init=False
            Sm=Sm+j
        self.add("S",[Sf,Sm])
        if printed==True:
            print("+++++++++++++++++++++++++++++++++++++++++++++")
            print("Sistemas de ecuación de fuerza:\n "+str(Sf))
            print("Sistemas de ecuación de momento:\n "+str(Sm))
            print("Agregados al diccionario con la Key: 'S' ")
            print("+++++++++++++++++++++++++++++++++++++++++++++")

    def Unitarian(V,VM):
        """_summary_

        Args:
            V (_type_): _description_
            VM (_type_): _description_

        Returns:
            _type_: _description_
        """
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
    def cross_product(self,distance,force,Resultingmomentum="MR",unity="momentum"):
        if len(distance)==len(force):
            self.pro[Resultingmomentum]=np.array([])
            print("Se realizara el producto cruz")
            hstack=True
            for i, j in zip(distance,force):
                if hstack==True:
                    print(i)
                    print(type(i[0]))
                    print(type(j[0]))
                    print(j)
                    print(np.cross(i,j))
                    self.pro[Resultingmomentum]=np.hstack( (self.pro[Resultingmomentum],np.cross(i,j)) )
            else:
                    self.pro[Resultingmomentum]=np.vstack((self.pro[Resultingmomentum],np.cross(i,j)) )
        else:
            print("Los vectores de distancia y fuerza no son compatibles")
            print(str(len(distance))+" Para distancia")
            print(str(len(force))+ " Para fuerza")
            print("Por favor verifique")
        self.pro[Resultingmomentum]=[self.pro[Resultingmomentum],unity]
        

    def momento(self,Nnodo,S="S",Contorno="Contorno_f"):
        """_summary_

        Args:
            Nnodo (_type_): _description_
            S (str, optional): _description_. Defaults to "S".
            Contorno (str, optional): _description_. Defaults to "Contorno_f".
        """
        def vector_dist(Nnodo,M):
            """_summary_

            Args:
                Nnodo (_type_): _description_
                M (_type_): _description_

            Returns:
                _type_: _description_
            """
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
            """_summary_

            Args:
                V (_type_): _description_

            Returns:
                _type_: _description_
            """
            VC=V**2
            try:
                VM=np.sqrt(VC[:,0]+VC[:,1])
            except:
                VM=np.sqrt(VC[:,0]+VC[:,1]+VC[:,2])
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
        """_summary_
        """
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