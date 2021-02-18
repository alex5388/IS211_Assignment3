import csv
import argparse
import re
from urllib import request

url = 'http://s3.amazonaws.com/cuny-is211-spring2015/weblog.csv'

fileOpen = request.urlopen(url)
readFile = fileOpen.read()
decFile = readFile.decode('ascii').split('\n')
for line in decFile:
    print(line)

x = re.findall("\.jpg|\.JPG", str(decFile))
y = re.findall("\.gif|\.GIF", str(decFile))
z = re.findall("\.png|\.PNG", str(decFile))

totalJPG = len(x)
totalGIF = len(y)
totalPNG = len(z)
print(f"Total .jpg images is {totalJPG}")
print(f"Total .gif images is {totalGIF}")
print(f"Total .png images is {totalPNG}")
