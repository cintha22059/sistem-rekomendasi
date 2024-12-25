# Laporan Proyek AKhir Machine Learning Terapan - Cintha Hafrida Putri

## Domain Proyek

Pertumbuhan Popularitas Anime
Anime telah berkembang menjadi bagian integral dari budaya populer global, 
dengan jutaan penggemar setia di seluruh dunia. Dari berbagai genre dan gaya visual,
anime menawarkan lebih dari 12.000 judul yang membuat penggemar terus menikmati, mengeksplorasi, 
dan menemukan konten baru. Namun, dengan banyaknya pilihan yang tersedia, banyak pengguna merasa 
kesulitan dalam menemukan judul yang sesuai dengan selera pribadi mereka [(Muhammad., 2023_)](https://publishing-widyagama.ac.id/ejournal-v2/bcti/article/view/4885). 
Untuk menjawab tantangan ini, muncul kebutuhan akan sistem rekomendasi yang 
mampu memberikan saran yang lebih tepat dan relevan, disesuaikan dengan preferensi 
unik masing-masing pengguna.

## Business Understanding

### Problem Statements
- Pengguna kesulitan menemukan judul anime yang sesuai dengan preferensi mereka di antara ribuan pilihan yang tersedia.
- Kurangnya rekomendasi yang relevan membuat pengguna membutuhkan sistem yang dapat menyarankan anime yang belum pernah ditonton dan sesuai dengan minat mereka.
- Diperlukan metode yang dapat mengukur efektivitas sistem rekomendasi dalam memberikan saran yang akurat dan relevan bagi pengguna.

### Goals
- Mengembangkan sistem rekomendasi anime yang mampu memberikan saran anime yang sesuai dengan preferensi pengguna.
- Meningkatkan kepuasan pengguna dengan merekomendasikan anime yang belum pernah ditonton dan cocok dengan minat mereka.
- Mengukur kinerja sistem rekomendasi menggunakan metrik seperti precision untuk memastikan kualitas rekomendasi yang dihasilkan.

### Solution statements
- Menggunakan pendekatan content-based filtering berbasis cosine similarity untuk merekomendasikan anime berdasarkan kesamaan genre.
- Mengimplementasikan collaborative-based filtering untuk menganalisis preferensi pengguna berdasarkan rating yang telah diberikan, sehingga bisa merekomendasikan anime yang mungkin disukai oleh pengguna.
- Mengukur performa sistem dengan menggunakan metrik precision untuk memastikan rekomendasi yang relevan dan meningkatkan akurasi sistem dalam memberikan saran yang sesuai.

## Data Understanding
Dataset yang digunakan adalah Anime Dataset 2023 [(Anime_dataset_2023_kaggle)](https://www.kaggle.com/datasets/dbdmobile/myanimelist-dataset?select=users-details-2023.csv). 
Dmana dalam proyek ini hanya menggunakan dataset anime-dataset-2023, user-score, dan user-details.

Anime-datset-2023 
- Jumlah baris : 24905
- Jumlah kolom : 24
- Berikut adalah variabel-variabel pada anime-dataset-2023
  
| Kolom         | Deskripsi                                                                                                                                                          |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| anime_id      | ID unik untuk setiap anime.                                                                                                                                        |
| Name          | Nama asli anime dalam bahasa aslinya.                                                                                                                              |
| English name  | Nama anime dalam bahasa Inggris.                                                                                                                                   |
| Other name    | Nama atau judul asli anime dalam bahasa lain (misalnya Jepang, Tiongkok, atau Korea).                                                                              |
| Score         | Skor atau penilaian yang diberikan untuk anime tersebut.                                                                                                          |
| Genres        | Genre dari anime, dipisahkan dengan koma.                                                                                                                          |
| Synopsis      | Deskripsi singkat atau ringkasan alur cerita anime.                                                                                                               |
| Type          | Tipe anime (misalnya, serial TV, film, OVA, dll.).                                                                                                                |
| Episodes      | Jumlah episode dalam anime.                                                                                                                                        |
| Aired         | Tanggal ketika anime ditayangkan.                                                                                                                                  |
| Premiered     | Musim dan tahun ketika anime pertama kali tayang.                                                                                                                 |
| Status        | Status penayangan anime (misalnya, Selesai Ditayangkan, Sedang Ditayangkan, dll.).                                                                                |
| Producers     | Perusahaan produksi atau produser dari anime.                                                                                                                     |
| Licensors     | Pemberi lisensi anime (misalnya, platform streaming).                                                                                                             |
| Studios       | Studio animasi yang mengerjakan anime tersebut.                                                                                                                   |
| Source        | Sumber asli materi dari anime (misalnya, manga, novel ringan, orisinal).                                                                                          |
| Duration      | Durasi setiap episode anime.                                                                                                                                      |
| Rating        | Rating usia untuk anime tersebut.                                                                                                                                 |
| Rank          | Peringkat anime berdasarkan popularitas atau kriteria lainnya.                                                                                                    |
| Popularity    | Peringkat popularitas dari anime tersebut.                                                                                                                        |
| Favorites     | Jumlah pengguna yang menandai anime sebagai favorit.                                                                                                              |
| Scored By     | Jumlah pengguna yang memberikan skor untuk anime tersebut.                                                                                                        |
| Members       | Jumlah anggota yang menambahkan anime ke daftar mereka di platform.                                                                                               |
| Image URL     | URL dari poster atau gambar anime.                                                                                                                                |

Dataset ini menawarkan informasi berharga untuk menganalisis dan
 memahami karakteristik, peringkat, popularitas, dan jumlah penonton dari berbagai 
 acara anime. Dengan memanfaatkan dataset ini, seseorang dapat melakukan berbagai analisis,
 termasuk mengidentifikasi anime dengan rating tertinggi, mengeksplorasi genre paling populer,
 memeriksa distribusi rating, dan mendapatkan wawasan tentang preferensi dan tren pemirsa. 
 Selain itu, dataset ini memfasilitasi pembuatan sistem rekomendasi, analisis deret waktu,
 dan pengelompokan untuk mempelajari lebih dalam tentang tren anime dan perilaku pengguna.



user-details
- Jumlah baris : 731290
- Jumlah kolom : 16
- berikut adalah variabel-variabel pada dataset user-details
  
| Kolom           | Deskripsi                                                                                                                                                 |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Mal ID          | ID unik untuk setiap pengguna.                                                                                                                            |
| Username        | Nama pengguna dari user.                                                                                                                                  |
| Gender          | Jenis kelamin pengguna.                                                                                                                                   |
| Birthday        | Tanggal lahir pengguna (dalam format ISO).                                                                                                                |
| Location        | Lokasi atau negara tempat pengguna berada.                                                                                                                |
| Joined          | Tanggal ketika pengguna bergabung dengan platform (dalam format ISO).                                                                                    |
| Days Watched    | Total jumlah hari yang dihabiskan oleh pengguna untuk menonton anime.                                                                                     |
| Mean Score      | Skor rata-rata yang diberikan oleh pengguna kepada anime yang telah mereka tonton.                                                                        |
| Watching        | Jumlah anime yang sedang ditonton oleh pengguna saat ini.                                                                                                 |
| Completed       | Jumlah anime yang telah selesai ditonton oleh pengguna.                                                                                                   |
| On Hold         | Jumlah anime yang ditunda oleh pengguna.                                                                                                                  |
| Dropped         | Jumlah anime yang telah dihentikan atau dibatalkan oleh pengguna.                                                                                         |
| Plan to Watch   | Jumlah anime yang direncanakan untuk ditonton oleh pengguna di masa mendatang.                                                                            |
| Total Entries   | Total jumlah entri anime di daftar pengguna.                                                                                                              |
| Rewatched       | Jumlah anime yang telah ditonton ulang oleh pengguna.                                                                                                     |
| Episodes Watched| Total jumlah episode yang telah ditonton oleh pengguna.                                                                                                   |


Dataset Detail Pengguna memberikan informasi berharga untuk menganalisis perilaku dan
preferensi pengguna di platform anime. Dengan memeriksa skor rata-rata dan genre anime, 
Anda dapat memperoleh wawasan tentang preferensi pengguna. Pengguna dapat disegmentasikan
ke dalam kelompok yang berbeda berdasarkan perilaku menonton mereka, seperti pengguna aktif 
dan penonton biasa. Sistem rekomendasi yang dipersonalisasi dapat dibuat menggunakan 
daftar yang telah diisi dan rencana tontonan pengguna. Analisis berbasis lokasi 
mengungkapkan popularitas anime dan keterlibatan pengguna di berbagai negara. 
Tren perilaku menonton, retensi pengguna, dan perbedaan preferensi anime berdasarkan ge
nder dapat diidentifikasi. Selain itu, Anda dapat mengeksplorasi kebiasaan menonton ulang 
dan melakukan analisis deret waktu untuk memahami pola keterlibatan pengguna dari waktu ke 
waktu.

user-score
- jumlah baris : 24325191 (pada analisis hanya digunakan sample sebanyak 10000 data)
- jumlah kolom : 5
- Berikut variabel nya
  
| Kolom       | Deskripsi                                                                                                  |
|-------------|------------------------------------------------------------------------------------------------------------|
| user_id     | ID unik untuk setiap pengguna.                                                                             |
| Username    | Nama pengguna dari user.                                                                                   |
| anime_id    | ID unik untuk setiap anime.                                                                                |
| Anime Title | Judul dari anime.                                                                                          |
| rating      | Rating yang diberikan oleh pengguna untuk anime tersebut.                                                  |


Dataset Skor Pengguna memungkinkan berbagai analisis dan wawasan tentang
interaksi pengguna dengan anime. Dengan memeriksa peringkat pengguna untuk berbagai 
judul anime, Anda dapat mengidentifikasi anime dengan peringkat tinggi dan populer
di kalangan pengguna. Selain itu, Anda dapat menjelajahi preferensi pengguna dan pola 
menonton untuk judul anime tertentu. Kumpulan data ini juga membentuk dasar untuk membangun 
sistem rekomendasi berdasarkan peringkat pengguna, membantu menyarankan anime yang sesuai 
dengan selera individu. Selain itu, Anda dapat melakukan pemfilteran kolaboratif dan 
analisis kemiripan untuk menemukan pola minat pengguna yang serupa. Secara keseluruhan,
kumpulan data ini menawarkan informasi berharga untuk memahami keterlibatan dan preferensi 
pengguna di platform anime.


## Exploratory Data Analysis

Mengecek informasi untuk dataset anime-dataset 2023

| No | Column       | Non-Null Count | Dtype  |
|----|--------------|----------------|--------|
| 1  | anime_id     | 24905 non-null | int64  |
| 2  | Name         | 24905 non-null | object |
| 3  | English name | 24905 non-null | object |
| 4  | Other name   | 24905 non-null | object |
| 5  | Score        | 24905 non-null | object |
| 6  | Genres       | 24905 non-null | object |
| 7  | Synopsis     | 24905 non-null | object |
| 8  | Type         | 24905 non-null | object |
| 9  | Episodes     | 24905 non-null | object |
| 10 | Aired        | 24905 non-null | object |
| 11 | Premiered    | 24905 non-null | object |
| 12 | Status       | 24905 non-null | object |
| 13 | Producers    | 24905 non-null | object |
| 14 | Licensors    | 24905 non-null | object |
| 15 | Studios      | 24905 non-null | object |
| 16 | Source       | 24905 non-null | object |
| 17 | Duration     | 24905 non-null | object |
| 18 | Rating       | 24905 non-null | object |
| 19 | Rank         | 24905 non-null | object |
| 20 | Popularity   | 24905 non-null | int64  |
| 21 | Favorites    | 24905 non-null | int64  |
| 22 | Scored By    | 24905 non-null | object |
| 23 | Members      | 24905 non-null | int64  |
| 24 | Image URL    | 24905 non-null | object |

Mengecek informasi untuk dataset user-details

| No | Column            | Non-Null Count   | Dtype    |
|----|-------------------|------------------|----------|
| 0  | Mal ID            | 731290 non-null   | int64    |
| 1  | Username          | 731289 non-null   | object   |
| 2  | Gender            | 224383 non-null   | object   |
| 3  | Birthday          | 168068 non-null   | object   |
| 4  | Location          | 152805 non-null   | object   |
| 5  | Joined            | 731290 non-null   | object   |
| 6  | Days Watched      | 731282 non-null   | float64  |
| 7  | Mean Score        | 731282 non-null   | float64  |
| 8  | Watching          | 731282 non-null   | float64  |
| 9  | Completed         | 731282 non-null   | float64  |
| 10 | On Hold           | 731282 non-null   | float64  |
| 11 | Dropped           | 731282 non-null   | float64  |
| 12 | Plan to Watch     | 731282 non-null   | float64  |
| 13 | Total Entries     | 731282 non-null   | float64  |
| 14 | Rewatched         | 731282 non-null   | float64  |
| 15 | Episodes Watched   | 731282 non-null   | float64  |

Mengecek informasi untuk dataset user-details

| No | Column       | Dtype  |
|----|--------------|--------|
| 0  | user_id      | int64  |
| 1  | Username     | object |
| 2  | anime_id     | int64  |
| 3  | Anime Title  | object |
| 4  | rating       | int64  |

Dari pengecekan informasi dataset maka kita dapat mengetahuo tipe data tiap kolomnya dari 
situ saya juga memilih beberapa kolom untuk diubah tipe datanya guna kebutuhan analisis yang lebih mendalam 
(akan dibahas pada preparataion)

Statistik deskriptif untuk anime-dataset 2023

| Statistik | anime_id       | Popularity     | Favorites      | Members         |
|-----------|----------------|----------------|----------------|-----------------|
| count     | 24905.000000   | 24905.000000   | 24905.000000   | 24905.000000    |
| mean      | 29776.709014   | 12265.388356   | 432.595222     | 37104.960000    |
| std       | 17976.076290   | 7187.428393    | 4353.181647    | 156825.200000   |
| min       | 1.000000       | 0.000000       | 0.000000       | 0.000000        |
| 25%       | 10507.000000   | 6040.000000    | 0.000000       | 209.000000      |
| 50%       | 34628.000000   | 12265.000000   | 1.000000       | 1056.000000     |
| 75%       | 45240.000000   | 18491.000000   | 18.000000      | 9326.000000     |
| max       | 55735.000000   | 24723.000000   | 217606.000000  | 3744541.000000  |

Statistik deksriptif untuk user-details

| Statistik | Mal ID         | Days Watched   | Mean Score     | Watching        | Completed      | On Hold        | Dropped        | Plan to Watch  | Total Entries  | Rewatched      | Episodes Watched |
|-----------|----------------|----------------|----------------|-----------------|----------------|----------------|----------------|----------------|----------------|----------------|------------------|
| count     | 731290.000000  | 731282.000000  | 731282.000000  | 731282.000000   | 731282.000000  | 731282.000000  | 731282.000000  | 731282.000000  | 731282.000000  | 731282.000000  | 731282.000000   |
| mean      | 507020.300000  | 24.180819      | 3.948018       | 4.765714        | 65.953066      | 3.391615       | 4.565480       | 17.547893      | 96.230147      | 4.443352       | 1658.828000     |
| std       | 364014.700000  | 140.105073     | 4.137606       | 20.495890       | 186.633286     | 19.296913      | 34.915341      | 90.286927      | 265.459220     | 29.693175      | 50771.680000    |
| min       | 1.000000       | 0.000000       | 0.000000       | 0.000000        | 0.000000       | 0.000000       | 0.000000       | 0.000000       | 0.000000       | 0.000000       | 0.000000        |
| 25%       | 201108.500000  | 0.000000       | 0.000000       | 0.000000        | 0.000000       | 0.000000       | 0.000000       | 0.000000       | 0.000000       | 0.000000       | 0.000000        |
| 50%       | 425170.500000  | 0.200000       | 0.000000       | 0.000000        | 0.000000       | 0.000000       | 0.000000       | 0.000000       | 1.000000       | 0.000000       | 15.000000       |
| 75%       | 775340.000000  | 24.800000      | 8.040000       | 4.000000        | 48.000000      | 1.000000       | 1.000000       | 5.000000       | 74.000000      | 0.000000       | 1489.000000     |
| max       | 1291097.000000 | 105338.600000  | 255.000000     | 4358.000000     | 13226.000000   | 5167.000000    | 14341.000000   | 21804.000000   | 24817.000000   | 13215.000000   | 3376442.000000  |

Statistik deskriptif untuk user-score

| Statistik | user_id        | anime_id       | rating         |
|-----------|----------------|----------------|----------------|
| count     | 24325190.000000| 24325190.000000| 24325190.000000|
| mean      | 440384.300000  | 9754.686000    | 7.622930       |
| std       | 366946.900000  | 12061.960000   | 1.661510       |
| min       | 1.000000       | 1.000000       | 1.000000       |
| 25%       | 97188.000000   | 873.000000     | 7.000000       |
| 50%       | 387978.000000  | 4726.000000    | 8.000000       |
| 75%       | 528043.000000  | 13161.000000   | 9.000000       |
| max       | 1291097.000000 | 56085.000000   | 10.000000      |

Pada EDA ini juga diidentifikasi missing value dimana ternyata ditemukan pada dataset user-details dan user-score
nantinya akan di handling pada data preparation

### Univariate Analysis 
![Top 10 Genre Anime](https://github.com/user-attachments/assets/d7b9cb71-f286-4f35-a27f-8874488dcd77)
![Distribusi Tipe Anime](https://github.com/user-attachments/assets/603e94f8-be0a-4953-9552-9613e20a6b2d)
![Distribusi studio anime](https://github.com/user-attachments/assets/e195273b-206e-4653-97d4-13906684129c)
![top 10 anime berdasarkan member](https://github.com/user-attachments/assets/7bbbd454-afff-4790-bb61-2ce7b704a9d0)

### Top 10 Genre Anime
- Grafik ini menunjukkan distribusi dari 10 genre anime paling populer. Dari grafik tersebut, genre **Action**, **Adventure**, dan **Comedy** terlihat mendominasi, menandakan minat yang tinggi terhadap cerita penuh aksi dan petualangan, serta hiburan yang menyenangkan.
- Genre seperti **Fantasy** dan **Supernatural** juga memiliki popularitas tinggi, menunjukkan minat penonton pada cerita dengan elemen magis atau dunia yang tidak realistis.
- Genre **Slice of Life** berada di posisi yang cukup tinggi, mengindikasikan ketertarikan penonton pada cerita-cerita yang menggambarkan kehidupan sehari-hari secara realistis.

### Distribusi Tipe Anime
- Tipe anime **TV** memiliki proporsi yang paling besar dibandingkan dengan tipe lainnya, seperti **OVA** dan **Movie**. Hal ini wajar karena serial TV adalah format yang paling umum untuk anime, memungkinkan pengembangan cerita yang panjang.
- Tipe **Movie** dan **OVA** (Original Video Animation) juga memiliki proporsi yang signifikan. Movies sering kali menarik karena kualitas animasi yang lebih tinggi dan cerita yang padat, sedangkan OVA memberikan konten tambahan bagi penggemar.
- Tipe lain seperti **ONA** (Original Net Animation) dan **Special** memiliki proporsi yang lebih kecil, menunjukkan bahwa mereka kurang populer dibandingkan format utama.

### Distribusi Studio Anime
- Grafik ini menunjukkan distribusi anime yang diproduksi oleh berbagai studio. Beberapa studio mendominasi dalam jumlah produksi anime, kemungkinan besar karena kapasitas dan sumber daya mereka yang lebih besar.
- Studio besar seperti **Toei Animation**, **Sunrise**, dan **Madhouse** mungkin terlihat sering muncul, mengindikasikan peran mereka dalam menciptakan berbagai judul anime terkenal.
- Jumlah anime yang diproduksi oleh studio besar ini menunjukkan reputasi dan pengalaman mereka dalam menghasilkan anime yang disukai oleh penonton.

### Top 10 Anime Berdasarkan Member
- Grafik ini menampilkan 10 anime dengan jumlah anggota komunitas tertinggi. Anime dengan jumlah anggota terbanyak mungkin merupakan anime yang sangat populer, banyak dibicarakan, atau termasuk dalam kategori anime "wajib tonton" di komunitas anime.
- Beberapa judul yang sering kali menjadi perbincangan seperti **Naruto**, **One Piece**, atau **Attack on Titan** kemungkinan besar muncul di daftar ini.
- Jumlah anggota komunitas menunjukkan popularitas secara keseluruhan, dan mungkin dipengaruhi oleh distribusi global atau aksesibilitas dari platform streaming.

### Multivariate Analysis

![Cuplikan layar 2024-11-04 095102](https://github.com/user-attachments/assets/9c41e1ee-d72f-4c46-80ab-62d55150f207)

Sebelum melanjutkan ke analisis multivariate saya mengubah beberapa tipe data ke tipedata numerik agar dapat dianalisis lebih dalam


![distribusi score berdasarkan tipe anime](https://github.com/user-attachments/assets/d1808a34-4d36-48e4-babf-50bd83f454e4)
![hubungan antara popularity dan member](https://github.com/user-attachments/assets/733a98e6-2347-413a-a186-171c5f3b5d8a)
![hubungan anatara fav dan popular](https://github.com/user-attachments/assets/3c1885c5-cc14-4ccf-a1c3-0fdc558feb6a)
![matriks kolerasi](https://github.com/user-attachments/assets/8f1b8231-6cc7-4064-bf54-cbf5998d01ba)

1. Distribusi Skor Berdasarkan Tipe Anime Visualisasi ini menggunakan boxplot untuk menunjukkan distribusi skor pada setiap jenis (tipe) anime. Boxplot ini memvisualisasikan median, kuartil bawah dan atas, serta outliers (jika ada) dalam setiap tipe anime, yang memungkinkan kita untuk melihat variasi skor antar tipe. Dari boxplot, kita bisa membandingkan median skor antar tipe untuk melihat tipe anime mana yang cenderung memiliki skor lebih tinggi atau distribusi yang lebih luas.
2. Hubungan antara Popularitas dan Jumlah Member Scatter plot ini menunjukkan hubungan antara popularitas dan jumlah anggota (member) untuk setiap anime. Di sumbu X ada metrik popularitas, dan di sumbu Y adalah jumlah anggota. Grafik ini membantu mengidentifikasi pola, misalnya apakah anime yang lebih populer cenderung memiliki lebih banyak anggota. Jika terlihat korelasi positif, maka semakin populer sebuah anime, semakin banyak anggota yang tertarik pada anime tersebut.
3. Hubungan antara Favorit dan Popularitas Scatter plot ini menggambarkan hubungan antara jumlah favorit (favoritisme) dengan popularitas anime. Sumbu X menunjukkan popularitas, sedangkan sumbu Y menunjukkan jumlah favorit. Melalui grafik ini, kita bisa melihat apakah anime yang lebih populer cenderung menjadi favorit atau apakah terdapat beberapa anime dengan penggemar yang sangat setia meskipun popularitasnya tidak tinggi. Jika ada garis diagonal atau pola linear, itu menunjukkan korelasi antara favoritisme dan popularitas.
4. Matriks Korelasi Matriks korelasi ini menampilkan hubungan antar variabel dalam dataset anime dalam bentuk heatmap. Nilai korelasi berkisar dari -1 (korelasi negatif sempurna) hingga 1 (korelasi positif sempurna). Warna lebih gelap atau cerah di masing-masing kotak menunjukkan kekuatan korelasi antar variabel. Variabel dengan korelasi tinggi memiliki nilai mendekati 1 atau -1, yang menunjukkan hubungan linier yang kuat. Misalnya, jika terdapat korelasi tinggi antara ‘member’ dan ‘popularity’, itu menunjukkan bahwa keduanya saling berkaitan erat.

   
## Data Preparation

Sebelum memasuki data preparation terlebih dahulu menghapus beberapa kolom yang tidak diperlukan dalam analisis.

**TF-IDF**
Tahap ini adalah mengubah data kedalam representasi numerik untuk modeling Cosine Similarity agar mengukur kemiripan antar Item 

**Encoding Data user_id dan anime_id**
Encoding ini diperlukan untuk model collaborative filtering. encoding dilakukan agar model neural network dapat memproses.

**Splitting Data**
Splitiing data dilakukan untuk model collaborative filtering digunakan untuk mengevaluasi  model.


## Modeling
### Model 1 Consine Similarity
Model 1 menggunakan cosine similarity untuk memberikan rekomendasi anime dengan menghitung kemiripan antara anime berdasarkan fitur teks, seperti genre. Pertama, model menghitung nilai cosine similarity dan menyimpannya dalam DataFrame untuk akses mudah. Selanjutnya, model mengambil sampel dari DataFrame dan mencari data spesifik untuk anime yang dijadikan acuan. Fungsi yang didefinisikan menerima parameter seperti nama anime, DataFrame similarity, dan jumlah rekomendasi yang diinginkan. Fungsi ini kemudian mencari indeks anime terdekat, menghapus anime acuan dari daftar, dan mengembalikan rekomendasi anime yang relevan. Meskipun sederhana dan efektif untuk data teks, model ini memiliki keterbatasan, seperti sensitivitas terhadap data yang tidak seimbang dan kurangnya konteks dalam rekomendasi.

1. **Menghitung Cosine Similarity**: 
   Pertama, kita menghitung cosine similarity antara item-item (dalam hal ini, anime) berdasarkan representasi TF-IDF mereka. Cosine similarity digunakan untuk menentukan seberapa mirip dua vektor (vektor TF-IDF) satu sama lain, yang dihitung berdasarkan sudut antara kedua vektor tersebut.

2. **Membuat DataFrame untuk Similarity**: 
   Setelah menghitung cosine similarity, kita mengonversi matriks similarity tersebut menjadi DataFrame. Dengan menggunakan nama anime sebagai indeks dan kolom, kita dapat dengan mudah merujuk ke similarity antara anime yang berbeda.

3. **Mengambil Sampel DataFrame**: 
   Kita mengambil sampel acak dari DataFrame similarity untuk melihat beberapa nilai yang dihasilkan dan memverifikasi bahwa data terstruktur dengan benar.

4. **Mencari Data Spesifik**: 
   Mengambil informasi tentang anime tertentu, misalnya 'Cowboy Bebop', untuk memverifikasi bahwa data ada dan dapat digunakan untuk rekomendasi.

5. **Fungsi Rekomendasi Anime**: 
   Fungsi ini dirancang untuk mengambil nama anime sebagai input dan memberikan rekomendasi anime lainnya berdasarkan similarity. Parameter yang digunakan mencakup nama anime sebagai acuan, DataFrame similarity, DataFrame informasi anime, dan jumlah rekomendasi yang ingin ditampilkan.

6. **Mencari Indeks Anime Terdekat**: 
   Di sini, kita mencari indeks anime yang memiliki similarity tertinggi dengan anime yang diberikan. Kita menggunakan teknik efisien untuk menemukan indeks tanpa mengurutkan seluruh array.

7. **Menghapus Nama Anime dari Rekomendasi**: 
   Nama anime yang diberikan dihapus dari daftar rekomendasi agar tidak muncul di hasil akhir.

8. **Mengembalikan DataFrame Rekomendasi**: 
   Terakhir, kita membuat DataFrame baru yang berisi nama dan genre anime yang direkomendasikan, kemudian mengembalikan hasilnya.

**Kelebihan Model**
- **Sederhana dan Mudah Dipahami**: Model berbasis cosine similarity mudah diimplementasikan dan dimengerti, terutama bagi yang sudah familiar dengan konsep vektor.
- **Efektif untuk Data Teks**: Cocok untuk aplikasi di mana data terdiri dari teks, seperti genre anime, karena dapat menangkap kemiripan berdasarkan konten.
- **Rekomendasi yang Personalisasi**: Menggunakan informasi spesifik dari anime yang disukai pengguna untuk memberikan rekomendasi yang relevan.

**Kekurangan Model**
- **Sensitivitas terhadap Data yang Tidak Seimbang**: Jika beberapa genre lebih umum daripada yang lain, model mungkin memberikan rekomendasi yang kurang bervariasi.
- **Kurangnya Konteks**: Model hanya mempertimbangkan genre dan tidak memperhitungkan aspek lain seperti rating, popularitas, atau preferensi pengguna.
- **Skalabilitas**: Seiring bertambahnya jumlah anime, perhitungan cosine similarity dapat menjadi tidak efisien dalam hal waktu dan memori.
- **Rekomendasi yang Terbatas**: Model hanya memberikan rekomendasi berdasarkan kemiripan konten, sehingga mungkin tidak memperkenalkan pengguna pada item yang berbeda dari yang sudah mereka lihat.

**Hasil Modeling**

![Cuplikan layar 2024-11-04 154434](https://github.com/user-attachments/assets/18c8198e-99db-4bdc-a1f6-761da997e75a)

Diatas merupakan hasil dari modeling Consine Similarity dimana model diminta untuk memberikan rekomendasi anime yang mirip dengan 'Cowboy Bebop' dan model memberikan output Top-N dimana anime yang direkomendasikan memiliki genre yang mirip dengan 'Cowboy Bebop'

### Model 2 RecommenderNet
Model rekomendasi berbasis jaringan saraf ini berfungsi dengan mendefinisikan kelas yang mewarisi dari tf.keras.Model, di mana layer embedding digunakan untuk mengurangi dimensi data pengguna dan anime. Dalam proses forward pass, model menghitung dot product antara vektor pengguna dan anime, ditambah bias, untuk menghasilkan prediksi rating. Model dikompilasi dengan fungsi kerugian Binary Crossentropy dan dilatih menggunakan data latih. Setelah pelatihan, model memberikan rekomendasi anime untuk pengguna dengan memprediksi rating untuk anime yang belum ditonton, menampilkan anime dengan rating tertinggi sebagai rekomendasi. Meskipun efektif dalam menangkap pola kompleks, model ini memerlukan data besar dan bisa sulit dipahami hasilnya.

1. **Definisi Model**: 
   Model rekomendasi didefinisikan sebagai kelas yang mewarisi dari `tf.keras.Model`, memungkinkan penyesuaian dan penggunaan fungsi-fungsi yang ada dalam framework Keras.

2. **Inisialisasi Model**: 
   Pada tahap ini, parameter-parameter penting seperti jumlah pengguna, jumlah anime, dan ukuran embedding diatur. Layer embedding untuk pengguna dan anime diciptakan, termasuk bias untuk masing-masing.

3. **Layer Embedding**: 
   Layer embedding digunakan untuk mereduksi dimensi representasi pengguna dan anime. Ini memungkinkan model untuk belajar representasi yang lebih kompak dan relevan dari data yang lebih besar.

4. **Forward Pass**: 
   Dalam metode ini, model memproses input untuk menghasilkan prediksi. Vektor untuk pengguna dan anime diambil dari embedding, dan kemudian dot product antara vektor pengguna dan anime dihitung, diikuti dengan penambahan bias.

5. **Kompilasi Model**: 
   Model disiapkan untuk pelatihan dengan menentukan fungsi kerugian, optimizer, dan metrik evaluasi. Fungsi kerugian yang digunakan adalah Binary Crossentropy, yang sesuai untuk masalah klasifikasi biner.

6. **Pelatihan Model**: 
   Model dilatih menggunakan data latih yang disediakan. Parameter seperti ukuran batch dan jumlah epoch ditentukan untuk proses pelatihan. Data validasi juga digunakan untuk memantau kinerja model selama pelatihan.

7. **Mendapatkan Rekomendasi untuk Pengguna**: 
   Setelah model dilatih, langkah selanjutnya adalah mendapatkan rekomendasi untuk pengguna tertentu. Ini melibatkan pengambilan ID pengguna, anime yang sudah ditonton, dan anime yang belum ditonton untuk memprediksi rating yang mungkin diberikan oleh pengguna terhadap anime yang belum mereka tonton.

8. **Memprediksi dan Menampilkan Rekomendasi**: 
   Rating diprediksi untuk anime yang belum ditonton berdasarkan model, dan kemudian anime dengan rating tertinggi ditampilkan sebagai rekomendasi untuk pengguna. Detail anime yang telah ditonton pengguna juga disediakan untuk konteks.

**Kelebihan Model**
- **Kemampuan Menangkap Pola Kompleks**: Model ini dapat mengenali dan mempelajari pola-pola kompleks dalam data, yang dapat meningkatkan akurasi rekomendasi.
- **Representasi yang Efisien**: Layer embedding memberikan representasi yang lebih ringkas untuk pengguna dan item, yang membantu dalam proses pembelajaran.
- **Fleksibilitas dalam Skala**: Dapat dengan mudah diskalakan untuk menangani jumlah pengguna dan item yang besar, asalkan data pelatihan yang memadai tersedia.

**Kekurangan Model**
- **Kebutuhan Data yang Besar**: Memerlukan dataset yang cukup besar agar model dapat belajar secara efektif. Kurangnya data dapat menyebabkan model tidak optimal.
- **Risiko Overfitting**: Meski ada regularisasi, model masih dapat mengalami overfitting, terutama pada dataset yang lebih kecil atau tidak seimbang.
- **Kompleksitas dan Waktu Pelatihan**: Model ini lebih kompleks dan memakan waktu untuk dilatih dibandingkan metode rekomendasi yang lebih sederhana.
- **Interpretabilitas yang Rendah**: Model berbasis deep learning sering dianggap sebagai "black box," sehingga sulit untuk memahami alasan di balik rekomendasi yang diberikan.

**Hasil Modeling**

![Cuplikan layar 2024-11-04 154502](https://github.com/user-attachments/assets/afa8b140-217c-4f53-a3cb-3bb539ec5896)

Dari output diatas model mengambil sampel user secara acak kemudian memberikan 10 rekomendasi berdasarkan analisis rating anime yang telah ditonton dan anime-anime yang sudah serta belum ditonton

## Evaluation
Metrik Evaluasi untuk Model 1

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

**Evaluasi Model 2**
RMSE (Root Mean Squared Error) adalah metrik evaluasi yang digunakan untuk mengukur seberapa baik model prediksi dalam memperkirakan nilai aktual. Metrik ini menghitung akar kuadrat dari rata-rata kesalahan kuadrat antara nilai yang diprediksi oleh model dan nilai yang sebenarnya. RMSE memberikan ukuran kesalahan dalam satuan yang sama dengan variabel yang diprediksi, sehingga mudah dipahami.

$$ RMSE =  \sqrt{\frac{\sum_{t=1}^{n}(A_t - F_t)^2}{n}} $$

Dimana:

- $A_t$ : Nilai aktual
- $F_t$ : Nilai hasil prediksi
- n: Banyak data
  
![model metriks](https://github.com/user-attachments/assets/f4f7a4bf-5be6-4d13-922e-019627b6a2a5)


Hasil training cukup bagus dimana hasil akhir error pada train 0.7 dan pada test 0.25.


**Evaluasi terhadap Business Understanding**
Hasil modeling sistem rekomendasi berhasil menjawab problem statement dengan menyediakan solusi yang efektif untuk membantu pengguna menemukan judul anime yang sesuai dengan preferensi mereka. Dengan mengimplementasikan pendekatan content-based filtering dan collaborative filtering, sistem mampu menghasilkan rekomendasi anime yang relevan berdasarkan kesamaan genre dan preferensi pengguna yang terukur melalui rating. Hal ini memberikan wawasan yang mendalam mengenai interaksi pengguna dengan berbagai judul anime dan faktor-faktor yang mempengaruhi ketertarikan mereka.

Model ini berhasil mencapai goals yang diharapkan, yaitu meningkatkan kepuasan pengguna dengan merekomendasikan anime yang belum pernah ditonton dan sesuai dengan minat mereka. Dengan menggunakan cosine similarity untuk content-based filtering dan analisis preferensi pengguna melalui collaborative filtering, sistem dapat memberikan rekomendasi yang lebih personal dan relevan. Metrik precision yang digunakan untuk mengukur kinerja sistem memberikan jaminan bahwa rekomendasi yang dihasilkan memiliki kualitas yang tinggi, sehingga pengguna lebih mungkin untuk menikmati saran yang diberikan.

Solusi yang direncanakan membawa dampak signifikan terhadap strategi pemasaran dan pengembangan produk. Dengan memberikan rekomendasi yang lebih tepat dan terarah, perusahaan dapat meningkatkan engagement pengguna di platform mereka. Misalnya, dengan memahami anime mana yang paling mungkin disukai oleh pengguna, perusahaan dapat menyesuaikan konten yang ditawarkan dan mengoptimalkan kampanye pemasaran. Ini tidak hanya meningkatkan pengalaman pengguna tetapi juga berpotensi meningkatkan loyalitas pelanggan dan konversi, menciptakan keuntungan kompetitif dalam industri anime.


## Daftar Refrensi 

Muhammad Auzhae., Firmansyah Aji., & M.Syamsudin. (2023).*Rekomendasi Anime Berdasarkan Prefensi Pengguna: Studi Kasus Menggunakan Decision Tree dengan Atribut Genre, Jumlah Episode dan Rating*. diakses pada 04 November 2024 [(https://publishing-widyagama.ac.id/ejournal-v2/bcti/article/view/4885)](https://publishing-widyagama.ac.id/ejournal-v2/bcti/article/view/4885)
