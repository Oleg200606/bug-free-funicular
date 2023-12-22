import pandas as pd
import matplotlib.pyplot as plt

from main import *



release_year_data = netflix_data['release_year']
duration_data = netflix_data['duration'].str.extract('(\d+)').astype(float)  


plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
plt.hist(release_year_data, bins=30, color='skyblue', edgecolor='black')
plt.title('Гистограмма лет выпуска')
plt.xlabel('Год выпуска')
plt.ylabel('Количество названий')



movie_durations = duration_data[netflix_data['type'] == 'Movie'].dropna()
plt.subplot(1, 3, 2)
plt.hist(movie_durations, bins=30, color='salmon', edgecolor='black')
plt.title('Гистограмма продолжительности фильма')
plt.xlabel('Продолжительность (минуты)')
plt.ylabel('Количество фильмов')


netflix_data['year_added'] = pd.to_datetime(netflix_data['date_added']).dt.year
year_added_data = netflix_data['year_added']
plt.subplot(1, 3, 3)
plt.hist(year_added_data.dropna(), bins=range(int(year_added_data.min()), int(year_added_data.max()) + 1), color='lightgreen', edgecolor='black')
plt.title('Гистограмма лет, когда были добавлены названия')
plt.xlabel('Год добавления')
plt.ylabel('Количество добавленных названий')

plt.tight_layout()
plt.show()
