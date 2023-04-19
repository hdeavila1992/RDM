import RDM
import Problem2_17


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

Link_img1="https://i.ibb.co/xL2RP9h/IMG2.png"

Ev=[0.30,0.40,0.50,0.60,0.70]
Pv=[1/8,1/4,1/2,3/8,3/16]


for i in Ev:
    for j in Pv:
        Nombre="Cálculo de desplazamientos"
        Contenido=""" La probeta que se muestra en la figura fue cortada de una hoja de vinilo (E = """+str(i)+"""x10^6psi) con 
        """+str(j)+""" in de espesor y está sometida a una carga de tensión de 350 lb. Determine a) el alargamiento total de la probeta, b) el
        desplazamiento de su porción central BC. \n
        <img src=\""""+Link_img1+"""\" alt="" width="449" />   """
        #Solución.
        #
        P2_19=Problem2_17.Solucion(i*(10**6),j)

        Ga=P2_19[0]
        Ga2=P2_19[1]
        Bda1=Ga*2
        Bda12=Ga2*2
        Bda2=Ga*2.1416
        Bda22=Ga2*2.1416
        Bda3=Ga/(1e-3)
        Bda32=Ga2/(1e-3) 
        Bda4=Ga/(1e9)
        Bda42=Ga2/(1e9) 

        respuesta=[str(Ga)+" y "+str(Ga2),str(Bda1)+" y "+str(Bda12),str(Bda2)+" y "+str(Bda22),str(Bda3)+" y "+str(Bda32),str(Bda4)+" y "+str(Bda42)]
        porcentaje=["100","0","0","0","0"]
        retroalimenta=["Correcto","Incorrecto","Incorrecto","Incorrecto","Incorrecto"]
        pregunta(root,quiz,Nombre,Contenido,respuesta,porcentaje,retroalimenta)





ThrWriter(root,"Pregunta_2_parcial_P1_2023.xml")
