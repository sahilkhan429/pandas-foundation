import pandas as pd   #importing pandas with short name pd
ages = pd.Series([22,32,43,23],index=["sahil","hamza","salar","ali"])   #converting python simple list into a pandas series with custome index
print(ages)  #printing ages