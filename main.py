import bs4
import asyncio
import requests
import discord
from discord.ext import commands
from datetime import datetime
import LanzamientosHoy
import LanzamientosProximos

intents = discord.Intents.default()

intents.typing = False
intents.presences = False
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

urlLanzamientos = "https://vandal.elespanol.com/lanzamientos/0/videojuegos"

titulosDiaAAA = LanzamientosHoy.titulosDiariosAAA(urlLanzamientos)
titulosDiaIndie = LanzamientosHoy.titulosDiariosIndie(urlLanzamientos)
titulosSemanaAAA = LanzamientosProximos.titulosSemanaAAA(urlLanzamientos)

for resultado in titulosDiaAAA:
    print("Fecha:", resultado['fecha'])
    print("Título:", resultado['titulo'])
    print("Enlace:", resultado['enlace'])
    print()

for resultado2 in titulosDiaIndie:
    print(resultado2['plataforma'])
    print("Fecha:", resultado2['fecha'])
    print("Título:", resultado2['titulo'])
    print()

for resultado3 in titulosSemanaAAA:
    print("Fecha:", resultado3['fecha'])
    print("Título:", resultado3['titulo'])
    print("Enlace:", resultado3['enlace'])
    print()


@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user.name}')

@bot.command()
async def kjuegos(ctx):
    # Enviar mensajes de titulosDiaAAA
    mensaje = ''
    for resultado in titulosDiaAAA:
        mensaje += f"[{resultado['titulo']}]({resultado['enlace']})\n\n"

    await ctx.send(mensaje)
    await asyncio.sleep(2)  # Espera 2 segundos antes de enviar el siguiente mensaje

    # Enviar mensajes de titulosDiaIndie
    mensaje = ''
    cont = 0
    proporcion = len(titulosDiaIndie) // 10  # Divide el número total de títulos por 10

    for resultado2 in titulosDiaIndie:
        mensaje += f"{resultado2['plataforma']}   Fecha: {resultado2['fecha']}\nTítulo: {resultado2['titulo']}\n"
        cont += 1

        if cont == proporcion:
            await ctx.send(mensaje)
            mensaje = ''  # Reinicia el mensaje
            cont = 0

    # Enviar el mensaje restante (si es menor que proporcion)
    if mensaje:
        await ctx.send(mensaje)

    await asyncio.sleep(2)  # Espera 2 segundos antes de enviar el siguiente mensaje

    # Enviar mensajes de titulosSemanaAAA
    mensaje = ''
    for resultado3 in titulosSemanaAAA:
        mensaje += f"Fecha: {resultado3['fecha']}\n[Título: {resultado3['titulo']}]({resultado3['enlace']})\n\n"
    await ctx.send(mensaje)
    await asyncio.sleep(2)  # Espera 2 segundos antes de enviar el siguiente mensaje


bot.run('MTE2NzQ2MjY4OTkyMTA1Njg4MA.G2TojV.W9g4Vz2WpHJ2Fqf3IHITQKreTG5nw-SsVXdSFM')