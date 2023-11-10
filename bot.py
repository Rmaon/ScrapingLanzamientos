import asyncio
import discord
from discord.ext import tasks, commands
import LanzamientosHoy
import LanzamientosProximos
from Videojuego import Videojuego
from datetime import datetime

# Crear una instancia de la clase Intents para personalizar las intenciones del bot
intents = discord.Intents.default()

# Desactivar ciertas intenciones para mejorar la eficiencia y seguridad
intents.typing = False
intents.presences = False
intents.message_content = True

# Crear una instancia del bot con el prefijo de comando y las intenciones personalizadas
bot = commands.Bot(command_prefix='@', intents=intents)

<<<<<<< Updated upstream
=======
# Leer el token del archivo 'token.txt'
with open('token.txt', 'r') as file:
    token = file.read().strip()

# URL de la página de lanzamientos de videojuegos
>>>>>>> Stashed changes
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

# Evento que se ejecuta cuando el bot se conecta
@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user.name}')

# Función asincrónica para ejecutar un comando cada 24 horas
async def ejecutar_comando():
    try:
        # ID del canal donde se ejecutará el comando
        channel_id = 1095471189960433759

        # Obtener el canal
        channel = await bot.fetch_channel(channel_id)

        # Ejecutar el comando directamente en el canal
        ctx = await bot.get_context(await channel.send("@jogos"))
        await bot.invoke(ctx)

        # Esperar 5 segundos después de ejecutar el comando
        await asyncio.sleep(5)

        print("Comando ejecutado a las", datetime.now())
    except Exception as e:
        print(f"Error al ejecutar el comando: {e}")
    finally:
        # Esperar 24 horas antes de ejecutar la función nuevamente
        await asyncio.sleep(86400)

# Función principal asincrónica que ejecuta la función anterior en bucle
async def main():
    while True:
        await ejecutar_comando()
        await asyncio.sleep(1)

# Tarea programada que se ejecuta cada 24 horas para enviar mensajes de lanzamientos de videojuegos
@tasks.loop(hours=24)
async def event_Lanzamientos():
    try:
        # ID del canal donde se enviarán los mensajes
        channel_id = 1095471189960433759

        # Obtener el canal
        channel = await bot.fetch_channel(channel_id)

        # Enviar mensajes de videojuegos
        if not videojuegos_AAA:
            await channel.send('\n # Hoy no hay bombazos...')
        else:
            await channel.send('\n # BOMBAZOS DEL DIA :bomb:\n')
            for juego in videojuegos_AAA:
                mensaje = f"[{juego.titulo}]({juego.enlace})\n\n"
                await channel.send(mensaje)
                # Espera 2 segundos antes de enviar el siguiente mensaje
                await asyncio.sleep(2)

        if not videojuegos_Indie:
            await channel.send('\n # Hoy no han salido títulos menores...')
        else:
            await channel.send('\n # Títulos menores\n')
            mensaje = ''
            cont = 0
            proporcion = len(videojuegos_Indie) // 10  # Divide el número total de títulos por 10

            for juego in videojuegos_Indie:
                mensaje += f"{juego.plataforma}   Fecha: {juego.fecha}\nTítulo: {juego.titulo}\n\n"
                cont += 1

                if cont == proporcion:
                    await channel.send(mensaje)
                    mensaje = ''  # Reinicia el mensaje
                    # Espera 1 segundo antes de enviar el siguiente mensaje
                    await asyncio.sleep(1)

            if mensaje:
                await channel.send(mensaje)

            # Espera 2 segundos antes de enviar el siguiente mensaje
            await asyncio.sleep(2)

        if not videojuegos_SemanaAAA:
            await channel.send('\n # La semana que viene no hay bombazos...')
        else:
            await channel.send('\n # Bombazos de la semana que viene :bomb::bomb:\n')
            for juego in videojuegos_SemanaAAA:
                mensaje = f"Fecha: {juego.fecha}\n[Título: {juego.titulo}]({juego.enlace})\n\n"
                await channel.send(mensaje)
                # Espera 1 segundo antes de enviar el siguiente mensaje
                await asyncio.sleep(1)

        print("Mensajes enviados a las", datetime.now())
    except Exception as e:
        print(f"Error al enviar mensajes al canal: {e}")

# Evento que se ejecuta cuando el bot se conecta; inicia la tarea programada
@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user.name}')
    event_Lanzamientos.start()

<<<<<<< Updated upstream
bot.run('MTE2NzQ2MjY4OTkyMTA1Njg4MA.G2TojV.W9g4Vz2WpHJ2Fqf3IHITQKreTG5nw-SsVXdSFM')
=======
# Ejecutar el bot con el token
bot.run(token)
>>>>>>> Stashed changes
