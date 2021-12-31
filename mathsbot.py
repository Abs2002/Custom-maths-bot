import discord
from discord.ext import commands
import math

token='Your_token'

def factorialz(n):
  factorialy =1
  if n<=0:
    return 1
  else:
    while n>0:
      factorialy*=n
      n-=1
    return factorialy




client=discord.Client()
bot=commands.Bot(command_prefix="<")

@bot.event
async def on_ready():
  print("logged in as", bot.user.name, bot.user.id)

@bot.command()
async def echo(ctx, arg):
  await ctx.send(arg)

@bot.command()
async def add(ctx,arg):
  if "+" in arg:
    await ctx.send(eval(arg))
  else:
    await ctx.send("Are you nuts")

@bot.command()
async def subtract(ctx,arg):
  if "-" in arg:
    await ctx.send(eval(arg))
  else:
    await ctx.send("Are you nuts")

@bot.command()
async def multiply(ctx, arg):
  if "*" in arg:
    await ctx.send(eval(arg))
  else:
    await ctx.send("Are you nuts")

@bot.command()
async def divide(ctx,arg):
  if "/" in arg:
    await ctx.send(eval(arg))
  else:
    await ctx.send("Are you nuts")

@bot.command()
async def sin(ctx,arg : int):
  await ctx.send(math.sin(arg))

@bot.command()
async def cos(ctx,arg:int):
  await ctx.send(math.cos(arg))

@bot.command()
async def tan(ctx,arg:int):
  await ctx.send(math.tan(arg))

@bot.command()
async def power(ctx,arg1:int,arg2:int):
  await ctx.send(math.pow(arg1,arg2))

@bot.command()
async def sqroot(ctx,arg:int):
  await ctx.send(math.sqrt(arg))

@bot.command()
async def factorial(ctx,arg:int):
  n=factorialz(arg)
  await ctx.send(n)


@bot.command()
async def helpcommands(ctx):
  await ctx.send("following are the list of commands")
  await ctx.send("echo : sends back the same message")
  await ctx.send("add : adds number within apostrophe")
  await ctx.send("subtract : subtracts withing apostrophe")
  await ctx.send("multiply : multiplies within apostrophe")
  await ctx.send("divide : divides within apostrophe")
  await ctx.send("sin : applies sin function ")


@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

bot.run(token)
