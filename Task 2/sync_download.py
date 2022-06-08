import requests
import time
import json

url = 'https://xkcd.com/{}/info.0.json'

start = time.time()

for i in range(1, 201):
    print('Working on comic_id {}'.format(i))
    response = requests.get(url.format(i))

    # For saving in .txt file format 
    with open('task2_sync.txt', 'a') as f:
        f.write(str(response.json()) + "\n")

    # # For saving in .json file format (if requred)
    # with open('task2_sync.json', 'a') as f:
    #     json.dump(response.json(), f)


print('Successfully saved all files in task2_sync')
time_taken = time.time() - start
print('Time Taken: {}'.format(time_taken))
# Completed in 72.19 sec (average)
# Lowest - 65.82 sec
# Worst - 87.29 sec