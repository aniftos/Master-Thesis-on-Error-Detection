# Merge all timeseries datasets from all the participants into a single file "timeseries_dataset.csv"

import pandas as pd 
import os

# Create some variables
df_list = []
f=0
timeseries = list()
myFolders = list()
first=True



for file in os.listdir("C:/Users/George/Desktop/Participants/ffmpeg_try/"):
	if '.' not in file:
		myFolders.append(file)

myFolders.sort()

# Get into every participants folder and merge all the .csv files
for folder in myFolders:
	for subfolder in os.listdir("C:/Users/George/Desktop/Participants/ffmpeg_try/"+folder):
		if '.' not in subfolder:#
			for file in os.listdir("C:/Users/George/Desktop/Participants/ffmpeg_try/"+folder+"/"+subfolder):
				if 'time_series' in file:
					f+=1
					print("file no: ",f, "filename: ",folder,subfolder,file)

					if(first==True):
						df = pd.read_csv("C:/Users/George/Desktop/Participants/ffmpeg_try/"+folder+"/"+subfolder+"/"+file, index_col=0)
						y=df.iloc[0,70]
						df = df.drop(['70'],axis=1)
						horizondaldf=df.iloc[0:1]
						for i in range(df.shape[0]-1):
							i+=1
							row=df.iloc[i:i+1]
							row.reset_index(drop = True,inplace=True)
							horizondaldf=pd.concat([horizondaldf,row],axis=1)
						first=False
						horizondaldf['label']=y
						
					else:
						df_tmp = pd.read_csv("C:/Users/George/Desktop/Participants/ffmpeg_try/"+folder+"/"+subfolder+"/"+file, index_col=0)
						y=df_tmp.iloc[0,70]
						df_tmp = df_tmp.drop(['70'],axis=1)
						tappend=df_tmp.iloc[0:1]
						for i in range(df_tmp.shape[0]-1):
							i+=1
							row=df_tmp.iloc[i:i+1]
							row.reset_index(drop = True,inplace=True)
							tappend=pd.concat([tappend,row],axis=1)
						tappend['label']=y
						horizondaldf = horizondaldf.append(tappend)
					

# Print the final merged csv file (timeseries_dataset.csv)
horizondaldf.to_csv("C:/Users/George/Desktop/Participants/ffmpeg_try/timeseries_dataset.csv", index =False)
print("THE END")