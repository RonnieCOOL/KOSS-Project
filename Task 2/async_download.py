import asyncio
import aiohttp
import time
import json

def download_files(session, url):
    tasks = []
    for i in range (1, 201):
        tasks.append(session.get(url.format(i)))
    return tasks

async def main():
    url = 'https://xkcd.com/{}/info.0.json'
    async with aiohttp.ClientSession() as session:
        tasks = download_files(session, url)
        responses = await asyncio.gather(*tasks)

        # For saving in .txt file format
        with open('task2_async.txt', 'a') as f:
            for response in responses:
                f.write(str(await response.json())+"\n")

        # For solving in .json file format
        # with open('task2_async.json', 'a') as f:
        #     for response in responses:
        #         json.dump(await response.json(), f)


start = time.time()

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())
print("Successfully saved all files in task2_async")
time_taken = time.time() - start
print("Time Taken: {} sec(s)".format(time_taken))
# Completed in 0.9513 sec (average)
# Best - 0.599 sec
# Worst - 1.48 sec