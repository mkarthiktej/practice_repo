import pandas as pd

data = pd.read_excel(r'C:\Users\91988\OneDrive\Desktop\Karthikxls\KarthikBook1.xlsx')
df = pd.DataFrame(data)
df = pd.DataFrame(data, columns=['Name', 'Age'])
# first_row = df.loc[:2]
print(df.info())
# print(first_row, end="")
# df = data.list[]
# print(data)

