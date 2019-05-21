#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lxml import html
import requests
import xml.etree.ElementTree as ET
import random

class principiosActivos():
    def generarPARandom():
        #saco principios activos
        page = requests.get('https://www.vademecum.es/principios-activos-a_1')
        tree = html.fromstring(page.content)
        principiosActivos = tree.xpath('//div[3]/div/ul/li/a')
        longitudPA = len(principiosActivos)

        #meto los principiosactivos q empiezan por A en un array
        arrayPrinAct = []
        for i in range(0, longitudPA):
            prinAct = principiosActivos[i].xpath('text()')[0]
            arrayPrinAct.append(prinAct)
        paRandom = random.randint(0, len(arrayPrinAct)-1)
        return arrayPrinAct[paRandom]