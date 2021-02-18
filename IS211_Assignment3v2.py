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

m = re.findall("Mozilla", str(decFile))
c = re.findall("Chrome", str(decFile))
#i = re.findall("Internet Explorer", str(decFile))
s = re.findall("Safari", str(decFile))

print(len(m))
print(len(c))
#print(i)
print(len(s))
totalJPG = len(x)
totalGIF = len(y)
totalPNG = len(z)
totalImg = len(x) + len(y) + len(z)

print(f"Total .jpg images is {totalJPG}")
print(f"Total .gif images is {totalGIF}")
print(f"Total .png images is {totalPNG}")

totalDecfile = len(decFile)
div = totalImg/totalDecfile * 100
print("Image requests account for {:.1f}% of all requests".format(div))