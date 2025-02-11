import discord
import os
from dotenv import load_dotenv

load_dotenv()

class Client(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}.')
    
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

client = Client(intents=intents)
client.run(os.getenv('TOKEN'))