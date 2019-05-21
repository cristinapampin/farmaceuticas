#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lxml import html
import requests
import xml.etree.ElementTree as ET
import random
import principiosActivos
import generadoresRandom
import laboratoriosRandom
#saco nombres de medicamentos y codigo random
page = requests.get('https://www.vademecum.es/medicamentos-a_1')
tree = html.fromstring(page.content)
nombresMedicamentos = tree.xpath('//div/section/div[3]/div/ul/li/a')

numeroRegistros = len(nombresMedicamentos) #saco longitud de medicamentos


#creo elemento medicamento
for i in range(0, numeroRegistros+1):
    nombreMedicamento = nombresMedicamentos[i].xpath('text()')[0]
    codigoMedicamento = str(random.randint(0, 999999999))
    principioActivoMedicamento = principiosActivos.principiosActivos.generarPARandom()
    genericoMedicamento = generadoresRandom.Generico.generarRandom()
    laboratorioMedicamento = laboratoriosRandom.laboratoriosRandom.generarLABRandom()
    prospectoMedicamento = generadoresRandom.Prospecto.generarProspecto()
    print(nombreMedicamento+codigoMedicamento+principioActivoMedicamento+genericoMedicamento+laboratorioMedicamento+prospectoMedicamento)



