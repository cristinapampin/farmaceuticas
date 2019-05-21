#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lxml import html
import requests
import xml.etree.ElementTree as ET


class Generico(object):
    def generarRandom():
        generarRandom = random.randint(0, 2)
        if generarRandom == 0:
         genericoMedicamento = "True"
        else:
          generarRandom = "False"
        return generarRandom

isGeneric = Generico()
print(isGeneric.generarRandom())