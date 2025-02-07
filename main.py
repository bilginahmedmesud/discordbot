import os
import discord
from discord.ext import commands

print("Melih botu v.1.0.0")

intents = discord.Intents.default()
intents.voice_states = True
intents.message_content = True
client = commands.Bot(command_prefix="!", intents=intents)

@client.event
async def on_ready():
    try:
        voice_channel = client.get_channel(int(os.getenv('CHANNEL_ID')))
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

client.run(os.getenv('TOKEN'))
