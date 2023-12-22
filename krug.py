import matplotlib.pyplot as plt
import seaborn as sns

from main import * 


fig, axes = plt.subplots(1, 2, figsize=(14, 7))


top_genres = netflix_data['listed_in'].str.split(', ').explode().value_counts().head(5)
top_genres.plot(kind='pie', ax=axes[0], autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
axes[0].set_title('Доля названий в разных жанрах (Топ-5)')
axes[0].set_ylabel('')


top_countries_share = netflix_data['country'].value_counts().head(5)
top_countries_share.plot(kind='pie', ax=axes[1], autopct='%1.1f%%', startangle=140, colors=sns.color_palette('deep'))
axes[1].set_title('Доля титулов из ведущих стран-доноров (Топ-5)')
axes[1].set_ylabel('')


plt.tight_layout()

plt.show()
