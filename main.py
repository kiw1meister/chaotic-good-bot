import discord

class Client(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}.')

intents = discord.Intents.default()
intents.message_content = True

