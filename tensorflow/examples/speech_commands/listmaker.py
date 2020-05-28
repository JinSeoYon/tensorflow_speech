



import os

path = "/Users/sheoyonjin/Desktop/crying_data_all_16wav/"
name_list =["burping2/","discomfort2/","hungry2/","tired2/","bellypain2/"]
f = open(path+"testing_lis22222.txt",'w')
for i in range(5):
    file_list=os.listdir(path+name_list[i])

    length_list = len(file_list)
    for j in range(length_list):
        print(file_list[j])
        word = name_list[i]+file_list[j]+"\n"
        f.write(word)

