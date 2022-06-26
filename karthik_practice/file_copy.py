import shutil
from datetime import datetime
import os
import pandas as pd

time_stamp = datetime.now()
print(time_stamp.minute)
print(time_stamp)
source = r'C:\Users\91988\Desktop\Test_data.xlsx'
destination = r'C:\Users\91988\Desktop\Test_results\Test_data_' + str(time_stamp.month) + "_" + str(
    time_stamp.day) + "_" + str(time_stamp.year) + "_" + str(time_stamp.hour) + "_" \
              + str(time_stamp.minute) + "_" + str(time_stamp.second) + '.xlsx'
print(destination)
os.makedirs(os.path.dirname(destination), exist_ok=True)

df1 = pd.read_excel(io="C:/Users/91988/Desktop/Test_data.xlsx",sheet_name="Sheet1")
df2 = pd.read_excel(io="C:/Users/91988/Desktop/Test_data.xlsx",sheet_name="Sheet2")
header_length=len(df1.columns)


df1["Test Results"]=""
print(df1.columns)


df1.to_excel(destination,sheet_name="Sheet1")

shutil.copyfile(source, destination)