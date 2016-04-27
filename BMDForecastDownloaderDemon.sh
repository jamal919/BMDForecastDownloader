#!/bin/bash

setsid /usr/bin/python BMDForecastDownloader.py > download.log 2>&1 < download.log &