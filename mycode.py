import pandas as pd
import os

data = {
    'Name': ['Tushar ', 'Vansh', 'kush'],
    'Age': [20, 21, 19],
    'City': ['Delhi', 'Noida', 'Agra']
}

df = pd.DataFrame(data)

new_row = {'Name': 'Ankit', 'Age': 22, 'City': 'Mumbai'}
df.loc[len(df.index)] = new_row

new_row = {'Name': 'Anshul', 'Age': 22, 'City': 'Mussoorie'}
df.loc[len(df.index)] = new_row

data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir, 'data.csv')
df.to_csv(file_path, index=False)
print(f"DataFrame saved to {file_path}")
print(df)