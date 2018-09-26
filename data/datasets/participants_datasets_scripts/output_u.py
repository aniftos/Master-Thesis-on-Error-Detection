import json
import os
import csv
part=1
e=7
ne=11
u=4
for fold in range(u):
    count=str(fold+1)
    dir_path = os.path.dirname(os.path.realpath("C:/Users/George/Desktop/Participants/ffmpeg_try/part"+str(part)+"_errors/p"+str(part)+"_u"+count+"/result.avi"))

    # this finds our json files
    #print(os.path.abspath("output.py"))
    #print(os.getcwd())
    #wdir=os.getcwd()
    path_to_json = dir_path
    json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
    print(path_to_json)
    # here I define the columns I want to get assing to my csv file
    l=[]
    first=True
    k=1
    kk=1
    for j in range(141):
        
        if j==140:
            l.append("Label")
        else:
            if j % 2 ==0:
                l.append("Point X"+str(k))
                k+=1
            else:
                l.append("Point Y"+str(kk))
                kk+=1
            


    # here i read all .json files and assing the in one whole csv file!!
    for index, js in enumerate(json_files):
        with open(os.path.join(path_to_json, js)) as json_file:
            data = json.load(json_file)
            #print(data)
            for output in data['people']:
                desire = output['face_keypoints_2d']
                num=2
                for i in range(70):
                    del desire[num]
                    num=num+2

                desire.append(1)  # PUT THE CORRECT LABEL!!!!


                with open(path_to_json+"\original_data.csv","a", newline='') as thefile:
                    if first==True:
                        spamwriter = csv.writer(thefile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
                        spamwriter.writerow(l)
                        first=False

                    spamwriter = csv.writer(thefile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    spamwriter.writerow(desire)