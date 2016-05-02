# -*- coding: utf-8 -*-
# @Date    	: 2016-04-21 12:54:46
# @Author  	: mr0cheng
# @email	: c15271843451@gmail.com

import urllib
from urllib import parse,request

r=urllib.request.urlopen('http://www.lu2396.com/index.php').read()
print(r)