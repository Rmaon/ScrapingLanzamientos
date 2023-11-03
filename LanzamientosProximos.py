import bs4
import requests
from datetime import datetime, timedelta

def titulosSemanaAAA(urlLanzamientos):
    try:
        resultLanzamiento = requests.get(urlLanzamientos)
        soupLanzamientos = bs4.BeautifulSoup(resultLanzamiento.text, 'html.parser')

        tablasAAA = soupLanzamientos.find_all('table', class_='table transparente tablasinbordes')

        fechaHoy = datetime.now().date()
        fecha_formato_pagina = "%d/%m/%Y"

        datos_serializados = []

        for tabla in tablasAAA:
            fecha_element = tabla.find('div', class_='tcenter w100 t11')
            fecha_text = fecha_element.text
            fecha_formateada = datetime.strptime(fecha_text, fecha_formato_pagina).date()

            fecha_limite = fechaHoy + timedelta(days=7)

            if fechaHoy < fecha_formateada <= fecha_limite:
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

        return datos_serializados

    except Exception as e:
        print("Error al serializar la aplicación:", str(e))
        return []
