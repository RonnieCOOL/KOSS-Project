import asyncio
import aiohttp
import time

async def download(url, arr):
    async with aiohttp.ClientSession() as session:
        for el in arr:
            print('Downloading Page {}'.format(el))
            response = await(session.get(url.format(el)))
            # print(await response.json()) #Can be used to print the contents of the page


async def main():
    arr = [1, 2, 3]
    url = 'https://reqres.in/api/users?page{}'

    start = time.time()
    await download(url, arr)
    time_taken = time.time() - start
    print('Time Taken {0}'.format(time_taken))

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())
# Completed in 0.25 sec (Average)
# Best - 0.14 sec
# Worst - 0.34 sec