import requests
from threading import Timer

api_token = None
url = "https://api.telegram.org/bot%s/" % api_token
latest_update_id = 0

def get_updates_json(url, latest_update_id):  
    params = {
        'timeout': 1000,
        'offset': latest_update_id + 1
    }
    response = requests.get(url + 'getUpdates', data=params)
    return response.json()

def last_update(data):  
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]

def printUpdates():
    global latest_update_id
    updates = get_updates_json(url, latest_update_id)['result']
    latest_update_id = updates[-1]['update_id'] if updates else latest_update_id
    print(updates)
    global timer
    timer = Timer(5.0, printUpdates)
    timer.start()

timer = Timer(5.0, printUpdates)
timer.start()
