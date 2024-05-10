import asyncio
import sys
import os

sys.path.insert(0, f"{os.getcwd()}/slack_jobs")
from slack_jobs.slack import get_conversation_history
from slack_jobs.config import CHANNEL_ID, SLACK_BOT_TOKEN
from slack_jobs.converter import json_to_df


async def main():
    rv = await get_conversation_history(
        channel_id=CHANNEL_ID, bearer_token=SLACK_BOT_TOKEN
    )
    df = json_to_df(rv)
    df.to_csv("jobs.csv", sep="~")


if __name__ == "__main__":
    asyncio.run(main())
