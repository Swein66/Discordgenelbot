import discord
from discord.ext import commands
import asyncio
import os

# Ses ve Mesaj Yetkileri (Intents)
intents = discord.Intents.default()
intents.message_content = True
intents.members = True          
intents.voice_states = True # Swéin


bot = commands.Bot(command_prefix=".", intents=intents, case_insensitive=True, help_command=None)

@bot.event
async def on_ready():
    activity = discord.Streaming(
        name="(Bot İsmin yada yazmak isteiğin) | .komut", #Düzelt
        url="https://www.twitch.tv/(istediğini yaz)" #Düzelt
    )
    await bot.change_presence(status=discord.Status.dnd, activity=activity)
    
   
    if not bot.owner_id:
        app = await bot.application_info()
        bot.owner_id = app.owner.id

    print(f'-----------------------------------------')
    print(f'✅ (Bot İsmin) Bot Aktif: {bot.user.name}') # Düzelt
    print(f'🔴 Durum: Rahatsız Etmeyin')
    print(f'🟣 Aktivite: Mor Yayın Modu')
    print(f'-----------------------------------------')

async def load_extensions():
    
    extensions = [
        'yargı', 'embed', 'komut', 'dmall', 
        'tamyasakla', 'guard', 'sorgula', 
        'play', 'stop', 'nuke', 'rol', 'ses' , 'log' , 'unyargı' , 'snipe'
    ]
    
    for ext in extensions:
        try:
            
            await bot.load_extension(ext)
            print(f"📦 Modül Yüklendi: {ext}.py")
        except Exception as e:
            print(f"❌ {ext}.py yüklenirken hata: {e}")

async def main():
    async with bot:
        await load_extensions()
        # Kendi tokenını buraya yaz
        await bot.start('YOUR_BOT_TOKEN') #Düzelt

if __name__ == "__main__":
    asyncio.run(main())