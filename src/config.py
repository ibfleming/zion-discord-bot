"""Configuration settings for the Zion Discord Bot."""

import os

from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

if not DISCORD_TOKEN:
    print("DISCORD_TOKEN is not set or is empty. Please check your .env file.")
    exit(1)

YTDL_FORMAT_OPTIONS = {
    "format": "bestaudio[acodec=opus]/bestaudio/best",
    "outtmpl": "%(extractor)s-%(id)s-%(title)s.%(ext)s",
    "restrictfilenames": True,
    "noplaylist": True,
    "nocheckcertificate": True,
    "ignoreerrors": False,
    "logtostderr": False,
    "quiet": True,
    "no_warnings": True,
    "default_search": "auto",
    "source_address": "0.0.0.0",
    "live_chunk_size": 10,
    "prefer_ffmpeg": True,
    "extractor_args": {
        "youtube": {
            "player_client": ["ios", "android"],
        }
    },
}

FFMPEG_OPTIONS = {
    "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",
    "options": "-vn -b:a 192k",
}
