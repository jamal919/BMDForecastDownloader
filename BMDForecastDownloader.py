#! /usr/env python
# -*- coding: utf-8 -*-
"""
BMDForecastDownloader.py

This script downloads the BMD forecast file using pyton library. The functionality
is kept simple for now.

TODO - Do it in python way. 

AUTHOR - Jamal Uddin Khan
EMAIL - jamal919@gmail.com
LICENSE - LGPL
"""

import urllib
import datetime
from bs4 import BeautifulSoup
urllib.URLopener().retrieve("http://bmd.gov.bd/?/p/=Weather-Forecast", "bmd.txt")
f = open('bmd.txt', 'r')
soup = BeautifulSoup(f.read(), 'html.parser')
downurl = soup.find("div", {"class": "myIframe iframeWait"}).get('src').split("=")[1].split("&")[0]
filename = u"bmd_" + unicode(datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")) + u".pdf"
urllib.urlretrieve(downurl, filename)