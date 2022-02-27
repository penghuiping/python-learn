# coding=utf-8
import asyncio

async def run():
    print(1)
    await asyncio.sleep(5)
    print(2)

async def run1():
    print("3")


async def main():
    task = asyncio.create_task(run())
    task1 = asyncio.create_task(run1())
    await task
    await task1


asyncio.run(main())
