# Indonesia E-commerce Sales Analysis

## Kelompok 7: Machine Learning

1. Kaila Rachmania Nareshwari
2. Cep Wildan Yanfa
3. Muhammad Riko Reyhand Budiman
4. Dara Ridzqitha Riyandhini
5. Rina Dwi Ariyanti
6. Indah Tri Utami
7. Nikeisha Wahyu Frieda

## Deskripsi Proyek

Proyek ini bertujuan untuk menganalisis dataset penjualan e-commerce di Indonesia guna memahami kategori produk berdasarkan pendapatan, tren penjualan bulanan, serta kategori produk yang paling banyak dibeli di Kabupaten Bogor.

Analisis dilakukan menggunakan Python dengan bantuan Pandas untuk pengolahan data dan Matplotlib untuk visualisasi. Hasil analisis juga disajikan dalam bentuk dashboard interaktif menggunakan Streamlit.

## Pertanyaan Analisis

1. Kategori produk apa yang menghasilkan pendapatan tertinggi?
2. Bagaimana tren penjualan bulanan pada tahun 2024?
3. Kategori produk apa yang paling banyak dibeli di Kabupaten Bogor?

## Dataset

Dataset yang digunakan adalah **Indonesia E-commerce Sales Challenging**, yang berisi informasi mengenai transaksi penjualan e-commerce di Indonesia.

- **Nama dataset:** Indonesia E-commerce Sales Challenging
- **Sumber:** Kaggle 
- **Link:** https://www.kaggle.com/datasets/zkyfauzi/indonesia-ecommerce-sales 
- **Format:** CSV
- **Jumlah data awal:** 18.868 baris dan 19 kolom

Kolom utama yang digunakan meliputi:

- `product_categories`: Kategori produk yang dibeli.
- `total_pembayaran`: Total pembayaran transaksi.
- `status_pesanan`: Status pesanan.
- `total_qty`: Jumlah produk yang dibeli.
- `kota_kabupaten`: Wilayah transaksi.
- `order_date`: Tanggal transaksi.
- `order_id`: Identitas transaksi.

Dataset digunakan untuk menganalisis pendapatan berdasarkan kategori produk, tren penjualan bulanan, dan kategori produk yang paling banyak dibeli di Kabupaten Bogor.

## Tools dan Library

- Python
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook
- Streamlit
- Visual Studio Code
- Git dan GitHub

## Tahapan Analisis

### 1. Data Understanding

Memahami struktur dataset, jumlah baris dan kolom, tipe data, nilai kosong, data duplikat, serta kondisi awal data penjualan.

### 2. Data Cleaning dan Exploratory Data Analysis (EDA)

Melakukan pemeriksaan *missing value*, duplikasi, tipe data, dan nilai yang tidak valid. Selanjutnya, eksplorasi dilakukan untuk memahami distribusi kategori produk, status pesanan, wilayah, serta informasi penjualan.

### 3. Visualisasi dan Analisis Insight

Membuat tiga visualisasi berdasarkan pertanyaan analisis yang telah ditentukan.

#### Visualisasi 1: Kategori Produk dengan Pendapatan Tertinggi

Hasil analisis menunjukkan bahwa kategori **Seal / Baut / Roof** menghasilkan pendapatan tertinggi berdasarkan transaksi yang hanya memiliki satu kategori produk.

**Insight:** Kategori tersebut menjadi kategori dengan pendapatan tertinggi dalam analisis transaksi satu kategori. Pembatasan ini digunakan agar nilai pembayaran transaksi dengan beberapa kategori tidak dihitung berulang.

**Rekomendasi:** Kategori tersebut dapat dipertimbangkan dalam perencanaan stok dan strategi penjualan dengan tetap memperhatikan permintaan pelanggan.

#### Visualisasi 2: Tren Penjualan Bulanan Tahun 2024

Analisis dilakukan terhadap transaksi berstatus selesai dari Januari hingga November 2024 untuk melihat perubahan penjualan setiap bulan.

**Insight:** Visualisasi tren bulanan digunakan untuk mengamati perubahan penjualan selama periode Januari–November 2024.

**Rekomendasi:** Informasi tren penjualan dapat digunakan untuk mengevaluasi perkembangan penjualan dan membantu perencanaan persediaan. Analisis ini belum mencakup Desember 2024.

#### Visualisasi 3: Kategori Produk Terpopuler di Kabupaten Bogor

Hasil analisis menunjukkan bahwa kategori **Celengan** menjadi kategori yang paling banyak dibeli di Kabupaten Bogor, dengan 350 transaksi unik.

**Insight:** Celengan merupakan kategori produk dengan jumlah transaksi unik tertinggi di Kabupaten Bogor berdasarkan hasil analisis.

**Rekomendasi:** Penjual dapat mengevaluasi peluang promosi dan ketersediaan stok produk Celengan di wilayah Kabupaten Bogor dengan mempertimbangkan permintaan dan kondisi penjualan.

## Dashboard

Dashboard dikembangkan menggunakan Streamlit untuk menyajikan hasil analisis penjualan e-commerce secara interaktif. Dashboard ini bertujuan memudahkan pengguna dalam memahami informasi pendapatan, tren penjualan, dan kategori produk berdasarkan wilayah.

Dashboard menampilkan indikator utama penjualan (KPI), filter tahun dan wilayah, visualisasi pendapatan berdasarkan kategori produk, grafik tren penjualan bulanan, serta kategori produk terpopuler di Kabupaten Bogor.

## Dokumentasi

Dokumentasi proyek mencakup tahapan analisis data, mulai dari *data understanding*, *data cleaning*, *exploratory data analysis* (EDA), visualisasi dan analisis insight, hingga pembangunan dashboard.

Seluruh proses analisis didokumentasikan dalam Jupyter Notebook, sedangkan ringkasan proyek, pertanyaan analisis, hasil temuan, dan rekomendasi disajikan dalam README.md.

## Kesimpulan

Berdasarkan hasil analisis, kategori Seal / Baut / Roof menghasilkan pendapatan tertinggi pada transaksi dengan satu kategori produk. Analisis tren penjualan dilakukan untuk periode Januari hingga November 2024, sedangkan kategori Celengan menjadi kategori yang paling banyak dibeli di Kabupaten Bogor dengan 350 transaksi unik.

Hasil analisis memberikan gambaran mengenai pola penjualan e-commerce berdasarkan kategori produk, waktu, dan wilayah. Temuan ini dapat menjadi bahan pertimbangan dalam pengambilan keputusan bisnis, tetapi belum cukup untuk menyimpulkan penyebab perubahan penjualan atau memprediksi penjualan di masa depan.

## Cara Menjalankan Proyek

[BELUM DIISI]

## Penutup

Proyek ini menerapkan proses analisis data menggunakan Python, mulai dari memahami dan membersihkan dataset, melakukan eksplorasi data, membuat visualisasi, menyusun insight dan rekomendasi, hingga membangun dashboard serta mendokumentasikan hasil analisis.

Melalui proyek ini, diharapkan pola penjualan e-commerce dapat dipahami berdasarkan kategori produk, tren bulanan, dan wilayah transaksi. Hasil analisis dapat menjadi gambaran awal untuk mendukung evaluasi dan pengambilan keputusan bisnis berbasis data.
