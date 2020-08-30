import requests
import re
import collections


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


    def getDomainName(self, url):
        domainPattern = re.compile(
            '(\w+)://(?P<domain>[\w\-\.]+)(:(\d+))?(/(.+))?')
        domainName = domainPattern.search(url[0]).group('domain')
        return domainName

    def getDomains(self):
        # return a dictionary with keys of domains and values of list of urls related to that doamin
        domainDic = collections.defaultdict(list)
        
        for url in self.urlList: 
            domainDic[self.getDomainName(url)].append(url)

        return domainDic

    def getAvgLoadTime(self):
        domainsDic = self.getDomains()
        domainLoadTimeDic = []
        # domainLoadTimeDic = collections.defaultdict(list)

        for domain in domainsDic.keys():
            urls = domainsDic[domain]
            count = len(urls)
            loadTimes = list(map(lambda url: requests.get(url[0]).elapsed.total_seconds(), urls))
            avgLoadTime = sum(loadTimes)/count
            domainLoadTimeDic.append((domain, avgLoadTime))

        return domainLoadTimeDic
