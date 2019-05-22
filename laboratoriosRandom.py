#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lxml import html
import requests
import xml.etree.ElementTree as ET
import random

class laboratoriosRandom():
    def generarLABRandom():
        #saco laboratorios
        page = requests.get('https://www.vademecum.es/laboratorios-a_1')
        tree = html.fromstring(page.content)
        laboratorios = tree.xpath('//div/ul/li[4]/a')

        longitudLAB = len(laboratorios)

        # meto en array
        arrayLAB = []
        for i in range(1, longitudLAB):
            lab = laboratorios[i].xpath('text()')[0]
            arrayLAB.append(lab)

        generarLABRandom = random.randint(0, len(arrayLAB)-1)
        return arrayLAB[generarLABRandom]





