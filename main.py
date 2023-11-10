import json
import LanzamientosHoy
import LanzamientosProximos
from Videojuego import Videojuego

# URL de la página de lanzamientos de videojuegos
urlLanzamientos = "https://vandal.elespanol.com/lanzamientos/0/videojuegos"

# Obtener títulos diarios AAA, diarios Indie y de la próxima semana AAA
titulosDiaAAA = LanzamientosHoy.titulosDiariosAAA(urlLanzamientos)
titulosDiaIndie = LanzamientosHoy.titulosDiariosIndie(urlLanzamientos)
titulosSemanaAAA = LanzamientosProximos.titulosSemanaAAA(urlLanzamientos)

# Listas para almacenar instancias de la clase Videojuego
videojuegos_AAA = []
videojuegos_Indie = []
videojuegos_SemanaAAA = []

# Crear instancias de Videojuego y agregarlas a las listas correspondientes
for resultado in titulosDiaAAA:
    videojuego = Videojuego(resultado['fecha'], resultado['titulo'], resultado['enlace'])
    videojuegos_AAA.append(videojuego)

for resultado2 in titulosDiaIndie:
    videojuego = Videojuego(resultado2['fecha'], resultado2['titulo'], plataforma=resultado2['plataforma'])
    videojuegos_Indie.append(videojuego)

for resultado3 in titulosSemanaAAA:
    videojuego = Videojuego(resultado3['fecha'], resultado3['titulo'], resultado3['enlace'])
    videojuegos_SemanaAAA.append(videojuego)

# Función para mostrar los lanzamientos AAA de hoy
def verLanzamientosAAA():
    for juego in videojuegos_AAA:
        juego.mostrar_datos()

# Función para mostrar los lanzamientos Indie de hoy
def verLanzamientosHoy():
    for juego in videojuegos_Indie:
        juego.mostrar_datos()

# Función para mostrar los lanzamientos AAA de la semana que viene
def verLanzamientosSemanaQueViene():
    for juego in videojuegos_SemanaAAA:
        juego.mostrar_datos()

# Función para guardar datos en formato JSON
def guardarAJson(datos, nombre_archivo):
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        json.dump(datos, archivo, ensure_ascii=False, indent=2)

# Bucle principal del programa
while True:
    # Mostrar el menú
    print('````````````````````````````````````````````````')
    print("         BOMBAZO INFORMATIVO :")
    print("1. Ver Lanzamientos AAA de hoy")
    print("2. Ver lanzamientos menores de hoy")
    print("3. Ver lanzamientos de la semana que viene")
    print("4. Guardar en json toda la informacion posible")
    print("5. Salir")
    print('````````````````````````````````````````````````')

    # Obtener la opción del usuario
    opcion = input("Selecciona una opción (1-5): ")

    # Evaluar la opción seleccionada
    if opcion == "1":
        verLanzamientosAAA()
    elif opcion == "2":
        verLanzamientosHoy()
    elif opcion == "3":
        verLanzamientosSemanaQueViene()
    elif opcion == "4":
        # Guardar datos en formato JSON
        guardarAJson({
            "titulosDiaAAA": titulosDiaAAA,
            "titulosDiaIndie": titulosDiaIndie,
            "titulosSemanaAAA": titulosSemanaAAA
        }, 'datosCompletos.json')
        print("Datos guardados en 'datosCompletos.json'")
    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")
