import pandas as pd
import os
import numpy as np 
import math
# this finds our json files
part=1
e=7
ne=11
u=4
sinolo=e+ne+u

for fold in range(sinolo):
    count=fold+1
    if count<=e:
        counte=str(count)
        dir_path = os.path.dirname(os.path.realpath("C:/Users/George/Desktop/Participants/ffmpeg_try/part"+str(part)+"_errors/p"+str(part)+"_e"+counte+"/original_data.csv"))
    elif count>e and count<=(ne+e):
        countne=str(count-e)
        dir_path = os.path.dirname(os.path.realpath("C:/Users/George/Desktop/Participants/ffmpeg_try/part"+str(part)+"_errors/p"+str(part)+"_ne"+(countne)+"/original_data.csv"))
    else:
        countu=str(count-ne-e)
        dir_path = os.path.dirname(os.path.realpath("C:/Users/George/Desktop/Participants/ffmpeg_try/part"+str(part)+"_errors/p"+str(part)+"_u"+countu+"/original_data.csv"))

    print(dir_path)
    originaldata_df = pd.read_csv(dir_path+"\original_data.csv")
    arr = originaldata_df.values
    #print(type(arr))
	#print(pow(3,2))
	#print(arr.shape)
	#print(np.size(arr,0))
    #print(arr.shape)
    new_rows=np.size(arr,0)-1
    new=np.zeros((new_rows,71))
	#print(arr)
    #print("checkpoint")

    for i in range(new_rows):
        n=0
        for j in range(70):
           # print(n,arr[i][n])
            calc=pow((arr[i][n]-arr[i+1][n]),2)+pow((arr[i][n+1]-arr[i+1][n+1]),2)
            calc=math.sqrt(calc)

            new[i][j]=calc
            n+=2

    print("checkpoint_2")
    new = pd.DataFrame(new)
    if arr[0][140]==1:
        new[70]=1 #Label
    else:
        new[70]=0

    new.to_csv(dir_path+'\displacement.csv')
#a = np.arange(9).reshape(3,3)
#print(a)
#for i in range(3):
 #   for j in range(3):
 #       a[i][j]+=1
#        print(a[i][j])
    

#new= np.multiply(new_df,new_df)

#print(new)



"""
#new = np.zeros((5,1))
#print(new.shape)

#new_df = pd.DataFrame(arr)
#print(type(new_df))
#print(new_df.loc[2:5,138:])
#
#final=new_df.loc[2:5,138:]
#final.to_csv("testing.csv")
#new_df.to_csv('test.csv')

#print(originaldata_df['Point X1'].dtypes)
#print(originaldata_df.head(2))
"""