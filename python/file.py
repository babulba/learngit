#!/usr/bin/env python
# -*- coding: utf-8 -*-

inFile=open("input.txt","r")
outFile=open("output.txt","w")
aLine=inFile.readline()
print aLine
for line in inFile:
    outFile.write(line)
inFile.close()
outFile.close()