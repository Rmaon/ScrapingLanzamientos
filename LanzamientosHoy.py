import bs4
import requests
import re
from datetime import datetime

def titulosDiariosAAA(urlLanzamientos):
    try:
        # Realizar una solicitud GET a la URL de lanzamientos
        resultLanzamiento = requests.get(urlLanzamientos)

        # Crear un objeto BeautifulSoup para analizar el contenido HTML
        soupLanzamientos = bs4.BeautifulSoup(resultLanzamiento.text, 'html.parser')

        # Encontrar todas las tablas con la clase específica
        tablasAAA = soupLanzamientos.find_all('table', class_='table transparente tablasinbordes')

        # Obtener la fecha actual
        fechaHoy = datetime.now().date()

        # Formato de fecha en la página web
        fecha_formato_pagina = "%d/%m/%Y"

        # Lista para almacenar datos serializados
        datos_serializados = []

        # Iterar a través de las tablas AAA
        for tabla in tablasAAA:
            # Encontrar el elemento de fecha dentro de la tabla
            fecha_element = tabla.find('div', class_='tcenter w100 t11')
            fecha_text = fecha_element.text

            # Convertir el texto de fecha al formato de fecha esperado
            fecha_formateada = datetime.strptime(fecha_text, fecha_formato_pagina).date()

            # Verificar si la fecha formateada coincide con la fecha actual
            if fecha_formateada == fechaHoy:
                # Encontrar los elementos de título y enlace dentro de la tabla
                titulo_element = tabla.find('strong')
                enlace_element = tabla.find('a')

                # Obtener datos y agregarlos a la lista
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
        # Manejar cualquier excepción e imprimir un mensaje de error
        print("Error al serializar la aplicación:", str(e))
        return []

def titulosDiariosIndie(urlLanzamientos):
    try:
        # Realizar una solicitud GET a la URL de lanzamientos
        resultLanzamiento = requests.get(urlLanzamientos)

        # Crear un objeto BeautifulSoup para analizar el contenido HTML
        soupLanzamientos = bs4.BeautifulSoup(resultLanzamiento.text, 'html.parser')

        # Patrón de expresión regular para encontrar fechas en el formato específico
        date_pattern = re.compile(r'\d{1,2}/\d{1,2}/\d{4}')

        # Formato de fecha en la página web
        fecha_formato_pagina = "%d/%m/%Y"
        # Obtener la fecha actual
        fechaHoy = datetime.now().date()

        # Seleccionar todas las tablas con las clases específicas
        tablas = soupLanzamientos.select('table.table.table-striped.froboto_real')
        data_list = []

        # Iterar a través de las tablas
        for tabla in tablas:
            # Encontrar todos los elementos de fecha, nombre y plataforma dentro de la tabla
            fechas = tabla.find_all('td', class_='t08')
            nombres = tabla.find_all('span', itemprop='name')
            plataformas = tabla.find_all('td', {'itemprop': 'operatingSystem gamePlatform'})

            # Iterar sobre los elementos encontrados
            for fecha, nombre, plataforma in zip(fechas, nombres, plataformas):
                # Obtener el texto de fecha y quitar espacios en blanco
                fechaStrip = fecha.get_text(strip=True)

                # Verificar si la fecha sigue el patrón esperado
                if date_pattern.match(fechaStrip):
                    # Convertir la fecha al formato esperado
                    fechaFormated = datetime.strptime(fechaStrip, fecha_formato_pagina).date()

                    # Verificar si la fecha formateada coincide con la fecha actual
                    if fechaFormated == fechaHoy:
                        # Obtener los textos de nombre y plataforma
                        nombreText = nombre.get_text()
                        plataformaText = plataforma.get_text()

                        # Crear un diccionario con los datos y agregarlo a la lista
                        data_dict = {
                            "fecha": fechaStrip,
                            "titulo": nombreText,
                            "plataforma": plataformaText
                        }
                        data_list.append(data_dict)

        # Ordenar la lista por plataforma
        data_listO = sorted(data_list, key=lambda x: x['plataforma'])
        return data_listO

    except Exception as e:
        # Manejar cualquier excepción e imprimir un mensaje de error
        print("Error al serializar la aplicación:", str(e))
        return []