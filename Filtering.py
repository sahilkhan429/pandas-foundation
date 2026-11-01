import pandas as pd    # importing pandas as short name pd
data = {
    "name":["musa","mehran","ikram","azan","ahmad"],
    "age":[23,14,32,12,34],             #  simple data 
    "marks":[567,675,865,457,865],
    "city":["peshawar","islamabad","karachi","lahore","kohat"]
}
df = pd.DataFrame(data)   # converting data into pandas dataframe

print(df[df["marks"]>=600])   #marks greater or equal to 600
print(df[df["age"]>=25])      #age greater or eqaul to 25
print(df[df["city"]=="karachi"]) #city is equal to karachi
print(df[(df["age"]<30)&(df["marks"]>500)])  # age less than 30 and got greater than 500 marks
print(df[(df["city"]=="peshawar")|(df["city"]=="punjab")])  #printing one of them punjab or peshawar peshawar will be printed because peshawar is in data
print(df[df["age"].between(15,30)])    # age between 15 to 30
print(df[df["marks"]>500][["name","marks"]])  #only print name and marks whose marks is greater than 500
