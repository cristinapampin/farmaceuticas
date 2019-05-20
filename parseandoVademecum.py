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

numeroRegistros = len(nombresMedicamentos)
#saco principios activos
pagePA = requests.get('https://www.vademecum.es/principios-activos-a_1')
treePA = html.fromstring(pagePA.content)
principiosActivos = tree.xpath('//div[3]/div/ul/li/a')


#creo elemento medicamento
for i in range (0, numeroRegistros+1:
    NombreMedicamento = nombresMedicamentos[i].xpath('text()')[0]
    codigoMedicamento = random.randint (0,999999999)
    principioActMedicamento = principiosActivos[i].xpath('text()')[0]
    genericoMedicamento = random.randint (0,2)
    if genericoMedicamento == 0:
        genericoMedicamento = "True"
    else:
        genericoMedicamento = "False"

    print(NombreMedicamento(i)+codigoMedicamento(i)+principioActMedicamento(i)+genericoMedicamento(i))
