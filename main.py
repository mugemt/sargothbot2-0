import json
import os;
import nextcord
from nextcord.ext import commands
TESTING_GUILD_ID = 721374983837974570
f = open('config.json')
config  = json.load(f)
token = config['token']
prefix= config['prefix']
bot = commands.Bot(command_prefix = prefix)
bot.remove_command('help')

@bot.event
async def on_ready():
    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}')

for fn in os.listdir("./cogs"):
  if fn.endswith(".py"):
    bot.load_extension(f'cogs.{fn[:-3]}')

@bot.command(name="set")
async def set(ctx, *args):
  await ctx.send("A")
  name = args[0]
  l = list(args)
  l.remove(name)
  print(l)
  if name == "hierarchy":
    await ctx.send("\n".join(l))




@bot.command()
async def load(ctx,extension):
  bot.load_extension(extension)
  await ctx.send("Loaded Cog")

@bot.command()
async def unload(ctx,extension):
  bot.unload_extension(extension)
  await ctx.send("Loaded Cog")

@bot.command()
async def reload(ctx,extension):
  bot.reload_extension(extension)
  await ctx.send("Loaded Cog")


if __name__ == '__main__':
    bot.run(token)