



import os

path = "/Users/sheoyonjin/Desktop/data/"
name_list =["Dog/","_background_noise_/","BabyCry/","Chainsaw/","ClockTick/","FireCrackling/","Helicopter/","PersonSneeze/","Rain/","Rooster/","SeaWaves/"]
f = open(path+"data_list.txt",'w')
for i in range(11):
    file_list=os.listdir(path+name_list[i])

    length_list = len(file_list)
    for j in range(length_list):
        print(file_list[j])
        word = name_list[i]+file_list[j]+"\n"
        f.write(word)

