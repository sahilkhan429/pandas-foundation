import pandas as pd    # importing pandas as short name pd
data = {
    "name":["musa","mehran","ikram","azan","ahmad"],
    "age":[23,14,32,12,34],             #  simple data 
    "marks":[567,675,865,457,865],
    "city":["peshawar","islamabad","karachi","lahore","kohat"]
}
df = pd.DataFrame(data)   # converting data into pandas dataframe
print("info:",df.info())   #gives information
print("head:",df.head(3))  #first 3 rows
print("tail:",df.tail(2))  #last 2 rows
          
print("shape:",df.shape)     # printing dataframe's shape
print("columns:",df.columns)   # printing dataframe all columns names
print("types:",df.dtypes)    # type of each column
print("describe:",df.describe)
print(df["marks"].shape)