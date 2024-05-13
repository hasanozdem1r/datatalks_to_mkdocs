import aiohttp
from slack_jobs.core import send_async_get_request, send_async_post_request
import json


async def get_conversation_history(channel_id: str, bearer_token):
    async with aiohttp.ClientSession() as session:
        headers = {
            "Content-Type": "application/json; charset=UTF-8;",
            "Authorization": f"Bearer {bearer_token}",
        }
        response = await send_async_post_request(
            session=session,
            base_url=f"https://slack.com/api/conversations.history?channel={channel_id}&include_all_metadata=true&limit=100&oldest=1&pretty=1",
            headers=headers,
        )
        return response
