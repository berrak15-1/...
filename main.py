import discord
import random
 
from discord.ext import commands
# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık.')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir sohbet botuyum!')


@bot.command()
async def copy(ctx, arg, c = 1):
    await ctx.send(arg * c)

@bot.command()
async def topla(ctx, a: int, b: int):
    await ctx.send(a + b)
@bot.command()
async def çıkar(ctx, a: int, b: int):
    await ctx.send(a - b)
@bot.command()
async def çarp(ctx, a: int, b: int):
    await ctx.send(a * b)
@bot.command()
async def böl(ctx, a: int, b: int):
    await ctx.send(a / b)

@bot.command()
async def emoji(ctx):
    await ctx.send("😛")
