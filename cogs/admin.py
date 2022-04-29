import nextcord.ext
from nextcord.ext import commands

class Admin(commands.Cog):
  def __init__(self,bot):
    self.bot = bot
"""
  @commands.command(name="help")
  async def help(ctx):
    await ctx.send("bbbbb")
    embed = nextcord.Embed(title="Sargoth Bot v2.0",         description=f"Bot frakcyjny        Sargoth.\n Prefix:****", color=0x000000)
    embed.add_field(name="field", value="value", inline=False)
    await ctx.send(embed=embed)

  @commands.command(name="set")
  async def set(ctx, *args):
    await ctx.send("A")
   # name = args[0]
    #l = list(args).remove(name)
    #if name == "hierarchy":
    #  await ctx.send("\n".join(l))
      
   
"""
    
def setup(bot):
  bot.add_cog(Admin(bot))