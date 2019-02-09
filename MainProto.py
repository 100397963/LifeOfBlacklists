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

currDay = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
path = os.path.realpath(__file__).split("MainProto")[0]

# Url list import

def importUrls():

    importPath = path + '\Resources\\blacklistList.csv'
    results = []
    with open(importPath) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            results.append(str(row)[2:-2].split(";"))
    return results

# Url entry parsing
# ToDo

def validEntry(string):

    if len(string) == 0: return 0
    if string[0] == '#': return 0
    if string[0] == '-': return 0
    if string[0] == '$': return 0
    if string[0] == '\"': return 0
    if string[0] == '/': return 0
    if string[0] == '<': return 0
    return 1

# Content extraction from urls

def getContents(url, filePath, category, index):

    #404 error protection
    try:
        contents = urllib.request.urlopen(url[0]).read()
        decoded = contents.decode("utf-8")
        decodedArray = decoded.split("\n")

        testFile = open(filePath + "\\" + str(index) + ".txt", "w+")
        for entry in decodedArray:
            if validEntry(entry):
                testFile.write(str((entry + ';' + url[0] + ';' + currDay + ';' + category + '\n').encode("utf-8")))
        return
    except:
        print("40x http error")
# Program Main Flow
url = importUrls()

# Conversion and saving

dirPath = path + 'Outputs'

if not os.path.isdir(dirPath):
    os.mkdir(dirPath)

dirPath = dirPath + '\\' + datetime.datetime.now().strftime("%Y-%m-%d")

if not os.path.isdir(dirPath):
    os.mkdir(dirPath)

category = ""
filePath = ""
index = 1

for entry in url:

    if not entry[1] == category:
        if not os.path.isdir(dirPath + "\\" + entry[1]):
            os.mkdir(dirPath + "\\" + entry[1])
        category = entry[1]
    filePath = dirPath + "\\" + entry[1]

    getContents(entry, filePath, category, index)
    print(index)
    index = index + 1



