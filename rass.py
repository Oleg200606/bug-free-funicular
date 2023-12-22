import seaborn as sns
import matplotlib.pyplot as plt
from main import *

duration_data = netflix_data['duration'].str.extract('(\d+)').astype(float)


movie_durations = duration_data[netflix_data['type'] == 'Movie'].dropna()


movies_data = netflix_data[netflix_data['type'] == 'Movie']
movie_durations = duration_data[netflix_data['type'] == 'Movie'].dropna()

plt.figure(figsize=(15, 6))
plt.subplot(1, 2, 1)
sns.scatterplot(x='release_year', y=movie_durations.squeeze(), data=movies_data)
plt.title('Диаграмма рассеяния зависимости продолжительности фильма от даты выхода')
plt.xlabel('Год выпуска')
plt.ylabel('Продолжительность в минутах')
netflix_data['date_added'] = pd.to_datetime(netflix_data['date_added'], errors='coerce')
netflix_data['year_added'] = netflix_data['date_added'].dt.year

plt.subplot(1, 2, 2)
sns.scatterplot(x='release_year', y='year_added', data=netflix_data)
plt.title('Точечная диаграмма года, добавленная в Netflix в зависимости от года выпуска')
plt.xlabel('Год выхода')
plt.ylabel('Добавлен на Netflix')

plt.tight_layout()
plt.show()
