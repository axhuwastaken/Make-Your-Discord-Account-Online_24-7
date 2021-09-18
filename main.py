import discord
import os
import config

client = discord.Client()

@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.dnd) #dnd, idle, online
  print("i am running")

client.run(config.token, bot=False)
