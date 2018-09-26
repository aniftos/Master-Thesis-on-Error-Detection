# Merge all original datasets from all the participants into a single file "originaldata_dataset.csv"

import pandas as pd 
import os
df_list = []

myFolders = list()
for file in os.listdir("C:/Users/George/Desktop/Participants/ffmpeg_try/"):
	if '.' not in file:
		myFolders.append(file)

myFolders.sort()


first=True
for folder in myFolders:
	for subfolder in os.listdir("C:/Users/George/Desktop/Participants/ffmpeg_try/"+folder):
		if '.' not in subfolder:#
			for file in os.listdir("C:/Users/George/Desktop/Participants/ffmpeg_try/"+folder+"/"+subfolder):
				if 'displacement' in file:
					if(first==True):
						df = pd.read_csv("C:/Users/George/Desktop/Participants/ffmpeg_try/"+folder+"/"+subfolder+"/displacement.csv", index_col=0)
						df['file'] = folder+"/"+subfolder+"/displacement.csv"
						first=False
					else:
						df_tmp = pd.read_csv("C:/Users/George/Desktop/Participants/ffmpeg_try/"+folder+"/"+subfolder+"/displacement.csv", index_col=0)
						df_tmp['file'] = folder+"/"+subfolder+"/displacement.csv"
						df = df.append(df_tmp)
						
#Print the final merged csv file (originaldata_dataset.csv)
df.to_csv("C:/Users/George/Desktop/Participants/ffmpeg_try/originaldata_dataset.csv", index =False)
print("THE END")