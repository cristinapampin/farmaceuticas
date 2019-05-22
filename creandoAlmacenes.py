import xml.etree.ElementTree as ET
import generadoresRandom

numeroAlmacenes = 5

registroAlmacenes = ET.Element("root")

for i in range(numeroAlmacenes):
    nombreAlmacenLoco = generadoresRandom.AlmacenLoco.generarNombreAlmacen()
    direccionAlmacenLoco = generadoresRandom.DireccionCrazy.generarDireccionCrazy()
    almacen = ET.SubElement(registroAlmacenes, "almacen")

    nbAlmacenXML = ET.SubElement(almacen, "nombreAlmacen")
    nbAlmacenXML.text = nombreAlmacenLoco

    lugarAlmacenXML = ET.SubElement(almacen, "ubicacionAlmacen")
    lugarAlmacenXML.text = direccionAlmacenLoco

    medicamentos_almacen = ET.SubElement(almacen, "medicamentos_almacen")
    medicamentos_almacen.text = "medicamentos en este almacen"

    medicamento1XML = ET.SubElement(medicamentos_almacen, "medicamento")
    medicamento1XML.text = "ABACAVIR/LAMIVUDINA MYLAN Comp. recub. con pelicula 600 mg/300 mg"
    stock_medicamento1XML = ET.SubElement(medicamento1XML, "stock")
    stock_medicamento1XML.text = "12"

    medicamento2XML = ET.SubElement(medicamentos_almacen, "medicamento")
    medicamento2XML.text = "EBASTINA ALPROFARMA Comp. recub. con pelicula 20 mg"
    stock_medicamento2XML = ET.SubElement(medicamento2XML, "stock")
    stock_medicamento2XML.text = "200"

    medicamento3XML = ET.SubElement(medicamentos_almacen, "medicamento")
    medicamento3XML.text = "URAPLEX Comp. recub. con pelicula 20 mg"
    stock_medicamento3XML = ET.SubElement(medicamento3XML, "stock")
    stock_medicamento3XML.text = "101"


#saco el xml
tree = ET.ElementTree(registroAlmacenes)
tree.write("almacenes.xml")
