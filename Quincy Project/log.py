import discord
from discord.ext import commands
import json
import os

class LogSistemi(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.settings_file = 'settings.json'

    def get_log_channel(self, guild_id):
        if os.path.exists(self.settings_file):
            with open(self.settings_file, 'r') as f:
                data = json.load(f)
                return data.get(str(guild_id), {}).get('log_channel')
        return None

    def save_log_channel(self, guild_id, channel_id):
        data = {}
        if os.path.exists(self.settings_file):
            with open(self.settings_file, 'r') as f:
                data = json.load(f)
        
        if str(guild_id) not in data:
            data[str(guild_id)] = {}
        
        data[str(guild_id)]['log_channel'] = channel_id
        
        with open(self.settings_file, 'w') as f:
            json.dump(data, f, indent=4)

    @commands.group(name="log", invoke_without_command=True)
    @commands.has_permissions(administrator=True)
    async def log(self, ctx):
        await ctx.send("❓ Kullanım: `.log aç #kanal` veya `.log kapat`", delete_after=5)

    @log.command(name="aç")
    async def ac(self, ctx, channel: discord.TextChannel):
        self.save_log_channel(ctx.guild.id, channel.id)
        await ctx.send(f" Log sistemi {channel.mention} kanalında aktif edildi.")

    @log.command(name="kapat")
    async def kapat(self, ctx):
        self.save_log_channel(ctx.guild.id, None)
        await ctx.send(" Log sistemi devre dışı bırakıldı.")

    #Swéin

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.author.bot: return
        log_id = self.get_log_channel(message.guild.id)
        if log_id:
            channel = self.bot.get_channel(log_id)
            embed = discord.Embed(title=" Mesaj Silindi", color=discord.Color.red())
            embed.add_field(name="Kanal", value=message.channel.mention)
            embed.add_field(name="Yazar", value=message.author.mention)
            embed.add_field(name="Mesaj", value=message.content or "Görsel/Dosya", inline=False)
            await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if before.author.bot or before.content == after.content: return
        log_id = self.get_log_channel(before.guild.id)
        if log_id:
            channel = self.bot.get_channel(log_id)
            embed = discord.Embed(title=" Mesaj Düzenlendi", color=discord.Color.orange())
            embed.add_field(name="Kanal", value=before.channel.mention)
            embed.add_field(name="Yazar", value=before.author.mention)
            embed.add_field(name="Eski", value=before.content, inline=False)
            embed.add_field(name="Yeni", value=after.content, inline=False)
            await channel.send(embed=embed)

async def setup(bot):
    await bot.add_cog(LogSistemi(bot))