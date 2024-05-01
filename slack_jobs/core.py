from typing import Dict, Optional
import aiohttp
import backoff


def backoff_handler(details):
    print(
        "Backing off {wait:0.1f} seconds after {tries} tries "
        "calling function {target} with args {args} and kwargs "
        "{kwargs}".format(**details)
    )


@backoff.on_exception(
    wait_gen=backoff.expo,
    exception=(
        aiohttp.ClientError,
        aiohttp.WebSocketError,
        aiohttp.ClientConnectionError,
        aiohttp.ServerDisconnectedError,
        aiohttp.ClientConnectionError,
    ),
    max_time=10,
    on_backoff=backoff_handler,
)
async def send_async_get_request(
    session: aiohttp.ClientSession,
    base_url: str,
    headers: Dict = None,
    params: Dict = None,
    timeout: int = 3600,
    **kwargs,
):
    async with session.get(
        url=base_url,
        params=params,
        headers=headers,
        timeout=timeout,
        **kwargs,
    ) as response:
        if response.status == 200:
            return await response.json()
        return None


@backoff.on_exception(
    wait_gen=backoff.expo,
    exception=(
        aiohttp.ClientError,
        aiohttp.WebSocketError,
        aiohttp.ClientConnectionError,
        aiohttp.ServerDisconnectedError,
        aiohttp.ClientConnectionError,
    ),
    max_time=10,
    on_backoff=backoff_handler,
)
async def send_async_post_request(
    session: aiohttp.ClientSession,
    base_url: str,
    headers: Dict = None,
    data: Dict = None,
    timeout: int = 3600,
    **kwargs,
):
    async with session.post(
        url=base_url,
        json=data,
        headers=headers,
        timeout=timeout,
        **kwargs,
    ) as response:
        if response.status == 200:
            return await response.json()
        return response.text


"""
https://slack.com/api/conversations.history?channel=C071VEV2J81&include_all_metadata=true&limit=999&oldest=1&pretty=1
Authorization: Bearer xoxb-7047917217333-7047978004821-z0FfOsAq8iKs7Dfq7VnB9u0r
"""


async def main():
    async with aiohttp.ClientSession() as session:
        rv = await send_async_post_request(
            session=session,
            base_url="https://slack.com/api/conversations.history?channel=C071VEV2J81&include_all_metadata=true&limit=999&oldest=1&pretty=1",
            headers={
                "Content-Type": "application/json; charset=UTF-8;",
                "Authorization": "Bearer xoxb-7047917217333-7047978004821-z0FfOsAq8iKs7Dfq7VnB9u0r",
            },
        )
        print(rv)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
