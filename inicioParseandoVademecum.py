#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lxml import html
import requests
import xml.etree.ElementTree as ET
import random
import principiosActivos
import generadoresRandom
import laboratoriosRandom

#saco nombres de medicamentos
page = requests.get('https://www.vademecum.es/medicamentos-a_1')
tree = html.fromstring(page.content)
nombresMedicamentos = tree.xpath('//div/section/div[3]/div/ul/li/a')
numeroRegistros = len(nombresMedicamentos) #saco longitud de medicamentos


#creo elemento medicamento, metiendo sus atributos
for i in range(0, numeroRegistros+1):
    nombreMedicamento = nombresMedicamentos[i].xpath('text()')[0]
    codigoMedicamento = str(random.randint(0, 999999999))
    principioActivoMedicamento = principiosActivos.principiosActivos.generarPARandom()
    genericoMedicamento = generadoresRandom.Generico.generarRandom()
    laboratorioMedicamento = laboratoriosRandom.laboratoriosRandom.generarLABRandom()
    prospectoMedicamento = generadoresRandom.Prospecto.generarProspecto()

# Elemento XML
root = ET.Element('medicamentos')

for i in range(numeroRegistros):

    # creo elemento medicamento
    medicamentoXML = ET.Element(root, 'medicamento')
    #hijos de medicamento
    nombreXML = ET.SubElement(medicamentoXML, "nombre_medicamento")
    nombreXML.text = nombreMedicamento[i]
    codigoXML = ET.SubElement(medicamentoXML, "codigo_medicamento")
    codigoXML.text = codigoMedicamento[i]
    pactivoXML = ET.SubElement(medicamentoXML, "p_activo_medicamento")
    pactivoXML.text = principioActivoMedicamento[i]
    genericoXML = ET.SubElement(medicamentoXML, "es_generico_medicamento")
    genericoXML.text = genericoMedicamento[i]
    laboratorioXML = ET.SubElement(medicamentoXML, "laboratorio_medicamento")
    laboratorioXML.text = laboratorioMedicamento[i]
    prospectoXML = ET.SubElement(medicamentoXML, "prospecto_medicamento")
    prospectoXML.text = prospectoMedicamento[i]


tree = ET.ElementTree(root)
tree.write('medicamentos.xml')