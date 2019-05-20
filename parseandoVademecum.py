#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lxml import html
import requests
import xml.etree.ElementTree as ET

page = requests.get('https://www.vademecum.es/medicamentos-a_1')
tree = html.fromstring(page.content)


nombresMedicamentos = tree.xpath('//div/section/div[3]/div/ul/li/a')
numeroMedicamentos = len(nombresMedicamentos)

for i in range (numeroMedicamentos):
    medicamento = nombresMedicamentos[i].xpath('text()')[0]
    print (medicamento)
