import discord
from discord.ext import commands
import json
import os

class Guard(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config_file = "settings.json"
        self.load_config()

    def load_config(self):
        if os.path.exists(self.config_file):
            with open(self.config_file, "r") as f:
                self.config = json.load(f)
        else:
            self.config = {"status": "kapalı"}
            self.save_config()

    def save_config(self):
        with open(self.config_file, "w") as f:
            json.dump(self.config, f, indent=4)

    @commands.command(name="guard")
    @commands.has_permissions(administrator=True)
    async def guard_toggle(self, ctx, secenek: str = None):
        """Guard sistemini açar veya kapatır."""
        await ctx.message.delete()
        
        if secenek == "aç":
            self.config["status"] = "açık"
            self.save_config()
            color = 0x2ecc71 # Swéin
            desc = " **Guard Sistemi Açıldı.**"
        elif secenek == "kapat":
            self.config["status"] = "kapalı"
            self.save_config()
            color = 0xe74c3c # Swéin
            desc = " **Guard Sistemi Kapatıldı.**"
        else:
            return await ctx.send(" Lütfen bir seçenek belirtin: `.guard aç` veya `.guard kapat`", delete_after=5)

        embed = discord.Embed(title=" QUINCY SECURITY", description=desc, color=color)
        embed.set_footer(text=f"İşlemi Yapan: {ctx.author.name}")
        await ctx.send(embed=embed)

    # Swéin
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot or self.config["status"] == "kapalı":
            return

        # Swéin
        reklam_kelimeleri = ["discord.gg/", "https://", ".com", ".net ", ".org", "www.", "bit.ly/", "t.me/", "join my server", "join our server" , "discord.me/" , "discord.io/" , "discordapp.com/invite/" ,  "invite.gg/" , "dsc.gg/" , "discord.gg" , "http://", "https://", "www.", ".com", ".net", ".org", ".io", ".gg", "bit.ly", "tinyurl.com", "join my server", "join our server", "t.me/", "telegram.me/"]
        if any(kelime in message.content.lower() for kelime in reklam_kelimeleri):
            if not message.author.guild_permissions.administrator:
                await message.delete()
                await message.channel.send(f" {message.author.mention}, Guard sistemi aktif!", delete_after=3)
        küfür_kelimeleri = ["aptal", "salak", "oç", "amk", "siktir", "orospu", "piç", "yarrak", "göt", "mal", "gerizekalı ", "sik", "amına", "ananı", "orospu çocuğu" , "amcık" , "yavşak" , "pezevenk" , "sürtük" , "kahpe" , "gavat" , "yarak" , "sikik" , "amcık çocuğu" , "amcık oğlanı", "sikini" , "amınakodumun" ,   "amınakodumu" , "amınakodum" , "amcık" , "amcıklar" , "sikimi" , "sikime" , "sikiyor" , "sikiş" , "sikişi" , "sikişte" , "yarram" , "yarrama" , "yarramam" , "yarramı" , "götünü" , "götüne" , "götümü" , "göte" , "götler" , "götlere" , "götlük" , "götelemek" , "göteledi" , "sikimi" , "sikime" , "sikmiş" , "sikmişim" , "sikmişsin" , "sikmişiz" , "sikmişsiniz" , "sikmişler"]
        if any(kelime in message.content.lower() for kelime in küfür_kelimeleri):
            if not message.author.guild_permissions.administrator:
                await message.delete()
                await message.channel.send(f" {message.author.mention}, Guard Aktif!", delete_after=3)
async def setup(bot):
    await bot.add_cog(Guard(bot))