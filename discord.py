import random
import discord
from discord import app_commands

TOKEN = ""

intents = discord.Intents.default()

bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)

dicas = [
    "Use uma garrafa reutilizavel.",
    "Apague as luzes que nao estiver usando.",
    "Evite desperdicar alimentos.",
    "Separe os residuos para a coleta seletiva.",
    "Use sacolas reutilizaveis nas compras.",
    "Economize agua durante o banho."
]

desafios = [
    "Passe o dia usando uma garrafa reutilizavel.",
    "Separe corretamente os residuos da sua casa.",
    "Evite desperdicar alimentos hoje.",
    "Reutilize um objeto que iria para o lixo.",
    "Apague as luzes dos ambientes vazios."
]


@tree.command(name="dica", description="Receba uma dica ecologica")
async def dica(interaction: discord.Interaction):
    mensagem = random.choice(dicas)
    await interaction.response.send_message(
        "🌱 Dica ecologica:\n" + mensagem
    )


@tree.command(name="reciclagem", description="Aprenda sobre reciclagem")
async def reciclagem(interaction: discord.Interaction):
    mensagem = (
        "♻️ Guia rapido de reciclagem\n\n"
        "📄 Papel: jornais e caixas limpas.\n"
        "🥫 Metal: latas limpas.\n"
        "🍾 Vidro: garrafas e potes aceitos "
        "pela coleta local.\n"
        "🧴 Plastico: embalagens vazias e limpas.\n\n"
        "Consulte as regras da coleta seletiva "
        "da sua cidade."
    )
    await interaction.response.send_message(mensagem)


@tree.command(name="desafio", description="Receba um desafio sustentavel")
async def desafio(interaction: discord.Interaction):
    mensagem = random.choice(desafios)
    await interaction.response.send_message(
        "🌎 Seu desafio sustentavel:\n" + mensagem
    )


@bot.event
async def on_ready():
    await tree.sync()
    print("EcoBot esta online!")
    print("Usuario: " + str(bot.user))


bot.run(TOKEN)

    
