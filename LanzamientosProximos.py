import bs4
import requests
from datetime import datetime, timedelta


def titulosSemanaAAA(urlLanzamientos):
    try:
        # Hacer una solicitud a la URL proporcionada
        resultLanzamiento = requests.get(urlLanzamientos)

        # Crear un objeto BeautifulSoup para analizar el contenido HTML
        soupLanzamientos = bs4.BeautifulSoup(resultLanzamiento.text, 'html.parser')

        # Encontrar todas las tablas que tienen la clase especificada
        tablasAAA = soupLanzamientos.find_all('table', class_='table transparente tablasinbordes')

        # Obtener la fecha actual
        fechaHoy = datetime.now().date()

        # Formato de fecha en la página web
        fechaFormatoPagina = "%d/%m/%Y"

        # Lista para almacenar los datos serializados
        datos_serializados = []

        # Iterar a través de las tablas encontradas
        for tabla in tablasAAA:
            # Encontrar el elemento de fecha dentro de la tabla
            fecha_element = tabla.find('div', class_='tcenter w100 t11')

            # Obtener el texto de la fecha
            fecha_text = fecha_element.text

            # Convertir el texto de la fecha al formato de fecha esperado
            fecha_formateada = datetime.strptime(fecha_text, fechaFormatoPagina).date()

            # Definir la fecha límite como una semana a partir de hoy
            fecha_limite = fechaHoy + timedelta(days=7)

            # Verificar si la fecha está dentro del rango de la próxima semana
            if fechaHoy < fecha_formateada <= fecha_limite:
                # Encontrar el elemento del título y del enlace dentro de la tabla
                titulo_element = tabla.find('strong')
                enlace_element = tabla.find('a')

                # Obtener los datos
                fecha = fecha_text
                titulo = titulo_element.text
                enlace = enlace_element.get('href')

                # Agregar los datos a la lista
                datos_serializados.append({
                    "fecha": fecha,
                    "titulo": titulo,
                    "enlace": enlace
                })

        # Devolver la lista de datos serializados
        return datos_serializados

    except Exception as e:
        # Manejar cualquier excepción e imprimir un mensaje de error
        print("Error al serializar la aplicación:", str(e))

        # Devolver una lista vacía en caso de error
        return []
