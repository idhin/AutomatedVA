#!/usr/bin/env python
import time
from zapv2 import ZAPv2

# Target URL
target = 'https://maresto.id/'
# Silahkan Ganti APIKey Sesuai dengan apps OWASP ZAP
apiKey = 'va102dj53le10nl12c7ec1d5em'

# By default ZAP API client will connect to port 8080
zap = ZAPv2(apikey=apiKey)
# Use the line below if ZAP is not listening on port 8080, for example, if listening on port 8090
# zap = ZAPv2(apikey=apiKey, proxies={'http': 'http://127.0.0.1:8090', 'https': 'http://127.0.0.1:8090'})

print('Ajax Spider target {}'.format(target))
scanID = zap.ajaxSpider.scan(target)

timeout = time.time() + 60*2   # 2 minutes from now
# Loop until the ajax spider has finished or the timeout has exceeded
while zap.ajaxSpider.status == 'running . . .':
    if time.time() > timeout:
        break
    print('Status: ' + zap.ajaxSpider.status)
    time.sleep(2)

print('Running Completed')
ajaxResults = zap.ajaxSpider.results(start=0, count=10)

# TODO: Start scanning the application to find vulnerabilities
