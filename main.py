import discord
from discord.ext import commands
from discord import app_commands
import os
from dotenv import load_dotenv

load_dotenv()

class Client(commands.Bot):
    async def on_ready(self):
        print(f'Logged in as {self.user}.')

        # Force sync test server
        try:
            guild = discord.Object(id=int(serverID))
            synced = await self.tree.sync(guild=guild)
            print(f'Synced {len(synced)} command(s) to server {guild.id}')
        except Exception as e:
            print(f'Error syncing commands: {e}')
    
    async def on_message(self, message):
        # Prevents bot from replying to itself
        if message.author == self.user:
            return
        
        if message.content.startswith('yo'):
            print(f'Message from {message.author}: {message.content}')
            await message.channel.send(f'Yo {message.author.name}')

    async def on_reaction_add(self, reaction, user):
        await reaction.message.channel.send('Reaction confirmed')


intents = discord.Intents.default()
intents.message_content = True
# Command prefix can be anything as Discord is trying to deprecate command prefixes in favor of using slash commands
client = Client(command_prefix="!", intents=intents)

# Server ID to locally test one server
serverID = os.getenv('SERVER')
GUILD_ID = discord.Object(id=int(serverID))

print(f"Test server ID: {serverID}")  # Debugging line

@client.tree.command(name='hello', description="This just says hello!", guild=GUILD_ID)
async def sayHello(interaction: discord.Interaction):
    await interaction.response.send_message("Hello!")

@client.tree.command(name='displayserverid', description="This displays the server ID", guild=GUILD_ID)
async def displayServerID(interaction: discord.Interaction):
    await interaction.response.send_message(f"{serverID}")

@client.tree.command(name='printer', description="This parrots the user!", guild=GUILD_ID)
async def printer(interaction: discord.Interaction, printer: str):
    await interaction.response.send_message(printer)

client.run(os.getenv('TOKEN'))