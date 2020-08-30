import requests


class UrlHandler:
    """
    A class to handle interaction with a list of URLs. It includes methods for calculating the response body size from GET requests, displaying all the domains found in the URLs along with the average load time for the URLs of that domain
    """

    def __init__(self, urlList):
        super().__init__()
        self.urlList = urlList

    def getRequestSize(self):

        byteSizeList = []

        try:

            for url in self.urlList:
                print('url is :', url)
                address = url[0]
                res = requests.get(address)
                byteSize = len(res.content)
                byteSizeList.append((address, byteSize))

            return byteSizeList

        except requests.exceptions.RequestException as e:
            raise SystemExit(e)


    # def getAvgPageLoadTime(self, url):
