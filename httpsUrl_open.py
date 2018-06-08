#!/user/bin/env python
# coding:utf8
__author__ = 'liyatao'
'''
https网址打开方法，并且忽略警告代码提示
'''
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning   # 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url="https://www.baidu.com"  #网址
html=requests.get(url,verify=False).content  #忽略证书错误
print(html)
