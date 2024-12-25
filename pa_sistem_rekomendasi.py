# -*- coding: utf-8 -*-
"""PA_SISTEM_REKOMENDASI.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LlXaAut0yLvbvw5nWSpt41oYGfSgFtmN

## Import Library
"""

import numpy as np
import pandas as pd
import seaborn as sns
import tensorflow as tflw
from tensorflow import keras
from google.colab import files
import matplotlib.pyplot as plt
from tensorflow.keras import layers
from sklearn.neighbors import NearestNeighbors
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

"""## Data Understanding

Pada tahap ini dilakukan untuk memahami dataset sebelum analisis.

### Data Loading

Tahap ini adalah memuat dataset. Saya menggunakan google drive agar lebih mudah.

Dataset "Anime Dataset 2023" didapatkan dari Kaggle https://www.kaggle.com/datasets/dbdmobile/myanimelist-dataset?select=users-details-2023.csv

Load data anime dataset 2023
"""

anime_film = pd.read_csv('/content/drive/MyDrive/DICODING MACHINE LEARNING/Machine Learning Terapan/anime-dataset-2023.csv')
anime_film.head()

"""Load data user details 2023"""

user = pd.read_csv('/content/drive/MyDrive/DICODING MACHINE LEARNING/Machine Learning Terapan/users-details-2023.csv')
user.head()

"""Loading dataset"""

user_score = pd.read_csv('/content/drive/MyDrive/DICODING MACHINE LEARNING/Machine Learning Terapan/users-score-2023.csv')
user_score.head()

"""### Exploratory Data Analysis

Pada EDA ini saya akan mengecek struktur data, informasi data, mengidentifikasi adanya missing value, serta menampilkan distribusi kolom numerik.
"""

anime_film.info()

anime_film.shape

user.info()

user.shape

user_score.info()

user_score.shape

anime_film.describe()

user.describe()

user_score.describe()

"""Cek Missing Value

"""

anime_film.isnull().sum()

"""Data film anime tidak memiliki missing value"""

user.isnull().sum()

user_score.isnull().sum()

"""Data user memiliki missing value pada Username, Gender, Birthday, Location, Mean Score, Watching, Completed, On Hold, Plan to Watch, Total Entries, Rewatched, Episode Watched.

Hapus Duplikat Data
"""

anime_film.duplicated().sum()

user.duplicated().sum()

user_score.duplicated().sum()

"""Tidak ada duplikat data

Setelah itu akan menghapus data missing value
"""

user.dropna()

user.shape

user_score.dropna()

user_score.shape

"""### Univariate Analysis

Univariate analysis adalah metode statistik yang digunakan untuk menganalisis satu variabel pada satu waktu. Tujuannya adalah untuk menggambarkan dan memahami karakteristik variabel tersebut, baik dari segi distribusi, central tendency (seperti mean, median, dan mode), maupun variabilitas (seperti range, variance, dan standard deviation).


pada tahap ini saya akan menampilkan visualisasi beberapa variabel agar dapat lebih memahami dataset
"""

# Memisahkan genre dan menghitung frekuensi
all_genres = anime_film['Genres'].str.split(', ').explode()
genre_counts = all_genres.value_counts()

# Plot 10 genre terbanyak
plt.figure(figsize=(10, 5))
sns.barplot(x=genre_counts.head(10).index, y=genre_counts.head(10).values, palette='viridis')
plt.title('Top 10 Genres Anime')
plt.xlabel('Genres')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

"""Visualisasi diatas menghitung berdasarkan main genre dikarenakan value pada genre data anime terdiri dari banyak genre."""

# Menghitung frekuensi setiap tipe anime
type_counts = anime_film['Type'].value_counts()

# Plot tipe anime
plt.figure(figsize=(10, 5))
sns.barplot(x=type_counts.index, y=type_counts.values, palette='viridis')
plt.title('Distribusi Tipe Anime')
plt.xlabel('Type')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

"""Visualisasi diatas menunjukkan distribusi tipe anime. Dimana paling tinggi adalah TV"""

# Menghitung jumlah studios
studio_counts = anime_film['Studios'].value_counts()

# Mengelompokkan studios dengan jumlah terbanyak
top_studios = studio_counts.head(5)  # Mengambil 5 studio teratas
other_count = studio_counts.iloc[5:].sum()  # Menghitung total untuk studio lainnya
studio_counts_grouped = pd.concat([top_studios, pd.Series({'Lainnya': other_count})])

# Mengurutkan studio_counts_grouped dari yang tertinggi ke terendah
studio_counts_grouped = studio_counts_grouped.sort_values(ascending=False)

# Memastikan variabel studio_counts_grouped terdefinisi
print(studio_counts_grouped)

# Membuat bar chart dengan urutan dari yang tertinggi ke terendah
plt.figure(figsize=(12, 7))
sns.barplot(
    x=studio_counts_grouped.index,
    y=studio_counts_grouped.values,
    palette='viridis'
)

# Menambahkan detail pada bar chart
plt.title('Distribusi Studios Anime (Top 5 + Lainnya)', fontsize=16, fontweight='bold')
plt.xlabel('Studios', fontsize=14)
plt.ylabel('Jumlah Anime', fontsize=14)
plt.xticks(rotation=45)
plt.show()

"""Visualisasi diatas menunjukkan Top 5 Studio anime terbanyak"""

# Data 10 anime teratas berdasarkan jumlah members
top10_anime = anime_film.nlargest(10, 'Members')[['Name', 'Members']]

# Membalik urutan top10_anime agar yang tertinggi berada di atas
top10_anime = top10_anime.sort_values(by='Members', ascending=True)

# Menggunakan palet warna 'viridis' dari Seaborn
colors = sns.color_palette('viridis', n_colors=10)

# Plot bar horizontal
plt.figure(figsize=(15, 5))
plt.barh(top10_anime['Name'], top10_anime['Members'], color=colors, edgecolor='black')
plt.xlabel('Jumlah Members', fontsize=15)
plt.ylabel('Nama Anime', fontsize=15)
plt.title("10 Anime Teratas Berdasarkan Jumlah Members")
plt.grid(axis='x', linestyle='--', alpha=0.7)

plt.show()

"""Visualisasi diatas menunjukkan top 10 anime berdasarkan jumlah member

### Multivariate Analysis

Multivariate analysis adalah teknik statistik yang digunakan untuk menganalisis lebih dari dua variabel secara bersamaan.


pada tahap ini saya akan mengubah beberapa tipe data yang kurang cocok agar dapat mempermudah EDA Multivariate Analysis, kemudian menampilkan beberapa visualisasi hubungan antar variabel.
"""

# Mengubah dat amenjadi numerik
user['Watching'] = user['Watching'].fillna(0).astype(int)
user['Completed'] = user['Completed'].fillna(0).astype(int)
user['Plan to Watch'] = user['Plan to Watch'].fillna(0).astype(int)

# Mengubah 'Score' dan 'Episodes' menjadi numerik
anime_film['Score'] = pd.to_numeric(anime_film['Score'], errors='coerce')
anime_film['Episodes'] = pd.to_numeric(anime_film['Episodes'], errors='coerce')

# Menghapus baris dengan NaN setelah konversi
anime_film = anime_film.dropna(subset=['Score', 'Episodes'])

plt.figure(figsize=(12, 6))
sns.boxplot(data=anime_film, x='Type', y='Score', palette='viridis')
plt.title('Distribusi Score Berdasarkan Tipe Anime')
plt.xlabel('Tipe Anime')
plt.ylabel('Score')
plt.grid(axis='y')
plt.show()

"""Visualisasi diatas dapat membantu melihat variasi skor untuk setiap tipe anime. Juga menampilkan outlier skor pada tiap anime."""

plt.figure(figsize=(15, 7))
sns.scatterplot(data=anime_film, x='Popularity', y='Members', alpha=0.6, color='purple')
plt.title('Hubungan antara Popularity dan Members Anime')
plt.xlabel('Popularity')
plt.ylabel('Members')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

"""Visualisasi diatas menunjukkan hubungan antara popularitas dan jumlah member dimana semakin populer anime nya semakin banyak jumlah member."""

plt.figure(figsize=(12, 6))
sns.scatterplot(data=anime_film, x='Favorites', y='Popularity', alpha=0.7, color='purple')
plt.title('Hubungan antara Jumlah Favorit dan Popularity Anime')
plt.xlabel('Jumlah Favorit')
plt.ylabel('Popularity')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

"""Grafik diatas menunjukkan korelasi negatif anatara jumlah favorit dan popularitas. Anime yang lebih populer (skor popularitas rendah) cenderung memiliki jumlah favorit yang lebih tinggi, meskipun tidak semua anime dengan banyak favorit berada di puncak popularitas."""

correlation_matrix = anime_film[['Score', 'Episodes', 'Popularity', 'Favorites', 'Members']].corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='viridis', fmt='.2f')
plt.title('Korelasi antara Variabel Numerik')
plt.show()

"""Heatmap diatas menunjukkan kolerasi antar variabel

### Data Preprocessing
"""

anime_film.info()

"""Untuk mempermudah dalam analisis maka kolom kolom yang tidak diperlukan akan dihapus

"""

Anime = anime_film.drop(columns=[
    'English name', 'Other name', 'Synopsis','Episodes', 'Aired', 'Premiered',
    'Status', 'Producers', 'Licensors', 'Studios', 'Source', 'Duration', 'Rating',
    'Rank', 'Popularity', 'Favorites', 'Scored By', 'Members', 'Image URL', 'Score','Type'
    ])

Anime_sorted = Anime.sort_values('anime_id')

Anime_sorted

Anime_sorted.Genres.unique()

"""Diatas merupakan genre-genre dari anime akan tetapi terdapat kolom genre yang berisi UNKWOWN, itu dapat mengganggu analisis maka akan dihapus."""

Anime_sorted[Anime_sorted['Genres'] == 'UNKNOWN']

"""terdapat 1751 yang memiliki genre UNKNOWN maka selanjutnya membuat dataframe baru tanpa anime yang memiliki genre UNKNOWN"""

anime_clean = Anime_sorted[Anime_sorted['Genres'] != 'UNKNOWN']

"""Karena jumlah user_score yang sangat banyak maka pada tahap ini akan diambil beberapa sample saja yaitu 10000 sample dan menerapkan random_state agar data lebih teracak dengan baik."""

rating_sample=user_score.sample(n=10000, random_state=42)

rating_sample.head()

"""## Data Preparation

Pada tahap ini dilakukan TF_IDF, Encoding pada Data User Rating, dan Data splitting pada User Rating

### TF-IDF Vectorizer Data
"""

tf = TfidfVectorizer()

tf.fit(anime_clean['Genres'])

tf.get_feature_names_out()

tfidf_matrix = tf.fit_transform(anime_clean['Genres'])

tfidf_matrix_dense = tfidf_matrix.toarray()

tfidf_matrix_dense

"""### Encoding Rating

encoding fitur'user_id'
"""

# Mengubah user_id menjadi list tanpa nilai yang sama
user_ids = rating_sample['user_id'].unique().tolist()
print('list user_id: ', user_ids)

# Melakukan encoding userID
user_to_user_encoded = {x: i for i, x in enumerate(user_ids)}
print('encoded user_id : ', user_to_user_encoded)

# Melakukan proses encoding angka ke ke user_id
user_encoded_to_user = {i: x for i, x in enumerate(user_ids)}
print('encoded angka ke user_id: ', user_encoded_to_user)

# Menampilkan jumlah pengguna yang telah diencode
print(f'Total unique users: {len(user_ids)}')

"""encoding 'anime_id'"""

anime_ids = rating_sample['anime_id'].unique().tolist()

anime_to_anime_encoded = {x: i for i, x in enumerate(anime_ids)}

anime_encoded_to_anime = {i: x for i, x in enumerate(anime_ids)}

rating_sample['user'] = rating_sample['user_id'].map(user_to_user_encoded)

rating_sample['anime'] = rating_sample['anime_id'].map(anime_to_anime_encoded)

"""Cek jumlah user, dan jumlah anime"""

# Mendapatkan jumlah user
total_users = len(user_to_user_encoded)
print(total_users)

# Mendapatkan jumlah anime
total_anime = len(anime_encoded_to_anime)
print(total_anime)

rating_sample.info()

rating_sample['rating'] = rating_sample['rating'].values.astype(np.float32)

"""Mengubah nilai rating menjadi float

## Splitting Rating
"""

# Nilai minimum rating
min_rating = min(rating_sample['rating'])

# Nilai maksimal rating
max_rating = max(rating_sample['rating'])

rating_sample = rating_sample.sample(frac=1, random_state=42)
rating_sample

"""Tahap splitting ini mengacak data, menyiapkan fitur dan target (dengan normalisasi rating), lalu membagi data menjadi 80% untuk pelatihan dan 20% untuk validasi."""

# Mengacak data
rating_sample = rating_sample.sample(frac=1, random_state=42)

# Membuat variabel x untuk mencocokkan data user dan anime menjadi satu value
x = rating_sample[['user', 'anime']].values

# Membuat variabel y untuk membuat rating dari hasil
y = rating_sample['rating'].apply(lambda x: (x - min_rating) / (max_rating - min_rating)).values

# Membagi menjadi 80% data train dan 20% data validasi
train_indices = int(0.8 * rating_sample.shape[0])
x_train, x_val, y_train, y_val = (
    x[:train_indices],
    x[train_indices:],
    y[:train_indices],
    y[train_indices:]
)

print(x,y)

"""## Modelling

Tahapan modelling akan dilakukan berdasarkan Content Based Learning menggunakan Cosine Similarity dan Collaborative Based learning menggunakan recomenderNet

### Model 1 Cosine Similarity

Tahap ini menghitung kemiripan kosinus antar-vektor dalam matriks TF-IDF (`tfidf_matrix`) dan menghasilkan matriks kemiripan kosinus.
"""

cosine_sim = cosine_similarity(tfidf_matrix)
cosine_sim

cosine_sim_df = pd.DataFrame(cosine_sim, index=anime_clean['Name'], columns=anime_clean['Name'])
print('Shape:', cosine_sim_df.shape)

cosine_sim_df.sample(5, axis=1).sample(10, axis=0)

"""Maka didapat kesamaa anatar anime satu dnegan yang lain

Selanjutnya membuat fungsi dengan parameter nama_anime, data similarity, item (anime_name dan Genres)

Fungsi `anime_recommendations` memberikan rekomendasi anime berdasarkan kemiripan kosinus. Berikut penjelasan singkat:

1. **Validasi Input**: Memastikan `nama_anime` yang dicari ada di dalam data `similarity_data`. Jika tidak, fungsi mengembalikan pesan error.
2. **Mengambil Indeks Terdekat**: Menghitung indeks anime dengan kemiripan tertinggi terhadap `nama_anime` menggunakan data kemiripan.
3. **Daftar Terdekat**: Mengambil daftar anime terdekat (k anime paling mirip) dan menghilangkan `nama_anime` dari daftar rekomendasi.
4. **Menggabungkan Data**: Menggabungkan hasil rekomendasi dengan data `items` untuk mendapatkan informasi genre, lalu mengembalikan daftar rekomendasi (maksimal `k` anime) sebagai DataFrame.

Fungsi ini menghasilkan daftar anime yang mirip dengan `nama_anime`, lengkap dengan genre-nya.
"""

def anime_recommendations(nama_anime, similarity_data=cosine_sim_df, items=anime_clean[['Name', 'Genres']], k=10):
    # Memastikan nama_anime ada dalam similarity_data
    if nama_anime not in similarity_data.columns:
        return f"{nama_anime} tidak ditemukan dalam data."

    # Mengambil indeks anime dengan similarity tertinggi
    index = similarity_data.loc[:, nama_anime].to_numpy().argpartition(range(-1, -k-1, -1))

    # Mengambil nama anime terdekat berdasarkan similarity
    closest_indices = index[-1:-(k+1):-1]
    closest = similarity_data.columns[closest_indices]

    # Menghapus nama_anime dari daftar rekomendasi
    closest = closest.drop(nama_anime, errors='ignore')

    # Mengembalikan DataFrame dengan informasi nama anime dan genre
    recommendations = pd.DataFrame(closest, columns=['Name']).merge(items, on='Name').head(k)

    return recommendations

"""Test rekomendasi dengan memasukkan nama anime"""

anime_clean[anime_clean.Name.eq('Cowboy Bebop')]

"""Hasil rekomendasu dimana anime ini memiliki genre yang mirip"""

anime_recommendations('Cowboy Bebop')

"""### Model 2 RecommenderNet

Kode ini mendefinisikan model rekomendasi `RecommenderNet` menggunakan TensorFlow dan Keras, yang memanfaatkan embedding untuk memodelkan preferensi pengguna terhadap anime. Berikut penjelasan singkat per bagian:

1. **Inisialisasi Model**: Fungsi `__init__` mendefinisikan layer embedding untuk pengguna (`user_embedding`) dan anime (`anime_embedding`), serta bias untuk masing-masing (`user_bias` dan `anime_bias`). `embedding_size` menentukan dimensi ruang embedding, dan regularisasi `l2` diterapkan untuk mencegah overfitting.

2. **Metode `call`**: Fungsi `call` menghitung skor rekomendasi untuk pasangan pengguna-anime:
   - Mengambil embedding dan bias untuk pengguna dan anime berdasarkan `inputs`.
   - Menghitung produk titik (dot product) antara vektor embedding pengguna dan anime (`dot_user_anime`), yang mewakili kesamaan antara keduanya.
   - Menambahkan nilai bias pengguna dan anime ke hasil `dot_user_anime`.
   
3. **Aktivasi Sigmoid**: Menggunakan fungsi sigmoid pada hasil akhir untuk mengeluarkan nilai antara 0 dan 1, yang mewakili probabilitas bahwa pengguna akan menyukai anime tersebut.

Model ini ditujukan untuk sistem rekomendasi berbasis kolaboratif, yang memprediksi preferensi pengguna terhadap anime tertentu.
"""

class RecommenderNet(tflw.keras.Model):

  # Insialisasi fungsi
  def __init__(self, num_users, num_anime, embedding_size, **kwargs):
    super(RecommenderNet, self).__init__(**kwargs)
    self.num_users = num_users
    self.num_anime = num_anime
    self.embedding_size = embedding_size
    self.user_embedding = layers.Embedding(
        num_users,
        embedding_size,
        embeddings_initializer = 'he_normal',
        embeddings_regularizer = keras.regularizers.l2(1e-6)
    )
    self.user_bias = layers.Embedding(num_users, 1)
    self.anime_embedding = layers.Embedding(
        num_anime,
        embedding_size,
        embeddings_initializer = 'he_normal',
        embeddings_regularizer = keras.regularizers.l2(1e-6)
    )
    self.anime_bias = layers.Embedding(num_anime, 1)

  def call(self, inputs):
    user_vector = self.user_embedding(inputs[:,0]) # memanggil layer embedding 1
    user_bias = self.user_bias(inputs[:, 0]) # memanggil layer embedding 2
    anime_vector = self.anime_embedding(inputs[:, 1]) # memanggil layer embedding 3
    anime_bias = self.anime_bias(inputs[:, 1]) # memanggil layer embedding 4

    dot_user_anime = tflw.tensordot(user_vector, anime_vector, 2)

    x = dot_user_anime + user_bias + anime_bias

    return tflw.nn.sigmoid(x) # activation sigmoid

model = RecommenderNet(total_users, total_anime, 50)

# model compile
model.compile(
    loss = tflw.keras.losses.BinaryCrossentropy(),
    optimizer = keras.optimizers.Adam(learning_rate=0.001),
    metrics=[tflw.keras.metrics.RootMeanSquaredError()]
)

"""Training"""

history = model.fit(
    x = x_train,
    y = y_train,
    batch_size = 32,
    epochs = 100,
    validation_data = (x_val, y_val)
)

"""Tahap selanjutnya adalah memberikan rekomendasi dari model yang telah dibuat.

- Mengambil sample secara acak
- Mendefinisikan anime_not_visited yang bermaksud anime yang belum pernah dilihat/dikunjungi user.
- Menggunakan operator bitwise
"""

anime_df = anime_clean
df = rating_sample

# Mengambil sample user
user_id = df.user_id.sample(1).iloc[0]

# Mendapatkan anime yang sudah dikunjungi oleh user
anime_visited_by_user = df[df.user_id == user_id]['anime_id'].values

# Operator bitwise (~), bisa diketahui di sini https://docs.python.org/3/reference/expressions.html
# Mengambil anime yang belum dikunjungi
anime_not_visited = anime_df[~anime_df['anime_id'].isin(anime_visited_by_user)]['anime_id']

# Mengonversi anime yang belum dikunjungi ke dalam format yang sesuai
anime_not_visited = [
    [anime_to_anime_encoded[anime_id]]
    for anime_id in set(anime_not_visited).intersection(anime_to_anime_encoded.keys())
]

# Mendapatkan user yang telah di-encode
user_encoder = user_to_user_encoded[user_id]

# Menggabungkan user dan anime yang belum dikunjungi ke dalam array
user_anime_array = np.hstack(
    ([[user_encoder]] * len(anime_not_visited), anime_not_visited)
)

# Menampilkan user_anime_array untuk memastikan hasilnya
print("User-Anime Array:", user_anime_array)

# Mengambil sample user
user_id = df.user_id.sample(1).iloc[0]
anime_visited_by_user = df[df.user_id == user_id]

# Memastikan anime_visited_by_user adalah DataFrame
anime_visited_by_user = anime_visited_by_user.copy()

# Memprediksi rating untuk anime yang belum dikunjungi oleh pengguna
ratings = model.predict(user_anime_array).flatten()

# Mengambil indeks anime dengan rating tertinggi
top_ratings_indices = ratings.argsort()[-10:][::-1]

# Mendapatkan ID anime yang direkomendasikan berdasarkan indeks rating tertinggi
recommended_anime_ids = [
    anime_encoded_to_anime[anime_not_visited[x][0]] for x in top_ratings_indices
]

# Menampilkan rekomendasi untuk pengguna
print('Menampilkan rekomendasi untuk pengguna: {}'.format(user_id))
print('===' * 15)
print('Anime dengan rating tertinggi dari pengguna')
print('---' * 15)

# Mengambil 5 anime teratas yang sudah ditonton oleh pengguna berdasarkan rating
if not anime_visited_by_user.empty:
    top_anime_user = (
        anime_visited_by_user.sort_values(by='rating', ascending=False)
        .head(5)
        .anime_id.values
    )

    # Menampilkan detail anime yang telah ditonton
    anime_df_rows = anime_df[anime_df['anime_id'].isin(top_anime_user)]
    for row in anime_df_rows.itertuples(index=False):
        print(f"{row.Name} : {row.Genres}")
else:
    print("Pengguna belum menonton anime.")

print('---' * 15)
print('Rekomendasi 10 anime teratas')
print('---' * 15)

# Menampilkan anime yang direkomendasikan
recommended_anime = anime_df[anime_df['anime_id'].isin(recommended_anime_ids)]
for row in recommended_anime.itertuples(index=False):
    print(f"{row.Name} : {row.Genres}")

"""Diatas merupakan hasil rekomendasi untuk user

## Evaluasi Model
"""

plt.plot(history.history['root_mean_squared_error'])
plt.plot(history.history['val_root_mean_squared_error'])
plt.title('model_metrics')
plt.ylabel('root_mean_squared_error')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

"""Hasil training cukup bagus dimana hasil akhir error pada train 0.7 dan pada test 0.25

Matrix

Metrik *Precision* digunakan untuk mengevaluasi seberapa baik performa model, terutama dalam pengelompokan. *Precision* mengukur proporsi antara nilai sebenarnya (ground truth) dengan prediksi yang positif. Rumusnya adalah:

$$ Precision = \frac{TP}{TP + FP} $$

Di mana:

- TP (*True Positive*) adalah jumlah kejadian positif yang diprediksi dengan benar oleh model.
- FP (*False Positive*) adalah jumlah kejadian positif yang salah diprediksi oleh model.

Metrik ini membantu menunjukkan akurasi prediksi positif yang dihasilkan model.


Precision dihitung dengan rumus:

$$
Precision = \frac{9}{9 + 1} = \frac{9}{10} = 0.9
$$

Berdasarkan hasil yang dihasilkan oleh model Cosine Similarity sebelumnya, tingkat presisi yang dihitung adalah 9/10 untuk rekomendasi Top-10. Ini menunjukkan bahwa sistem mampu memberikan rekomendasi yang sangat sesuai dengan genre anime yang diinginkan, meskipun ada sedikit perbedaan dari rekomendasi yang ideal
"""

