import asyncio

async def say_hello():
    print("Привет")
    await asyncio.sleep(1)
    print("Снова привет")

async def say_goodbye():
    print("Пока")
    await asyncio.sleep(2)
    print("Снова пока")

async def main():
    await asyncio.gather(say_hello(), say_goodbye(), say_hello())

asyncio.run(main())