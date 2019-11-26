# coding=utf-8
import asyncio


async def incr():
    await asyncio.sleep(5)
    print(3)


async def run():
    print(1)
    await incr()
    print(2)


asyncio.run(run())
