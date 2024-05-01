import aiohttp
from slack_jobs.core import send_async_get_request, send_async_post_request
from slack_jobs.config import CHANNEL_ID, SLACK_BOT_TOKEN
import json


async def get_conversation_history(channel_id: str):
    async with aiohttp.ClientSession() as session:
        headers = {
            "Content-Type": "application/json; charset=UTF-8;",
            "Authorization": "Bearer xoxb-7047917217333-7047978004821-z0FfOsAq8iKs7Dfq7VnB9u0r",
        }
        response = await send_async_post_request(
            session=session,
            base_url=f"https://slack.com/api/conversations.history?channel={channel_id}&include_all_metadata=true&limit=999&oldest=1&pretty=1",
            headers=headers,
        )
        return response
