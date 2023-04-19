import RDM
import Problem2_13


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

Link_img1="https://i.ibb.co/V32ZFnW/IMG4.png"

Ev=[20,30,40,50,60]
Pv=[12,16,20,24,28]


for i in Ev:
    for j in Pv:
        Nombre="Cálculo de diámetro"
        Contenido=""" La varilla BD está hecha de acero (E = """+str(i)+"""X10^6psi) y se utiliza para reforzar 
        al elemento axialmente comprimido ABC. La máxima fuerza que puede desarrollarse en el elemento BD es de 0.02P.
        Si el esfuerzo no debe exceder """+str(j)+"""ksi y el máximo cambio en longitud de BD no debe sobrepasar 0.001 veces 
        la longitud de ABC, determine el diámetro mínimo que puede utilizarse para 
        la varilla del elemento BD. \n
        <img src=\""""+Link_img1+"""\" alt="" width="449" />   """
        #Solución.
        #
        P2_19=Problem2_13.Solucion(i*(10**6),j*(10**3))

        Ga=P2_19[0]
        Bda1=Ga*2
        Bda2=Ga*2.1416
        Bda3=Ga/(1e-3)
        Bda4=Ga/(1e9)

        respuesta=[str(Ga),str(Bda1),str(Bda2),str(Bda3),str(Bda4)]
        porcentaje=["100","0","0","0","0"]
        retroalimenta=["Correcto","Incorrecto","Incorrecto","Incorrecto","Incorrecto"]
        pregunta(root,quiz,Nombre,Contenido,respuesta,porcentaje,retroalimenta)





ThrWriter(root,"Pregunta_3_parcial_P1_2023.xml")
