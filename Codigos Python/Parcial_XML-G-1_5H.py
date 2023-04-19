import RDM
import Problem1_5H


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


root=minidom.Document()


quiz=append(root,"quiz",root)

Link_img1="https://i.ibb.co/5nq4hv5/IMG5.png"

Ev=[2,3,4,5,6]
Pv=[3,4,5,6,7]

c=0
for i in Ev:
    for j in Pv:
        Nombre=str(c)+" Determine el esfuerzo normal promedio"
        Contenido=""" Las barras AB y BC tienen diámetros de """+str(i)+""" mm y 
        """+str(j)+""" mm, respectivamente. Si la fuerza de 3 kN se aplica al
        anillo en B, determine el ángulo Theta tal que el esfuerzo normal promedio en cada barra sea equivalente. ¿Cuál es este 
        esfuerzo? \n
        <img src=\""""+Link_img1+"""\" alt="" width="449" />   """
        #Solución.
        #
        P2_19=Problem1_5H.Solucion(i,j)

        Ga=P2_19[0]
        Bda1=Ga*2
        Bda2=Ga*2.1416
        Bda3=Ga/(1e-3)
        Bda4=Ga/(1e9)

        Ga2=P2_19[1]
        Bda12=Ga2*2
        Bda22=Ga*2.1416
        Bda32=Ga/(1e-3)
        Bda42=Ga/(1e9)

        respuesta=[str(Ga)+" grados y "+str(Ga2)+"Pa",
                   str(Bda1)+" grados y "+str(Bda12)+"Pa",
                   str(Bda2)+" grados y "+str(Bda22)+"Pa",
                   str(Bda3)+" grados y  "+str(Bda32)+"Pa",
                   str(Bda4)+" grados y "+str(Bda42)+"Pa"]
        porcentaje=["100","0","0","0","0"]
        retroalimenta=["Correcto","Incorrecto","Incorrecto","Incorrecto","Incorrecto"]
        pregunta(root,quiz,Nombre,Contenido,respuesta,porcentaje,retroalimenta)
        c+=1





ThrWriter(root,"Pregunta_1S_parcial_P1_2023.xml")