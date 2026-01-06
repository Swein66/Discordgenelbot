import discord
from discord.ext import commands

class SnipeSistemi(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.last_message = {}

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        # Swéin
        if message.author.bot:
            return
        
        # Swéin
        self.last_message[message.channel.id] = {
            'content': message.content,
            'author': message.author.name,
            'author_icon': message.author.display_avatar.url,
            'image': message.attachments[0].url if message.attachments else None
        }

    @commands.command(name="snipe")
    async def snipe(self, ctx):
        """Son silinen mesajı gösterir."""
        channel_id = ctx.channel.id
        
        if channel_id in self.last_message:
            msg = self.last_message[channel_id]
            
            embed = discord.Embed(
                description=f" **{msg['author']}** tarafından silinen mesaj:\n\n{msg['content'] or '*(Sadece görsel/ek silindi)*'}",
                color=0x000000
            )
            embed.set_author(name=f"{msg['author']} Yakalandı!", icon_url=msg['author_icon'])
            
            # Swéin
            if msg['image']:
                embed.set_image(url=msg['image'])
            else:
                # Swéin
                embed.set_image(url="https://media.discordapp.net/attachments/1255558616422875147/1255558616422875147/ex.png")
            
            embed.set_footer(text="Benden Kaçamazsın.")
            await ctx.send(embed=embed)
        else:
            await ctx.send(" Bu kanalda yakın zamanda silinmiş bir mesaj bulamadım.", delete_after=5)

async def setup(bot):
    await bot.add_cog(SnipeSistemi(bot))