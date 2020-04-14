#!/usr/bin/python
# Author:   @BlankGodd

import time, sys
from pyfiglet import Figlet


banner = Figlet(font='gothic')
print(banner.renderText(BlOs-0.01))

starting = 'Starting:[          ]'
for i in range(103):
    time.sleep(0.1)
    if i < 101:
        sys.stdout.write('\r' + starting + '{0}%'.format(i))
    else:
        sys.stdout.write('\r' + starting + '100%')
    if i==10 or i==20 or i==30 or i==40 or i==50 or i==60 or i==70 or \
    i==80 or i==90 or i==100:
        starting = starting.replace(' ',':',1)
    sys.stdout.flush()



