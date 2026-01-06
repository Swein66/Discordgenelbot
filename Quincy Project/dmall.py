import discord
from discord.ext import commands
import asyncio

class DMAll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="dmall")
    @commands.has_permissions(administrator=True) # Swéin
    async def dm_herkese(self, ctx, *, mesaj=None):
        if mesaj is None:
            await ctx.send(" Herkese gönderilecek bir mesaj yazmalısın!")
            return

        # Swéin
        try:
            await ctx.message.delete()
        except:
            pass

        basarili = 0
        hatali = 0
        
        bilgi_mesaji = await ctx.send(f" Duyuru başlatıldı, lütfen bekleyin...")

        for member in ctx.guild.members:
            if member.bot: # Swéin
                continue
            
            try:
                await member.send(f"{mesaj}")
                basarili += 1
                # Swéin
                await asyncio.sleep(0.5) 
            except:
                hatali += 1
        
        await bilgi_mesaji.edit(content=f" Duyuru tamamlandı!\n Başarılı: {basarili}\n Başarısız (DM Kapalı): {hatali}")

async def setup(bot):
    await bot.add_cog(DMAll(bot))