#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lxml import html
import requests
import xml.etree.ElementTree as ET
import random
import principiosActivos
import generadoresRandom
import laboratoriosRandom
import sacandoMedicamentos

#creoxmlalmacenes
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


#saco el xmlalmacenes
tree = ET.ElementTree(registroAlmacenes)
tree.write("almacenes.xml")


#ahora vamos con xml medicamentos
page = requests.get('https://www.vademecum.es/medicamentos-a_1')
tree = html.fromstring(page.content)
nombresMedicamentos = tree.xpath('//div/section/div[3]/div/ul/li/a')


root = ET.Element('medicamentos')
#creo elemento medicamento, metiendo sus atributos
for i in range(0, 20):

    medicamentoXML = ET.SubElement(root, 'medicamento')

    nombreXML = ET.SubElement(medicamentoXML, "nombre_medicamento")
    nombreXML.text = sacandoMedicamentos.medicamentoRandom.generarDrogaRandom()

    codigoXML = ET.SubElement(medicamentoXML, "codigo_medicamento")
    codigoXML.text = (str(random.randint(0, 999999999)))

    pactivoXML = ET.SubElement(medicamentoXML, "p_activo_medicamento")
    pactivoXML.text = principiosActivos.principiosActivos.generarPARandom()

    genericoXML = ET.SubElement(medicamentoXML, "es_generico_medicamento")
    genericoXML.text = generadoresRandom.Generico.generarRandom()

    laboratorioXML = ET.SubElement(medicamentoXML, "laboratorio_medicamento")
    laboratorioXML.text = laboratoriosRandom.laboratoriosRandom.generarLABRandom()

    prospectoXML = ET.SubElement(medicamentoXML, "prospecto_medicamento")
    prospectoXML.text = generadoresRandom.Prospecto.generarProspecto()


tree = ET.ElementTree(root)
tree.write('medicamentos.xml')
print("Se han creado los siguientes xml:\n\talmacenes.xml\n\tmedicamentos.xml")
