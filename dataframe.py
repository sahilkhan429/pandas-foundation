import pandas as pd    # importing pandas as short name pd
data = {
    "name":["musa","mehran","ikram","azan","ahmad"],
    "age":[23,14,32,12,34],             #  simple data 
    "marks":[567,675,865,457,865],
    "city":["peshawar","islamabad","karachi","lahore","kohat"]
}
df = pd.DataFrame(data)   # converting data into pandas dataframe
print(df)   # printing dataframe
