import sys
import random

def randomAlphaNumeric( length ):
    alphaNumeric = ''
    for i in range(0, length):
        alphaNumeric = alphaNumeric + random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
    return alphaNumeric

def addQuoteToFile( fullFilePath ):
	quotes = []
	textFile = open(fullFilePath, 'a')
	textFile.write(random.choice(quotes))
	textFile.close()

for i, arg in enumerate(sys.argv):
    if arg == '-about':
        print 'The Infinite Improbability Command Line is a command line interface (CLI) that performs'
        print 'basic functions and is used as an example program for UGUI to create a GUI for.'
        print 'IICL is created in Python by Hai Nguyen.'
    if arg == '-random':
        print randomAlphaNumeric(int(sys.argv[i + 1]))
    if arg == '-quote':
    	addQuoteToFile(sys.argv[i + 1])
