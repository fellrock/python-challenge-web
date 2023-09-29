import asyncio

async def print_items(items):
    wait_time = 1
    for item in items:
        await asyncio.sleep(wait_time)
        print(item)
        wait_time *= 2

# Test the function
asyncio.run(print_items(["a", "b", "c", "d"]))
