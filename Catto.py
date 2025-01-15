import discord
import feedparser
import asyncio
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv('DISCORD_BOT_TOKEN')

# Discord bot intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

# RSS feed URL
RSS_FEED_URL = "https://rss.app/feeds/kgvB3KGQAZFI4ylD.xml"  # Replace with your RSS feed URL

# Discord channel ID to post updates
DISCORD_CHANNEL_ID = 1325135942918344714  # REPLACE THE CHANNEL ID WHEN YOU WANT IT SENT TO THAT SPECIFIC CHANNEL LILBRO

# Track last seen entry to prevent duplicate posts
last_seen_entry_id = None


async def fetch_rss_updates():
    """Fetch the RSS feed periodically and post updates to Discord."""
    global last_seen_entry_id
    await bot.wait_until_ready()  # Ensure the bot is ready before running the task

    while not bot.is_closed():
        try:
            feed = feedparser.parse(RSS_FEED_URL)

            if feed.entries:
                latest_entry = feed.entries[0]

                if latest_entry.id != last_seen_entry_id:
                    last_seen_entry_id = latest_entry.id

                    title = latest_entry.title
                    link = latest_entry.link
                    message = f"@everyone\nNew Tweet: {title}\n{link}"

                    # Send message to the Discord channel
                    channel = bot.get_channel(DISCORD_CHANNEL_ID)
                    if channel:
                        await channel.send(message)

        except Exception as e:
            print(f"Error fetching RSS feed: {e}")

        # Check for feed updates every 5 minutes
        await asyncio.sleep(300)


@bot.event
async def on_ready():
    print(f"Bot is now online as {bot.user}")


@bot.event
async def on_disconnect():
    print("Bot disconnected, cleaning up resources...")


async def main():
    # Start the RSS update task
    asyncio.create_task(fetch_rss_updates())
    # Start the bot
    await bot.start(TOKEN)


if __name__ == "__main__":
    # Run the bot's main event loop
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Shutting down bot.")
