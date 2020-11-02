import requests
import psutil
r = requests.get('https://baidu.com')
print(r.status_code, r.encoding)

print(psutil.cpu_count())
