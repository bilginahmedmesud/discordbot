import os
import time
import discord
from discord.ext import commands

print("Melih botu v.1.0.0")
time.sleep(0.5)

intents = discord.Intents.all()  # Tüm intents'leri aktif et
client = commands.Bot(command_prefix="!", intents=intents)

Token = "MTMzNzM5MTA4NjQ0ODE1MjU3Ng.GUzXXh.IFhzEG0UBa7ajW32Ec8uoke2zsVaUhurJULiRY"
Id = int(1022641335183876157)

@client.event
async def on_ready():
    try:
        voice_channel = client.get_channel(Id)
        if voice_channel:
            await client.change_presence(activity=discord.Activity(
                type=discord.ActivityType.competing, 
                name="Askerde 🔫🚁", 
                details="🎖️ TSK'da görevli", 
                state="Vatanı Koruyor⚔️"
                ))
            await voice_channel.connect()
            print('Logged in as {0.user}'.format(client))
            print('Connected to voice channel: {}'.format(voice_channel))
        else:
            print('Kanal bulunamadı')
    except Exception as e:
        print(f'Hata: {e}')

client.run(Token)
