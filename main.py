from wox import Wox, WoxAPI
import webbrowser as wb


class Main(Wox):

    def query(self, key):
        results = []
        results.append({
            "Title": "Hello world",
            "SubTitle": 'Enter to Initiate Site',
            "IcoPath": "images\\music.ico",
            "JsonRPCAction": {
                "method": "openUrl",
                "parameters": [key],
                "dontHideAfterAction": False
            }
        })

        return results

    def openUrl(self, url):
        pass


if __name__ == "__main__":
    Main()
