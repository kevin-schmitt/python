# example with parrallelision task require 3.7
import asyncio
import time

async def slowDisplay(delay, msg):
    await asyncio.sleep(delay)
    print(msg)

async def main():
    task1 = asyncio.create_task(slowDisplay(1, 'task 1'))
    task2 = asyncio.create_task(slowDisplay(2, 'task 2'))

    print('Démarrage ', time.strftime('%X'))

    await task1
    await task2

    print('Fin ', time.strftime('%X'))

# Python 3.7+
asyncio.run(main())