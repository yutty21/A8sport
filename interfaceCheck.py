import urllib.request
import urllib.parse
import readTXT


#url = "http://test.api.a8tiyu.com/right/news/news_html"
#word = {"nid":"83baa6fb5c028b34440467c56630ecd6"}
#word = urllib.parse.urlencode(word) #转换成url编码格式（字符串）
#newurl = url + "?" + word    # url首个分隔符就是 ?
count = 0
var =(r'\Users\yutty\Desktop\ReadUrl.txt')
headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}

interList = readTXT.readtxt(var)

while count<len(interList):
    url = interList[count]
    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)
    print(url)
    print(response.getcode())
    print(response.read().decode())
    count = count + 1








