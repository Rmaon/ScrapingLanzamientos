import bs4
import requests
import discord
from discord.ext import commands
from datetime import datetime


def titulosDiarios(urlLanzamientos):
    try:
        resultLanzamiento = requests.get(urlLanzamientos)
        soupLanzamientos = bs4.BeautifulSoup(resultLanzamiento.text, 'html.parser')

        tablasAAA = soupLanzamientos.find_all('table', class_='table transparente tablasinbordes')

        tablasIndie = soupLanzamientos.find('table', class_='table table-striped froboto_real')

        fechaHoy = datetime.now().date()
        fecha_formato_pagina = "%d/%m/%Y"

        datos_serializados = []

        for tabla in tablasAAA:
            fecha_element = tabla.find('div', class_='tcenter w100 t11')
            fecha_text = fecha_element.text
            fecha_formateada = datetime.strptime(fecha_text, fecha_formato_pagina).date()

            if fecha_formateada == fechaHoy:
                titulo_element = tabla.find('strong')
                enlace_element = tabla.find('a')

                fecha = fecha_text
                titulo = titulo_element.text
                enlace = enlace_element.get('href')

                datos_serializados.append({
                    "fecha": fecha,
                    "titulo": titulo,
                    "enlace": enlace
                })


            fecha_element = tablasIndie.select('link', itemprop_='applicationCategory', href_='http://schema.org/GameApplication')
            for fecha in fecha_element:
                fecha_text = fecha.text
                fecha_formateada = datetime.strptime(fecha_text, fecha_formato_pagina).date()

                if fecha_formateada == fechaHoy:
                    titulo_element = tabla.find('span', itemprop_='name')
                    fecha = fecha_text
                    titulo = titulo_element.text

                    datos_serializados.append({
                        "fecha": fecha,
                        "titulo": titulo,
                        "enlace": ''
                    })


        return datos_serializados

    except Exception as e:
        print("Error al serializar la aplicación:", str(e))
        return []