"datetimeAPI"


from datetime import datetime

now = datetime.now()
print(now)

# 转换为毫秒数
timestamp = now.timestamp()

# 毫秒数转时间
datetime.fromtimestamp(timestamp) 

cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)