from wox import Wox, WoxAPI
import webbrowser as wb
import requests


class Main(Wox):

    def query(self, key):
        return self.convToDictionary(self.getResults(key))

    def getResults(self, searchTerm):
        apiKey = "AIzaSyBr3GzNXwL3Ps31sGUNPYU1WQAw02Rldr0"
        url = f'https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=25&q={searchTerm}&key={apiKey}'
        headers = {'content-type': 'application/json',
                   'Accept-Charset': 'UTF-8'}
        r = requests.get(url, headers=headers)
        results = r.json()['items']
        ids = [val['id']['videoId'] for val in results]
        thumbnails = [val['snippet']['thumbnails']['medium']['url']
                      for val in results]
        titles = [val['snippet']['title'] for val in results]
        # print(ids, '\n', thumbnails, '\n', titles)

        return titles, ids, thumbnails

    def convToDictionary(self, titles, ids, thumbnails):
        results = []
        for i in range(len(titles)):
            results.append({
                "Title": titles[i],
                "SubTitle": 'Enter to Initiate Site',
                "IcoPath": thumbnails[i],
                "JsonRPCAction": {
                    "method": 'openUrl',
                    "parameters": [ids[i]],
                    "dontHideAfterAction": False
                }

            })
        return results

    def openUrl(self, ids):
        wb.open(f'https://www.youtube.com/watch?v={ids}')


if __name__ == "__main__":
    Main()
