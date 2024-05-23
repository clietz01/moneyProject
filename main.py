# Hello Diego, sorry I messed up the other one.
# I think I know how to use git now tho.
#testing git pull and git fetch
#testing git pull and git fetch pt2
import numpy as np
import pandas as pd
import matplotlib as mpl

chris = "que guey"

print(chris)
print("\nello wurld")

id_number_list = [1, 2,3,4,5]
amount_list = [3,5,1,7,54]
category_list = [12,32,32,4,8]
frequency_list = [14,13,12,11,10]
time_list = [10,12,14,16,18]
rating_list = [90,100,102,119,130]

data = {"id number": id_number_list, "amount": amount_list, "category": category_list, "frequency": frequency_list, "time": time_list, "rating": rating_list}
default_template =  pd.DataFrame(data)
print(default_template)

#bankfile = str(input("Enter the path to your banking csv file: "))
#print(bankfile)
#pd.read_csv(bankfile)