#!/usr/bin/env python3
import asyncio
import random

async def wait_random(max_delay=10):
    """Wait for a random delay between 0 and max_delay second
    Parameters:
    max_delay (int): The maximum delay in seconds. Default is 10.
    Returns:
    float: The random delay that was waited.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

