import RDM
import Problem2_16


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

root=minidom.Document()


quiz=append(root,"quiz",root)

Link_img1="https://i.ibb.co/5T4fMX9/IMG1.png"

Ev=[70]#[65,70,73,75,80]
Pv=[105]#[95,100,105,110,115]


for i in Ev:
    for j in Pv:
        Nombre="Calculo de esfuerzo normal promedio"
        Contenido=""" Un tubo de aluminio (E = """+str(i)+"""GPa) con una longitud de 250 mm, un diámetro exterior de 36 mm y un diámetro interior de 28 mm puede cerrarse en 
        ambos extremos por medio de tapas roscadas de hilo sencillo con un paso 
        de 1.5 mm. Con una tapa completamente enroscada, en el interior del tubo 
        se coloca una varilla de latón sólido (E = """+str(j)+"""GPa) de 25 mm de diámetro 
        y después se enrosca la segunda tapa. Como la varilla es ligeramente más 
        larga que el tubo, se observa que la tapa debe forzarse contra la varilla girándola un cuarto de vuelta antes de que pueda estar enroscada por completo. 
        Determine a) el esfuerzo normal promedio en el tubo y en la varilla, b) las 
        deformaciones del tubo y de la varilla """
        #Solución.
        #
        P2_19=Problem2_16.Solucion(i*(10**9),j*(10**9))

        Ga=P2_19[0]
        print(Ga)
        Ga2=P2_19[1]
        print(Ga2)
        Bda1=multiplicar_lista(Ga,2.0)
        Bda12=[n*2.0 for n in Ga2]
        Bda2=[n*2.1416 for n in  Ga]
        Bda22=[n*2.1416 for n in  Ga2]
        Bda3=[n/(1e-3) for n in  Ga]
        Bda32=[n/(1e-3) for n in  Ga2]
        Bda4=[n/(1e9) for n in  Ga]
        Bda42=[n/(1e9) for n in  Ga2]

        respuesta=["El esfuerzo normal promedio para tubo y varilla:"+str(Ga)+" y las deformaciones del tubo y de la varilla"+str(Ga2),
                   "El esfuerzo normal promedio para tubo y varilla:"+str(Bda1)+" y las deformaciones del tubo y de la varilla"+str(Bda12),
                   "El esfuerzo normal promedio para tubo y varilla:"+str(Bda2)+" y las deformaciones del tubo y de la varilla"+str(Bda22),
                   "El esfuerzo normal promedio para tubo y varilla:"+str(Bda3)+" y las deformaciones del tubo y de la varilla"+str(Bda32),
                   "El esfuerzo normal promedio para tubo y varilla:"+str(Bda4)+" y las deformaciones del tubo y de la varilla"+str(Bda42)]
        print(respuesta)
        porcentaje=["100","0","0","0","0"]
        retroalimenta=["Correcto","Incorrecto","Incorrecto","Incorrecto","Incorrecto"]
        pregunta(root,quiz,Nombre,Contenido,respuesta,porcentaje,retroalimenta)





ThrWriter(root,"Pregunta_1_parcial_P1_2023.xml")

