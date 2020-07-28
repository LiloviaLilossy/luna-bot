from discord.ext import commands
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
log_format = '%(asctime)s %(name)s %(levelname)s: %(message)s~lu'

class Fun(commands.Cog):
    def __init__(self, bot):
        logger.info("Loading extension Fun")
        self.bot = bot
    
    @commands.command()
    async def hug(self, ctx, *, text: commands.clean_content):
        if "@everyone" in text or "@here" in text:
            return await ctx.send("I won't let you ping many people~lu!")
        await ctx.send(f"*hugs {text}~lu*")

def setup(bot):
    bot.add_cog(Fun(bot))
    bot.logger.info("Fun is ready")