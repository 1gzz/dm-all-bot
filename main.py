import discord
from discord.ext import commands
import asyncio
import json

with open('config.json', 'r') as config_file:
    config = json.load(config_file)

TOKEN = config['TOKEN']
allowed_user_ids = config['allowed_user_ids']

intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    RESET = '\033[0m'

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command(name='info')
async def info(ctx):
    print("Help command triggered")
    embed = discord.Embed(title="Help", description="List of commands", color=0x00ff00)
    embed.add_field(name="$dmall [message]", value="Send a DM to all members in the server with the specified message.", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def dmall(ctx, *, message: str):
    print("dmall command triggered")
    if ctx.author.id not in allowed_user_ids:
        await ctx.send("You do not have permission to use this command.")
        print(f"{Colors.RED} [-] User {ctx.author} tried to use dmall without permission.{Colors.RESET}")
        return

    await ctx.send("Starting to send DMs...")

    members = [member for member in ctx.guild.members if not member.bot]
    total_members = len(members)
    for i, member in enumerate(members):
        try:
            await member.send(message)
            print(f"{Colors.GREEN}[+] DM sent to {member.name}#{member.discriminator}{Colors.RESET}")
            await asyncio.sleep(0.7)
        except Exception as e:
            print(f"{Colors.RED}[-] Could not DM {member.name}#{member.discriminator}: {e}{Colors.RESET}")

    await ctx.send("Finished sending DMs.")

bot.run(TOKEN)