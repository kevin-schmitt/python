# example with parrallelision task require python 3.7
import asyncio
import time

loop = asyncio.get_event_loop()

async def slowDisplay(delay, msg):
    await asyncio.sleep(delay)
    print(msg)

async def main():
    task1 = loop.create_task(slowDisplay(1, 'task 1'))
    task2 = loop.create_task(slowDisplay(2, 'task 2'))

    print('Start ', time.strftime('%X'))

    await task1
    await task2

    print('Fin ', time.strftime('%X'))

# Python 3.7+
loop.run_until_complete(main())