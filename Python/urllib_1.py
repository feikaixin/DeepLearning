from urllib import request
from urllib import parse
import random

# request的用法
ag_list = [
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
  "Mozilla/5.0 (Windows NT 6.1; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
  "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
  "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
]
user_agent = random.choice(ag_list)
request_obj1 = request.Request('https://www.baidu.com', headers={'User-Agent': user_agent})
response = request.urlopen(request_obj1)
html = response.read().decode('utf-8')
print(html)
# 获取响应状态码
print(response.getcode())
# 返回服务器响应信息头
print(response.info())
# 返回返回实际数据的url，防止重定向问题
print(response.geturl())




# parse的用法
url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action="
# 构造访问头信息
headers = {
	"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
}
# 构造请求数据
form_data = {
    "start": "0",
    "limit": "10",
}
data = parse.urlencode(form_data).encode('utf-8')
request_obj2 = request.Request(url, data=data, headers=headers)
json = request.urlopen(request_obj2).read().decode('utf-8')
print(json)








