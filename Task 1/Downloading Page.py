import asyncio
import aiohttp
import time


async def download(url):
    async with aiohttp.ClientSession() as session:
        response = await(session.get(url))
    return response


async def main():
    start = time.time()
    arr = [1, 2, 3]
    url = 'https://reqres.in/api/users?page{}'
    tasks = []
    for el in arr:
        tasks.append(download(url.format(el)))

#     await asyncio.gather(*tasks);

    time_taken = time.time() - start
    print('Time Taken {0}'.format(time_taken))

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())
# Completed in 0.18 sec (Average)
# Best - 0.14 sec
# Worst - 0.26 sec
