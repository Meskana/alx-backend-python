#!/usr/bin/env python3
"""
Modified wait_n function that uses task_wait_random instead of wait_random.
"""

import asyncio
from typing import List
task_wait_random = __import__( '3-tasks' ).task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times and returns the list of delays in ascending order.
    
    Args:
        n (int): The number of times to spawn task_wait_random.
        max_delay (int): The maximum delay for task_wait_random.
    
    Returns:
        List[float]: A list of delays in ascending order.
    """
    tasks = []
    
    for _ in range(n):
        tasks.append(task_wait_random(max_delay))

    completed_delays = await asyncio.gather(*tasks)
    
    result = []
    for delay in completed_delays:
        index = 0
        while index < len(result) and result[index] < delay:
            index += 1
        result.insert(index, delay)
    
    return result