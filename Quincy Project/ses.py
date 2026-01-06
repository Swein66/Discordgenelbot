import discord
from discord.ext import commands

class SesSistemi(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        # Swéin
        SES_KANAL_ID = SES_KANAL_ID  # Swéin #Düzelt
        
        channel = self.bot.get_channel(SES_KANAL_ID)
        if channel and isinstance(channel, discord.VoiceChannel):
            try:
                await channel.connect()
                print(f" Bot başarıyla ses kanalına bağlandı: {channel.name}")
            except Exception as e:
                print(f" Ses kanalına bağlanırken hata oluştu: {e}")
        else:
            print("Belirtilen ses kanalı ID'si bulunamadı veya bir ses kanalı değil.")

async def setup(bot):
    await bot.add_cog(SesSistemi(bot))