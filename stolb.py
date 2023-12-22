
import matplotlib.pyplot as plt

from main import *

fig, axes = plt.subplots(3, 1, figsize=(10, 15))


top_countries = netflix_data['country'].value_counts().head(10)
top_countries.plot(kind='bar', ax=axes[0], color='purple')
axes[0].set_title('Количество названий по странам (Топ-10)')
axes[0].set_xlabel('Страна')
axes[0].set_ylabel('Количество названий')


ratings_count = netflix_data['rating'].value_counts()
ratings_count.plot(kind='bar', ax=axes[1], color='orange')
axes[1].set_title('Распределение титулов по различным рейтингам')
axes[1].set_xlabel('Рейтинг')
axes[1].set_ylabel('Количество названий')


type_count = netflix_data['type'].value_counts()
type_count.plot(kind='bar', ax=axes[2], color='teal')
axes[2].set_title('Количество фильмов по сравнению с телешоу')
axes[2].set_xlabel('Тип')
axes[2].set_ylabel('Количество')


plt.tight_layout()

plt.show()
