import pandas as pd
import matplotlib.pyplot as plt

from main import *



fig, axes = plt.subplots(3, 1, figsize=(10, 15))

netflix_data.groupby('added_year')['title'].count().plot(kind='line', ax=axes[0], color='blue', marker='o')
axes[0].set_title('Количество названий, добавляемых каждый год')
axes[0].set_xlabel('Год')
axes[0].set_ylabel('Количество названий')


netflix_movies = netflix_data[netflix_data['type'] == 'Movie']
netflix_movies.groupby('release_year')['duration_min'].mean().plot(kind='line', ax=axes[1], color='green', marker='o')
axes[1].set_title('Средняя продолжительность фильмов за годы')
axes[1].set_xlabel('Год выпуска')
axes[1].set_ylabel('Средняя продолжительность (минуты)')


netflix_data.groupby(['release_year', 'type']).size().unstack().plot(kind='line', ax=axes[2], marker='o')
axes[2].set_title('Количество фильмов по сравнению с телешоу за последние годы')
axes[2].set_xlabel('Год выпуска')
axes[2].set_ylabel('Количество')
axes[2].legend(title='Type')


plt.tight_layout()

plt.show()
