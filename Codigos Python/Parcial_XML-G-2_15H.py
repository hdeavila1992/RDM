import RDM
import Problem2_15H


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

Link_img1="https://i.ibb.co/gwpyPhJ/IMG7.png"

Ev=[0.5,0.55,0.6,0.65,0.70,0.75,0.80,0.85,0.90,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45]#[65,70,73,75,80]
Pv=[1]#[95,100,105,110,115]

c=0
for i in Ev:
    for j in Pv:
        Nombre="Calculo de deformaciones"+str(c+1)
        Contenido=""" Parte de un eslabonamiento de control para un
        avión consiste en un elemento rígido CB y un cable flexible
        AB. Si se aplica una fuerza al extremo B del elemento y se
        hace que éste gire un ángulo Theta = """+str(i)+"""°, determine la deformación unitaria normal en el cable. En un inicio, el cable
        no está estirado. \n
        <img src=\""""+Link_img1+"""\" alt="" width="449" />"""
        #Solución.
        #
        P2_19=Problem2_15H.Solucion(i,j)

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
        
        respuesta=[" la deformación unitaria normal en el cable es:"+str(Ga),
                   " la deformación unitaria normal en el cable:"+str(Bda1),
                   " la deformación unitaria normal en el cable:"+str(Bda2),
                   " la deformación unitaria normal en el cable:"+str(Bda3),
                   " la deformación unitaria normal en el cable:"+str(Bda4)]
        print(respuesta)
        porcentaje=["100","0","0","0","0"]
        retroalimenta=["Correcto","Incorrecto","Incorrecto","Incorrecto","Incorrecto"]
        pregunta(root,quiz,Nombre,Contenido,respuesta,porcentaje,retroalimenta)
        c+=1





ThrWriter(root,"Pregunta_6_parcial_P1_2023.xml")
