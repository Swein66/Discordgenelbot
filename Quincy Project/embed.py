import discord
from discord.ext import commands

class EmbedSistemi(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="embed")
    async def embed_yaz(self, ctx, *, mesaj=None):
        if mesaj is None:
            await ctx.send(" Bir mesaj yazmalısın!")
            return

        # Swéin
        try:
            await ctx.message.delete()
        except:
            pass

        # Swéin
        await ctx.send(f"{mesaj}")

async def setup(bot):
    await bot.add_cog(EmbedSistemi(bot))