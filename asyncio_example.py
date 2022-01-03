import time
import asyncio


def count(i):
    print(f"[{i}] Start")
    time.sleep(1)
    print(f"[{i}] Finish")


async def async_count(i):
    print(f"[{i}] Start")
    await asyncio.sleep(1)
    print(f"[{i}] Finish")


async def async_gather():
    tasks = []
    for i in range(20):
        tasks.append(asyncio.create_task(async_count(i)))
    await asyncio.gather(*tasks)


def main_2():
    asyncio.run(async_gather())


def main_1():
    for i in range(20):
        count(i)


if __name__ == "__main__":
    s = time.time()
    # main_1()
    main_2()
    elapsed = time.time() - s
    print(f"Executed in {elapsed:0.2f} seconds.")
