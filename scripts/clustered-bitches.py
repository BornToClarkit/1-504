import pandas as pd
from csv import reader, writer
import hdbscan
import os
directory = os.fsencode("data/1/")

for file in os.listdir(directory):
	filename = os.fsdecode(file)
	dataframe =pd.read_csv("data/1/"+filename,sep=",",index_col=[0,13,6,7,8,9,10,11,12])
	clusterer = hdbscan.HDBSCAN()
	clusterer.fit(dataframe)
	print("file name: "+filename + " clusters: "+str(clusterer.labels_.max()))
	out = writer(open("data/clusters/clusters1.csv","a"),delimiter=",")
	out.writerow(clusterer.labels_)
