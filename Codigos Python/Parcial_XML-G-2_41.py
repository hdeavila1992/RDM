import RDM
import Problem2_41


from xml.dom import minidom
import os 
import codecs

def append(root,elemento,append):
    E=root.createElement(elemento)
    append.appendChild(E)

    return E

def ThrWriter(root,filename="index"):
    xml_str = root.toprettyxml(indent ="\t") 
    with codecs.open(filename, "w","utf-8") as f:
        f.write(xml_str)

def preguntar():
    return

def item(root,question,respuesta,porcentaje,retroalimenta):
    c=0
    for i in porcentaje:
        answer=append(root,"answer",question)
        answer.setAttribute("fraction",i)
        text=append(root,"text",answer)
        texto=root.createTextNode(respuesta[c])
        text.appendChild(texto)

        feedback=append(root,"feedback",answer)
        text=append(root,"text",feedback)
        texto=root.createTextNode(retroalimenta[c])
        feedback.appendChild(text)
        text.appendChild(texto)
        c+=1
    shuffleanswers=append(root,"shuffleanswers",question)
    texto=root.createTextNode("1")
    shuffleanswers.appendChild(texto)
    single=append(root,"single",question)
    texto=root.createTextNode("true")
    single.appendChild(texto)
    answernumbering=append(root,"answernumbering",question)
    texto=root.createTextNode("abc")
    answernumbering.appendChild(texto)

def CrearElemento(root,Nombre_elemento,elemento_contenedor,texto_contenido):
    name=append(root,Nombre_elemento,elemento_contenedor)
    text=append(root,"text",name)
    texto=root.createTextNode(texto_contenido)
    text.appendChild(texto)

def pregunta(root,quiz,Nombre,Contenido,respuesta,porcentaje,retroalimenta):
    question=append(root,"question",quiz)
    question.setAttribute("type","multichoice")
    CrearElemento(root,"name",question,Nombre)
    CrearElemento(root,"questiontext",question,Contenido)
    item(root,question,respuesta,porcentaje,retroalimenta)

def multiplicar_lista(lista,numero):
    c=0
    for i in lista:
        lista[c]=i*numero
        c+=1
    return lista

root=minidom.Document()


quiz=append(root,"quiz",root)

Link_img1="https://i.ibb.co/30q29mD/IMG6.png" 

Ev=[190,200,210,215,220]
Pv=[95,90,100,105,110]

c=0
for i in Ev:
    for j in Pv:
        Nombre="Calculo de reacciones"+str(c+1)
        Contenido=""" Dos varillas cilíndricas, una de acero y la otra de latón, se unen en 
        C y están restringidas por soportes rígidos en A y en E. Para la 
        carga mostrada y sabiendo que Es = """+str(i)+""" GPa y Eb = """+str(j)+""" GPa, determine 
        a) las reacciones en A y en E,
        b) la deflexión del punto C.\n
        <img src=\""""+Link_img1+"""\" alt="" width="449" /> 
 """
        #Solución.
        #
        P2_19=Problem2_41.Solucion(i*(10**9),j*(10**9))

        Ga=P2_19
        print(Ga)
        if c==0:
            save=Ga
        if c>1:
            Bda1=save
        else:
            Bda1=[n*2.0 for n in  Ga]
        
        Bda2=[n*2.1416 for n in  Ga]
        Bda3=[n/(1e-3) for n in  Ga]
        Bda4=[n/(1e9) for n in  Ga]

        respuesta=[" las reacciones en A, en E y el desplazamiento Delta de 'C' es:\n"+
                   str(Ga[0:2])+" Newtons y "+str(Ga[2])+" metros",
                   " las reacciones en A, en E y el desplazamiento Delta de 'C' es:\n"+
                   str(Bda1[0:2])+" Newtons y "+str(Bda1[2])+" metros",
                   " las reacciones en A, en E y el desplazamiento Delta de 'C' es:\n"+
                   str(Bda2[0:2])+" Newtons y "+str(Bda2[2])+" metros",
                   " las reacciones en A, en E y el desplazamiento Delta de 'C' es:\n"+
                   str(Bda3[0:2])+" Newtons y "+str(Bda3[2])+" metros",
                   " las reacciones en A, en E y el desplazamiento Delta de 'C' es:\n"+
                   str(Bda4[0:2])+" Newtons y "+str(Bda4[2])+" metros"]
        print(respuesta)
        porcentaje=["100","0","0","0","0"]
        retroalimenta=["Correcto","Incorrecto","Incorrecto","Incorrecto","Incorrecto"]
        pregunta(root,quiz,Nombre,Contenido,respuesta,porcentaje,retroalimenta)
        c+=1





ThrWriter(root,"Pregunta_7_parcial_P1_2023.xml")
