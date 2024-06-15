# Hello Diego, sorry I messed up the other one.
# I think I know how to use git now tho.
#testing git pull and git fetch
#testing git pull and git fetch pt2
import numpy as np
import pandas as pd
import matplotlib.pyplot as mpl

chris = "que guey"

print(chris)
print("\nello wurld")

id_number_list = []
amount_list = []
category_list = []
frequency_list = []
time_list = []
rating_list = []

#making the default dataframe
data = {"id number": id_number_list, "amount": amount_list, "category": category_list, "frequency": frequency_list, "time": time_list, "rating": rating_list}
default_template =  pd.DataFrame(data)
print(default_template)

#adding testing file and making a list with the column names for the user file and for the default file
bankfile = pd.read_csv("Test CSV.csv")
print(bankfile.head())
user_mapping_fields = list(bankfile.columns)
default_mapping_fields = list(default_template.columns)

combined_mapping_list = []

print("\nAvailable columns to map:\n")
print("User fields: ", user_mapping_fields)
print("System fields:  ", default_mapping_fields)

print("\nHow do you want to map your fields? Type the system field name you want to map to.")

user_correct_mapping = "n"

#looping through the column names in the user file until it is empty
while user_correct_mapping == "n":
  while len(user_mapping_fields) > 0:
    system_field_selection = input(f'\nMap "{user_mapping_fields[0]}" to which system field?\n').strip().lower()
  
    #checking if the user input is a column name or not
    #"none" is an option and will be treated as an empty value
    if system_field_selection not in default_mapping_fields:
      if system_field_selection == "none":
        pass
      else:
        print("\nThat field is not available. Please select a field from the following list:\n")
        print(*default_mapping_fields, sep = ", ")
        continue
    if system_field_selection in default_mapping_fields:
      default_mapping_fields.remove(system_field_selection)
      
    #a list is made for each map, then each list is added into a combined list
    new_list = [system_field_selection, user_mapping_fields.pop(0)]
    combined_mapping_list.append(new_list)
  
    if len(default_mapping_fields) == 0:
      break
  
  #adding "none" to any system field that did not have a mapping
  for i in range(len(default_mapping_fields)):
    combined_mapping_list.append([default_mapping_fields[i], "none"])
  
  #gets rid of any mappings in combined_mapping_list that are mapped to "none"
  combined_mapping_list = [field for field in combined_mapping_list if "none" not in field]
 
  #if this is correct, continue. If the mapping is wrong, then restart
  print("\nIs the following correct? (y/n)")
  print(str(combined_mapping_list)[1:-1] + "\n")
  user_correct_mapping = input().strip().lower()
  if user_correct_mapping == "n":
    combined_mapping_list = []
    user_mapping_fields = list(bankfile.columns)
    default_mapping_fields = list(default_template.columns)
    continue

  if user_correct_mapping == "y":
    break

  else:
    user_correct_mapping = "n"
    print("That is not a valid input. Please try again.")
    
#adds the info from the user's file into the mapped default field
while len(combined_mapping_list) > 0:
  individual_mappings = combined_mapping_list.pop(0)
  default_column = individual_mappings[0]
  user_column = individual_mappings[1]
  default_template[default_column] = bankfile[user_column]

print("\ndefault:\n", default_template)
print("bankfile:\n", bankfile)
print("combined:\n", combined_mapping_list)

print("combined mapping list: ", combined_mapping_list)
print("user fields: ", user_mapping_fields)
print("default fields: ", default_mapping_fields)



#######
# Data manipulation part starts here
#######

# getting rid of the unmapped columns
default_template = default_template.dropna(axis=1, how='all')
print("graph this: \n", default_template)

# Create a bar chart
rating_graph = default_template['rating']
id_number_graph = default_template['id number']
# figure size
fig1 = mpl.figure(figsize = (10,7))
# horizontal bar plot
mpl.bar(rating_graph, id_number_graph)
mpl.show()
