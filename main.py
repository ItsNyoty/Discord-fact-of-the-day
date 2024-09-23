import discord
import requests
import asyncio
from datetime import datetime, timedelta

intents = discord.Intents.default()
client = discord.Client(intents=intents)

WIKI_API_URL = "https://en.wikipedia.org/api/rest_v1/feed/featured/{year}/{month}/{day}"

TOKEN = 'YOUR_DISCORD_BOT_TOKEN'

CHANNEL_ID = YOUR_CHANNEL_ID
class WikipediaButton(discord.ui.View):
    def __init__(self, url):
        super().__init__()
        self.add_item(discord.ui.Button(label="Click here to read more", url=url))

async def get_wikipedia_featured():
    now = datetime.now()
    url = WIKI_API_URL.format(year=now.year, month=f"{now.month:02d}", day=f"{now.day:02d}")

    headers = {
        "User-Agent": "DiscordBot/1.0 (contact@example.com)"
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        try:
            data = response.json()
            featured_article = data['tfa']['titles']['normalized']
            summary = data['tfa']['extract']
            article_url = data['tfa']['content_urls']['desktop']['page']
            thumbnail_url = data['tfa']['thumbnail']['source'] if 'thumbnail' in data['tfa'] else None
            
            return featured_article, summary, article_url, thumbnail_url
        except KeyError:
            return None, "No featured article available for today.", None, None
    else:
        return None, f"Failed to retrieve featured article: {response.status_code}", None, None

async def send_daily_featured():
    channel = client.get_channel(CHANNEL_ID)

    while True:
        title, summary, article_url, thumbnail_url = await get_wikipedia_featured()
        embed = discord.Embed(title=title or "Wikipedia Featured Article", description=summary, color=0x1d9bf0)

        if thumbnail_url:
            embed.set_thumbnail(url=thumbnail_url)

        embed.set_footer(text=f"Featured by Wikipedia • {datetime.now().strftime('%Y-%m-%d')}")

        view = WikipediaButton(article_url) if article_url else None
        await channel.send(embed=embed, view=view)

        # 24h timer
        await asyncio.sleep(86400)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    client.loop.create_task(send_daily_featured())


client.run(TOKEN)
