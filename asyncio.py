import asyncio

async def main():
    print('tim')
    task = asyncio.create_task(foo('text'))
    await asyncio.sleep(0.1)
    print('finished')

async def foo(text):
    print(text)
    await asyncio.sleep(1)

asyncio.run(main())
