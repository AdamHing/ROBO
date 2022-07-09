import asyncio 



async def main():
    print("hello world")
    task = asyncio.create_task(foo("text"))
    await asyncio.sleep(2)
    print("finished")


async def foo(text):
    print(text)
    await asyncio.sleep(5)

asyncio.run(main())