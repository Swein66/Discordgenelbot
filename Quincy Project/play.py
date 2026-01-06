import discord
from discord.ext import commands
import yt_dlp
import os

class MusicPlay(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.ydl_opts = {'format': 'bestaudio/best', 'quiet': True, 'noplaylist': True}

    @commands.command(name="play")
    async def play(self, ctx, *, search: str = None):
        if search is None:
            return await ctx.send(" Bir şarkı adı gir!")
        
        if not ctx.author.voice:
            return await ctx.send(" Önce bir ses kanalına girmen gerekiyor!")

        channel = ctx.author.voice.channel
        voice_client = ctx.voice_client or await channel.connect()

        await ctx.message.delete()
        msg = await ctx.send(f" **{search}** aranıyor...")

        # --- FFmpeg Yol Kontrolü ---
        # Swéin
        ffmpeg_executable = "ffmpeg" 
        
        # Swéin
        if not os.path.exists(ffmpeg_executable):
            alternatif_yol = "C:/ffmpeg/bin/ffmpeg.exe"
            if os.path.exists(alternatif_yol):
                ffmpeg_executable = alternatif_yol
        # ---------------------------

        try:
            with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
                info = ydl.extract_info(f"ytsearch:{search}", download=False)['entries'][0]
                url = info['url']

            if voice_client.is_playing():
                voice_client.stop()

            voice_client.play(discord.FFmpegPCMAudio(
                url, 
                executable=ffmpeg_executable, 
                before_options="-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5", 
                options="-vn"
            ))
            
            await msg.edit(content=f"🎶 **{info['title']}** çalınıyor...")
        except Exception as e:
            await msg.edit(content=f" Hata oluştu: {e}\n(Not: FFmpeg hala bulunamadıysa lütfen bilgisayarı yeniden başlatın.)")

async def setup(bot):
    await bot.add_cog(MusicPlay(bot))