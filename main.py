import pandas as pd
import json
import os

file_list=os.listdir("E:\\새 폴더\\수업\\3학년\\1학기\\로봇비전\\Data\\traindata\\training\\label")
json_list=os.listdir()

for i in file_list:
    json_list = os.listdir("E:\\새 폴더\\수업\\3학년\\1학기\\로봇비전\\Data\\traindata\\training\\label\\"+i)
    for j in json_list:
        with open("E:\\새 폴더\\수업\\3학년\\1학기\\로봇비전\\Data\\traindata\\training\\label\\"+i+"\\"+j, 'r', encoding='UTF8') as f:
            json_data = json.load(f)
            print(json_data)


