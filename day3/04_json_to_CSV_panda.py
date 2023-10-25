import pandas as pd
import json

with open("simple.json","r") as json_file:
    json_data=json.load(json_file)


df=pd.DataFrame(json_data,index=[0])
df.to_csv('simple.csv',index=False)
