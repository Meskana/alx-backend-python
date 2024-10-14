#!/usr/bin/env python3
"""
async routine called wait_n that takes in 2 int arguments (in this order):
n and max_delay. You will spawn wait_random n times with the specified max_delay
"""


import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    delays = []
    for _ in range(n):
      
        delays.append(asyncio.create_task(wait_random(max_delay)))
    

    completed_delays = await asyncio.gather(*delays)
    result = []
    for delay in completed_delays:
        index = 0
        while index < len(result) and result[index] < delay:
            index += 1
        result.insert(index, delay)
    
    return result
