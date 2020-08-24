
from re import search
import webbrowser as wb
import requests


def getResults(searchTerm):
    apiKey = "AIzaSyBr3GzNXwL3Ps31sGUNPYU1WQAw02Rldr0"
    url = f'https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=25&q={searchTerm}&key={apiKey}'
    headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
    r = requests.get(url, headers=headers)
    results = r.json()['items']
    ids = [val['id']['videoId'] for val in results]
    thumbnails = [val['snippet']['thumbnails']['medium']['url']
                  for val in results]
    titles = [val['snippet']['title'] for val in results]
    # print(ids, '\n', thumbnails, '\n', titles)

    return titles, ids, thumbnails

titles, ids, thumbnails = getResults(searchTerm)

def convToDictionary(titles,ids,thumbnails):
    results = []
    for i in range(len(titles)):
        results.append({
            "Title": titles[i],
            "SubTitle": 'Enter to Initiate Site',
            "IcoPath": thumbnails[i],
            "JsonRPCAction": {
                "method": openUrl,
                "parameters": [ids[i]],
                "dontHideAfterAction": False
            }

        })
    return results

def openUrl(ids):
    wb.open(f'https://www.youtube.com/watch?v={ids}')