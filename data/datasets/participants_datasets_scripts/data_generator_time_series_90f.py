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
finished=True

for fold in range(sinolo):
    count=fold+1
    if count<=e:
        counte=str(count)
        dir_path = os.path.dirname(os.path.realpath("C:/Users/George/Desktop/Participants/ffmpeg_try/part"+str(part)+"_errors/p"+str(part)+"_e"+counte+"/displacement.csv"))
    elif count>e and count<=(ne+e):
        countne=str(count-e)
        dir_path = os.path.dirname(os.path.realpath("C:/Users/George/Desktop/Participants/ffmpeg_try/part"+str(part)+"_errors/p"+str(part)+"_ne"+(countne)+"/displacement.csv"))
    else:
        countu=str(count-ne-e)
        dir_path = os.path.dirname(os.path.realpath("C:/Users/George/Desktop/Participants/ffmpeg_try/part"+str(part)+"_errors/p"+str(part)+"_u"+countu+"/displacement.csv"))

    print(dir_path)

    #-------------------READ THE DISPLACEMENT FILE WITH THE ORIGINAL LENGTHS-----------------
    originaldata_df = pd.read_csv(dir_path+"\displacement.csv",index_col=0)
    y=originaldata_df.iloc[0,70]
    print("data shape original =",originaldata_df.shape)
    reloop=False
    #originaldata_df = originaldata_df.drop(['70'],axis=1)

    #---------------------INPUT VARIABLES--------------------------------------
    arr = originaldata_df.values
    video=1
    row_size=np.size(arr,0) #input file rows
    r=row_size

    totalfr=int(row_size/30)*30
   
    ipolipo=row_size%30 #to see if we are undersampling or oversampling!! We need pollaplasio tou 30 arithmo frame!!

    if ipolipo>10:
        totalfr+=30

    print("ipolipo: ",ipolipo)
    print("totalframes =",totalfr)
    #blabla

    #--------------------------------OVERSAMPLING AND UNDERSAMPING PROCEDURE-------------------------------------#

    #--Discard if you have low number of frames, less than 46---#
    if row_size<46:
        reloop=True
        finished=False

    #--Oversample to get to 90 frames which is the baseline--#
    if row_size<71 and reloop==False:
        difference=90-row_size #35
        print("empika damee ksanaaaa")
        row_size=row_size+difference
        ind=int(r/difference)
        #ind_num=int(r/ind)
        ind_num=difference
        print("ind =",ind)
        print("ind_num =",ind_num)
        transpose=originaldata_df.T
        offset=0
        for times in range(ind_num):
            times+=1
            indx=ind*times #39
            print("indx = ", indx)
            inrow=originaldata_df[indx-1:indx].T
          #  print(inrow.shape)
            transpose.insert((indx+offset),""+str(times),inrow)
            print("Transpose size = ", transpose.shape)
            offset+=1
        originaldata_df=transpose.T
        originaldata_df=originaldata_df.reset_index(drop = True)
        finished=False

    #--Undersample to get to pollaplasio tou 30--#
    if ipolipo <= 10 and ipolipo!= 0 and finished==True:
        print("ASEGASDGASDGA")
        extra=ipolipo
        row_size=row_size-extra
        print(row_size)
        ind=int(r/extra)
        ind_num=int(r/ind)
        print("ind =",ind)
        print("ind_num =",ind_num)
        offset=1
        for times in range(ind_num):
            times+=1
            indx=ind*times-offset
            print(indx)
            originaldata_df = originaldata_df.drop([indx])
            originaldata_df = originaldata_df.reset_index(drop = True)
            offset+=1
            print("check!!!")
    #--Oversample to get to pollaplasio tou 30--#
    elif ipolipo > 10 and finished==True:
        print("empika damee")
        extra=(30-ipolipo)
        row_size=row_size+extra
        print(row_size,r)
        ind=int(r/extra)
        #ind_num=int(r/ind)
        ind_num=extra
        print("ind =",ind)
        print("ind_num =",ind_num)
        transpose=originaldata_df.T
        offset=0
        for times in range(ind_num):
            times+=1
            indx=ind*times #39
            print("indx = ", indx)
            inrow=originaldata_df[indx-1:indx].T
          #  print(inrow.shape)
            transpose.insert((indx+offset),""+str(times),inrow)
            print("Transpose size = ", transpose.shape)
            offset+=1
        originaldata_df=transpose.T
        originaldata_df=originaldata_df.reset_index(drop = True)

    finished=True
    exactly=True

    print(originaldata_df.shape)

    #------------SAVE THE NEW DATA IN SCV FILES WITH SIZE OF 90 FRAMES EACH!!!!--------------#

    frows=originaldata_df.shape[0] #finished rows
    if(frows)>90:
        video=int((frows/30)-2)
        exactly=False
        for countt in range(video):
            n=countt*30
            s_to_f=originaldata_df[n:(n+90)]
           # s_to_f = s_to_f.drop(['0'],axis=1)
            s_to_f=s_to_f.reset_index(drop = True)
            s_to_f.to_csv(dir_path+'/time_series'+str(countt+1)+'.csv')

    if exactly==True and reloop==False:
       originaldata_df.to_csv(dir_path+'/time_series1.csv')



    #     diff=90-row_size
    #     new=np.zeros((video,col_size))
    #     print(new.shape)
    #     print("videos =",video)
    # elif(row_size)>90:
    #     video=int(row_size/30-2)
    #     new=np.zeros((video,col_size))
    #     print(new.shape)
    #     print("videos =",video)
    # zsdg

    # X=row_size-90


    # new=np.zeros((X,col_size))

    # measure=row_size-90

    # if measure == 0:
    #     asaf
    # elif measure >0:
    #     asdgfas
    # else:
    #     asdgasdg

    #originaldata_df.to_csv(dir_path+'/time_series.csv')
    
    
   # print(transpose.T)
        




'''

    asd


    if(row_size)<=90:
        diff=90-row_size
        new=np.zeros((video,col_size))
        print(new.shape)
        print("videos =",video)
    elif(row_size)>90:
        video=int(row_size/30-2)
        new=np.zeros((video,col_size))
        print(new.shape)
        print("videos =",video)
    zsdg

    X=row_size-90


    new=np.zeros((X,col_size))

    measure=row_size-90

    if measure == 0:
        asaf
    elif measure >0:
        asdgfas
    else:
        asdgasdg



    for i in range(rows_size):
        n=0
        for j in range(col_size):
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

    new.to_csv(dir_path+'/time_seiries.csv')
'''