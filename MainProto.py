##########################################################
#
# Proto script in the LifeOfBlacklists project
# Auth : 100397963
# Version : 1.01
# Embedded Functionality:
#   - Extraction of content from a statically defined url
#   - Saving of content in file
#
##########################################################

# Library imports

import csv
import os
import urllib.request
import datetime

# Globals

currDay = datetime.datetime.now().strftime("%Y-%m-%d")
path = os.path.realpath(__file__).split("MainProto")[0]

# Url list import

def importUrls():

    importPath = path + '\Resources\\blacklistList.csv'
    results = []
    with open(importPath) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            results.append(str(row)[2:-2])
    return results

# Url entry parsing
# ToDo

def validEntry(string):

    if len(string) == 0: return 1
    if string[0] == '#': return 1
    if string[0] == '-': return 1
    if string[0] == '$': return 1
    if string[0] == '\"': return 1
    if string[0] == '/': return 1

    return 0

# Content extraction from urls

def getContents(url):
    contents = urllib.request.urlopen(url).read()
    decoded = contents.decode("utf-8")
    decodedArray = decoded.split("\n")

    # Conversion and saving

    dirPath = path + 'Outputs'

    if not os.path.isdir(dirPath):
        os.mkdir(dirPath)

    testFile = open(dirPath + '\\File1.txt', "a+")
    for entry in decodedArray:
        if validEntry(entry):
            testFile.write(entry + ';' + url + ';' + currDay + '\n')
    return

# Program Main Flow
url = importUrls()

for entry in url :
    getContents(entry)


