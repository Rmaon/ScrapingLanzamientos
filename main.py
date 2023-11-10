import json
import LanzamientosHoy
import LanzamientosProximos
from Videojuego import Videojuego

urlLanzamientos = "https://vandal.elespanol.com/lanzamientos/0/videojuegos"

titulosDiaAAA = LanzamientosHoy.titulosDiariosAAA(urlLanzamientos)
titulosDiaIndie = LanzamientosHoy.titulosDiariosIndie(urlLanzamientos)
titulosSemanaAAA = LanzamientosProximos.titulosSemanaAAA(urlLanzamientos)

videojuegos_AAA = []
videojuegos_Indie = []
videojuegos_SemanaAAA = []

for resultado in titulosDiaAAA:
    videojuego = Videojuego(resultado['fecha'], resultado['titulo'], resultado['enlace'])
    videojuegos_AAA.append(videojuego)

for resultado2 in titulosDiaIndie:
    videojuego = Videojuego(resultado2['fecha'], resultado2['titulo'], plataforma=resultado2['plataforma'])
    videojuegos_Indie.append(videojuego)

for resultado3 in titulosSemanaAAA:
    videojuego = Videojuego(resultado3['fecha'], resultado3['titulo'], resultado3['enlace'])
    videojuegos_SemanaAAA.append(videojuego)


def verLanzamientosAAA():
    for juego in videojuegos_AAA:
        juego.mostrar_datos()


def verLanzamientosHoy():
    for juego in videojuegos_Indie:
        juego.mostrar_datos()


def verLanzamientosSemanaQueViene():
    for juego in videojuegos_SemanaAAA:
        juego.mostrar_datos()


def guardarAJson(datos, nombre_archivo):
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        json.dump(datos, archivo, ensure_ascii=False, indent=2)


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
