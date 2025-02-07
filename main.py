import os
import time
import discord
from discord.ext import commands

print("Melih botu v.1.0.0")
time.sleep(0.5)

intents = discord.Intents.all()
client = commands.Bot(command_prefix="!", intents=intents)

# Token ve ID'yi environment variables'dan al
Token = os.getenv('TOKEN')
Id = int(os.getenv('CHANNEL_ID'))

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
