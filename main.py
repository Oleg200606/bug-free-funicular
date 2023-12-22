import pandas as pd

file_path = '/Users/oleg/Desktop/Питон практос/netflix_titles2.csv'
netflix_data = pd.read_csv(file_path)

netflix_data.head()


netflix_data['date_added'] = pd.to_datetime(netflix_data['date_added'], errors='coerce')


netflix_data['added_year'] = netflix_data['date_added'].dt.year
netflix_data['added_month'] = netflix_data['date_added'].dt.month


netflix_data['duration_min'] = netflix_data['duration'].str.extract('(\d+)').astype(float)





