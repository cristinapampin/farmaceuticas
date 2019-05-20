#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lxml import html
import requests
import xml.etree.ElementTree as ET
import random
#saco nombres de medicamentos y codigo random
page = requests.get('https://www.vademecum.es/medicamentos-a_1')
tree = html.fromstring(page.content)
nombresMedicamentos = tree.xpath('//div/section/div[3]/div/ul/li/a')

numeroRegistros = len(nombresMedicamentos) #saco longitud de medicamentos

#saco principios activos
pagePA = requests.get('https://www.vademecum.es/principios-activos-a_1')
treePA = html.fromstring(pagePA.content)
principiosActivos = tree.xpath('//div[3]/div/ul/li/a')


#saco laboratorios
pageLA = requests.get('https://www.vademecum.es/laboratorios-a_1')
treeLA = html.fromstring(pageLA.content)
laboratorios = tree.xpath('//div[3]/div/ul/li[4]/a')

#creo elemento medicamento
for i in range(0, numeroRegistros+1):
    NombreMedicamento = nombresMedicamentos[i].xpath('text()')[0]
    codigoMedicamento = str(random.randint(0, 999999999))
    print("MEDICAMENTO: " + NombreMedicamento + "CÓDIGO MEDICAMENTO: " + codigoMedicamento + "\n\n")


for j in range (0, len(principiosActivos)+1):
    principioActMedicamento = principiosActivos[i].xpath('text()')[0]
    genericoMedicamento = random.randint(0, 2)
    if genericoMedicamento == 0:
        genericoMedicamento = "True"
    else:
        genericoMedicamento = "False"