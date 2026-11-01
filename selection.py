import pandas as pd    # importing pandas as short name pd
data = {
    "name":["musa","mehran","ikram","azan","ahmad"],
    "age":[23,14,32,12,34],             #  simple data 
    "marks":[567,675,865,457,865],
    "city":["peshawar","islamabad","karachi","lahore","kohat"]
}
df = pd.DataFrame(data)   # converting data into pandas dataframe
print(df["name"])   # selectin the names column
print(df[["name","marks"]])  #selecting 2 coulmns will return dataframe
print(df.iloc[2])    #third studnt complete row
print(df.iloc[3,2])  #selectin th number student marks
print(df[0:3])       # selecting first three student
print(df[["name","city"]])    #names+cities
