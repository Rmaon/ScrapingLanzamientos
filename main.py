import bs4
import requests
import discord
from discord.ext import commands
from datetime import datetime
import lanzamientosHoy

urlLanzamientos = "https://vandal.elespanol.com/lanzamientos/0/videojuegos"

resultados = lanzamientosHoy.titulosDiarios(urlLanzamientos)

for resultado in resultados:
    print("Fecha:", resultado['fecha'])
    print("Título:", resultado['titulo'])
    print("Enlace:", resultado['enlace'])
    print()

#token = 'MTE2NzQ2MjY4OTkyMTA1Njg4MA.GzUeAM.4NHKRuYKaP3weFtM3ibz29pbaN6LsoVnKW03CA'