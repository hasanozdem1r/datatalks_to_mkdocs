import asyncio
import sys
import os

sys.path.insert(0, f"{os.getcwd()}/slack_jobs")
from slack_jobs.slack import get_conversation_history
from slack_jobs.config import CHANNEL_ID, SLACK_BOT_TOKEN
from slack_jobs.converter import json_to_df
from slack_jobs.utils import get_job_url, prepare_slack_message, write_to_file

CWD = os.getcwd()


async def main():
    rv = await get_conversation_history(
        channel_id=CHANNEL_ID, bearer_token=SLACK_BOT_TOKEN
    )
    print(rv)
    df = json_to_df(rv)
    df["url"] = df["slack_message"].apply(get_job_url)
    final_message = prepare_slack_message(df=df)
    write_to_file(file_name=f"{CWD}/docs/index.md", data=final_message)


if __name__ == "__main__":
    asyncio.run(main())
