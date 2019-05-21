#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lxml import html
import requests
import xml.etree.ElementTree as ET

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

class Vademecum(object):
    def sacarMedicamento(self):
        page = requests.get('https://www.vademecum.es/medicamentos-a_1')
        tree = html.fromstring(page.content)
        nombresMedicamentos = tree.xpath('//div/section/div[3]/div/ul/li/a')


