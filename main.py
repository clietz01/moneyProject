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
bankfile = pd.read_csv("Test CSV.csv")
print(bankfile.head())
user_mapping_fields = list(bankfile.columns)
default_mapping_fields = list(default_template.columns)

combined_mapping_list = []

print("\nAvailable columns to map:\n")
print("User fields: ", user_mapping_fields)
print("System fields:  ", default_mapping_fields)

print("\nHow do you want to map your fields? Type the system field name you want to map to.")

while len(user_mapping_fields) > 0:
  system_field_selection = input(f'\nMap "{user_mapping_fields[0]}" to which system field?\n').strip().lower()
  
  if system_field_selection not in default_mapping_fields:
    if system_field_selection == "none":
      print("good")
    else:
      print("That field is not available. Please select a field from the list.")
      continue
  if system_field_selection in default_mapping_fields:
    default_mapping_fields.remove(system_field_selection)
  
  new_list = [system_field_selection, user_mapping_fields.pop(0)]
  combined_mapping_list.append(new_list)

for i in range(len(default_mapping_fields)):
  combined_mapping_list.append([default_mapping_fields[i], "none"])
default_mapping_fields = []

print(combined_mapping_list)
print("user fields: ", user_mapping_fields)
print("default fields: ", default_mapping_fields)
