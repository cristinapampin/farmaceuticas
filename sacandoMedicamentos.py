from lxml import html
import requests
import xml.etree.ElementTree as ET
import random

class medicamentoRandom():
    def generarDrogaRandom():
        page = requests.get('https://www.vademecum.es/medicamentos-a_1')
        tree = html.fromstring(page.content)
        nombresMedicamentos = tree.xpath('//div/section/div[3]/div/ul/li/a')
        numeroRegistros = len(nombresMedicamentos) #saco longitud de medicamentos

            # meto en array
        arrayDrogas = []
        for i in range(0, numeroRegistros):
            droga = nombresMedicamentos[i].xpath('text()')[0]
            arrayDrogas.append(droga)

        generarDrogaRandom = random.randint(0, len(arrayDrogas)-1)
        return arrayDrogas[generarDrogaRandom]

