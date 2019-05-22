import xml.etree.ElementTree as ET
import generadoresRandom

#me traigo los nb de almacenes random y las direcciones
nombreAlmacenLoco = generadoresRandom.AlmacenLoco.generarNombreAlmacen()
direccionAlmacenLoco = generadoresRandom.DireccionCrazy.generarDireccionCrazy()

print(nombreAlmacenLoco)
print(direccionAlmacenLoco)
numeroAlmacenes = 5

registroAlmacenes = ET.Element("root")

for i in range(numeroAlmacenes):
    almacen = ET.SubElement(registroAlmacenes, "almacen")

    nbAlmacenXML = ET.SubElement(almacen, "nombreAlmacen")
    nbAlmacenXML.text = nombreAlmacenLoco

    lugarAlmacenXML = ET.SubElement(almacen, "ubicacionAlmacen")
    lugarAlmacenXML.text = direccionAlmacenLoco


#saco el xml
tree = ET.ElementTree(registroAlmacenes)
tree.write("almacenes.xml")
