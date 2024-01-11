
import pandas as pd
import os

# // Creates directory path for Excel file//
path = os.path.dirname(__file__)

# // data from Excel file
df_chem = pd.read_excel(path + "/data_sheets/course_schedule.xlsx", sheet_name="chemistry")
print(df_chem)

df_bio = pd.read_excel(path + "/data_sheets/course_schedule.xlsx", sheet_name="biology")
print(df_bio)

df_hist = pd.read_excel(path + "/data_sheets/course_schedule.xlsx", sheet_name="UsHistory")
print(df_hist)

df_world_hist = pd.read_excel(path + "/data_sheets/course_schedule.xlsx", sheet_name="WorldHistory")
print(df_world_hist)











