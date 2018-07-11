import quandl
import time
import csv
f = open("tickers.txt","r")
tickersString = f.readline()
#print(tickersString)
tickers = tickersString.split(", ")
i=1
for ticker in tickers:
	stockdata = quandl.get("WIKI/"+ticker)
	stockdata.to_csv("data/"+str(i)+".csv", sep=',')
	i+=1
	print(i)
	time.sleep(3)
