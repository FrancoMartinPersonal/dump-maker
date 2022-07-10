
def urlRepoName(url):
    urlList = url.split('/')
    print(urlList, "urlList")
    return urlList[-1]
    