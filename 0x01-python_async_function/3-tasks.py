#!/usr/bin/env python3
"""
Create a regular function that returns an asyncio.Task for wait_random.
"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates and returns an asyncio.Task for the wait_random coroutine.
    
    Args:
        max_delay (int): The maximum delay for the wait_random function.
    
    Returns:
        asyncio.Task: An asyncio task for wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))