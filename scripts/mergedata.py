import time
from csv import reader, writer
import os.path

f = open("tickers.txt","r")
tickersString = f.readline()

#print(tickersString)
tickers = tickersString.split(", ")
i=1
for ticker in tickers:
	data = list(reader(open("data/"+str(i)+".csv"),delimiter=","))
	data.pop(0)
	for row in data:
		print("file: " + str(i) +" date: " +row[0])
		out = writer(open("data/0/"+row[0]+".csv","a"),delimiter=",")
		out.writerow(row)
	i+=1
	

