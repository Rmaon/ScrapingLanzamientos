import asyncio
import discord
from discord.ext import tasks, commands
import LanzamientosHoy
import LanzamientosProximos
from Videojuego import Videojuego
from datetime import datetime


intents = discord.Intents.default()

intents.typing = False
intents.presences = False
intents.message_content = True

bot = commands.Bot(command_prefix='@', intents=intents)

# Por motivos de seguridad guardo el token de mi bot en un txt que no publico en el repositorio
with open('token.txt', 'r') as file:
    token = file.read().strip()

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

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user.name}')

async def ejecutar_comando():
    try:
        channel_id = 1095471189960433759

        # Obtener el canal
        channel = await bot.fetch_channel(channel_id)

        # Ejecutar el comando directamente en el canal
        ctx = await bot.get_context(await channel.send("@jogos"))
        await bot.invoke(ctx)

        await asyncio.sleep(5)

        print("Comando ejecutado a las", datetime.now())
    except Exception as e:
        print(f"Error al ejecutar el comando: {e}")
    finally:
        # Esperar 24 horas antes de ejecutar la función nuevamente
        await asyncio.sleep(86400)


async def main():
    while True:
        await ejecutar_comando()
        await asyncio.sleep(1)

@tasks.loop(hours=24)
async def event_Lanzamientos():
    try:
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
                await asyncio.sleep(2)  # Espera 2 segundos antes de enviar el siguiente mensaje

        if not videojuegos_Indie:
            await channel.send('\n # Hoy no han salido titulos menores...')
        else:
            await channel.send('\n # Titulos menores\n')
            mensaje = ''
            cont = 0
            proporcion = len(videojuegos_Indie) // 10  # Divide el número total de títulos por 10

            for juego in videojuegos_Indie:
                mensaje += f"{juego.plataforma}   Fecha: {juego.fecha}\nTítulo: {juego.titulo}\n\n"
                cont += 1

                if cont == proporcion:
                    await channel.send(mensaje)
                    mensaje = ''  # Reinicia el mensaje
                    cont = 0
                    await asyncio.sleep(1)

            if mensaje:
                await channel.send(mensaje)

            await asyncio.sleep(2)  # Espera 2 segundos antes de enviar el siguiente mensaje

        if not videojuegos_SemanaAAA:
            await channel.send('\n # La semana que viene no hay bombazos...')
        else:
            await channel.send('\n # Bombazos de la semana que viene :bomb::bomb:\n')
            for juego in videojuegos_SemanaAAA:
                mensaje = f"Fecha: {juego.fecha}\n[Título: {juego.titulo}]({juego.enlace})\n\n"
                await channel.send(mensaje)
                await asyncio.sleep(1)  # Espera 2 segundos antes de enviar el siguiente mensaje

        print("Mensajes enviados a las", datetime.now())
    except Exception as e:
        print(f"Error al enviar mensajes al canal: {e}")

@bot.command(name='suma')
async def sumar(ctx, num1: int, num2: int):
    response = num1 + num2
    await ctx.send(response)

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user.name}')
    event_Lanzamientos.start()

bot.run(token)