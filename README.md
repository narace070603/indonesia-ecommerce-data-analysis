# Indonesia E-Commerce Sales Analysis & Interactive Dashboard

![Streamlit](https://img.shields.io/badge/Streamlit-1.66.1-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.14-3776AB?style=for-the-badge&logo=python&logoColor=white)
![React](https://img.shields.io/badge/React-18-61DAFB?style=for-the-badge&logo=react&logoColor=black)
![Three.js](https://img.shields.io/badge/Three.js-WebGL-000000?style=for-the-badge&logo=three.js&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active_Development-brightgreen?style=for-the-badge)

Aplikasi web interaktif untuk menganalisis performa data penjualan e-commerce di Indonesia secara komprehensif. Aplikasi ini menggabungkan hasil pemrosesan analitis bisnis dengan pengalaman visual modern melalui integrasi komponen kustom berbasis React WebGL (Mode Cihuy).

---

## Kelompok 7: Machine Learning

1. Kaila Rachmania Nareshwari
2. Cep Wildan Yanfa
3. Muhammad Riko Reyhand Budiman
4. Dara Ridzqitha Riyandhini
5. Rina Dwi Ariyanti
6. Indah Tri Utami
7. Nikeisha Wahyu Frieda

---

## Deskripsi Proyek

Proyek ini bertujuan untuk menganalisis dataset penjualan e-commerce di Indonesia guna memahami kategori produk berdasarkan pendapatan, tren penjualan bulanan, serta kategori produk yang paling banyak dibeli di Kabupaten Bogor.

Analisis dilakukan menggunakan Python dengan bantuan Pandas untuk pengolahan data dan Matplotlib/Plotly untuk visualisasi. Hasil analisis disajikan dalam bentuk dashboard interaktif menggunakan Streamlit yang dilengkapi opsi latar belakang animasi 3D WebGL (Mode Cihuy).

---

## Tautan Demo Live

Aplikasi ini telah dideploy dan dapat diakses langsung secara publik melalui tautan berikut:
* **Streamlit Cloud:** https://share.streamlit.io

---

## Daftar Isi

* [Kelompok 7: Machine Learning](#kelompok-7-machine-learning)
* [Deskripsi Proyek](#deskripsi-proyek)
* [Pertanyaan Analisis](#pertanyaan-analisis)
* [Dataset](#dataset)
* [Tools dan Library](#tools-dan-library)
* [Tahapan Analisis](#tahapan-analisis)
* [Visualisasi dan Analisis Insight](#visualisasi-dan-analisis-insight)
* [Fitur Utama Dashboard](#fitur-utama-dashboard)
* [Dokumentasi](#dokumentasi)
* [Kesimpulan](#kesimpulan)
* [Panduan Instalasi & Persiapan](#panduan-instalasi--persiapan)
* [Cara Menjalankan Proyek](#cara-menjalankan-proyek)
* [Struktur Folder](#struktur-folder)
* [Panduan Kontribusi](#panduan-kontribusi)
* [Lisensi](#lisensi)
* [Penutup](#penutup)

---

## Pertanyaan Analisis

1. Kategori produk apa yang menghasilkan pendapatan tertinggi?
2. Bagaimana tren penjualan bulanan pada tahun 2024?
3. Kategori produk apa yang paling banyak dibeli di Kabupaten Bogor?

---

## Dataset

Dataset yang digunakan adalah **Indonesia E-commerce Sales Challenging**, yang berisi informasi mengenai transaksi penjualan e-commerce di Indonesia.

* **Nama dataset:** Indonesia E-commerce Sales Challenging
* **Sumber:** Kaggle 
* **Link Dataset:** [Kaggle - Indonesia E-Commerce Sales](https://www.kaggle.com/datasets/zkyfauzi/indonesia-ecommerce-sales) 
* **Format:** CSV
* **Jumlah data awal:** 18.868 baris dan 19 kolom

### Kolom Utama yang Digunakan
* `product_categories`: Kategori produk yang dibeli.
* `total_pembayaran`: Total pembayaran transaksi.
* `status_pesanan`: Status pesanan.
* `total_qty`: Jumlah produk yang dibeli.
* `kota_kabupaten`: Wilayah transaksi.
* `order_date`: Tanggal transaksi.
* `order_id`: Identitas transaksi.

Dataset digunakan untuk menganalisis pendapatan berdasarkan kategori produk, tren penjualan bulanan, dan kategori produk yang paling banyak dibeli di Kabupaten Bogor.

---

## Tools dan Library

* Python
* Pandas
* NumPy
* Matplotlib & Plotly Express
* React & Three.js / WebGL (Micro Slats)
* Jupyter Notebook
* Streamlit
* Visual Studio Code
* Git dan GitHub

---

## Tahapan Analisis

### 1. Data Understanding
Memahami struktur dataset, jumlah baris dan kolom, tipe data, nilai kosong, data duplikat, serta kondisi awal data penjualan.

### 2. Data Cleaning dan Exploratory Data Analysis (EDA)
Melakukan pemeriksaan *missing value*, duplikasi, tipe data, dan nilai yang tidak valid. Selanjutnya, eksplorasi dilakukan untuk memahami distribusi kategori produk, status pesanan, wilayah, serta informasi penjualan.

### 3. Visualisasi dan Analisis Insight
Membuat tiga visualisasi utama berdasarkan pertanyaan analisis yang telah ditentukan.

---

## Visualisasi dan Analisis Insight

### Visualisasi 1: Kategori Produk dengan Pendapatan Tertinggi
Hasil analisis menunjukkan bahwa kategori **Seal / Baut / Roof** menghasilkan pendapatan tertinggi berdasarkan transaksi yang hanya memiliki satu kategori produk.

* **Insight:** Kategori tersebut menjadi kategori dengan pendapatan tertinggi dalam analisis transaksi satu kategori. Pembatasan ini digunakan agar nilai pembayaran transaksi dengan beberapa kategori tidak dihitung berulang.
* **Rekomendasi:** Kategori tersebut dapat dipertimbangkan dalam perencanaan stok dan strategi penjualan dengan tetap memperhatikan permintaan pelanggan.

### Visualisasi 2: Tren Penjualan Bulanan Tahun 2024
Analisis dilakukan terhadap transaksi berstatus selesai dari Januari hingga November 2024 untuk melihat perubahan penjualan setiap bulan.

* **Insight:** Visualisasi tren bulanan digunakan untuk mengamati perubahan penjualan selama periode Januari–November 2024.
* **Rekomendasi:** Informasi tren penjualan dapat digunakan untuk mengevaluasi perkembangan penjualan dan membantu perencanaan persediaan. Analisis ini belum mencakup Desember 2024.

### Visualisasi 3: Kategori Produk Terpopuler di Kabupaten Bogor
Hasil analisis menunjukkan bahwa kategori **Celengan** menjadi kategori yang paling banyak dibeli di Kabupaten Bogor, dengan 350 transaksi unik.

* **Insight:** Celengan merupakan kategori produk dengan jumlah transaksi unik tertinggi di Kabupaten Bogor berdasarkan hasil analisis.
* **Rekomendasi:** Penjual dapat mengevaluasi peluang promosi dan ketersediaan stok produk Celengan di wilayah Kabupaten Bogor dengan mempertimbangkan permintaan dan kondisi penjualan.

---

## Fitur Utama Dashboard

Dashboard dikembangkan menggunakan Streamlit untuk menyajikan hasil analisis penjualan e-commerce secara interaktif:

1. **Analisis Transaksi & KPI Interaktif:** Menyajikan metrik pendapatan, tren penjualan bulanan, serta visualisasi kategori produk berbasis Plotly.
2. **Kustomisasi Tampilan (Mode Cihuy):** Fitur latar belakang animasi 3D WebGL buatan kustom (React + Micro Slats) yang dapat diaktifkan atau dimatikan via sidebar.
3. **Filter Data Dinamis:** Memungkinkan pengguna menyaring data berdasarkan rentang tanggal, kategori produk, dan wilayah penjualan secara real-time.
4. **Pembersihan Data Otomatis:** Dashboard membaca data hasil pembersihan secara konsisten untuk menjamin akurasi informasi.

---

## Dokumentasi

Dokumentasi proyek mencakup seluruh tahapan analisis data, mulai dari *data understanding*, *data cleaning*, *exploratory data analysis* (EDA), visualisasi dan analisis insight, hingga pembangunan dashboard.

Seluruh proses analisis didokumentasikan dalam Jupyter Notebook di folder `notebooks/`, sedangkan ringkasan proyek, pertanyaan analisis, hasil temuan, petunjuk instalasi, dan rekomendasi disajikan di dalam berkas `README.md`.

---

## Kesimpulan

Berdasarkan hasil analisis, kategori **Seal / Baut / Roof** menghasilkan pendapatan tertinggi pada transaksi dengan satu kategori produk. Analisis tren penjualan dilakukan untuk periode Januari hingga November 2024, sedangkan kategori **Celengan** menjadi kategori yang paling banyak dibeli di Kabupaten Bogor dengan 350 transaksi unik.

Hasil analisis memberikan gambaran mengenai pola penjualan e-commerce berdasarkan kategori produk, waktu, dan wilayah. Temuan ini dapat menjadi bahan pertimbangan dalam pengambilan keputusan bisnis, tetapi belum cukup untuk menyimpulkan penyebab perubahan penjualan atau memprediksi penjualan di masa depan.

---

## Panduan Instalasi & Persiapan

### Prasyarat
Sebelum menjalankan aplikasi di lingkungan lokal, pastikan perangkat kamu telah terpasang:
* Python versi 3.10 atau yang lebih baru
* Git

### Langkah Instalasi

1. **Kloning Repositori:**
   ```bash
   git clone [https://github.com/narace070603/indonesia-ecommerce-data-analysis.git](https://github.com/narace070603/indonesia-ecommerce-data-analysis.git)
   cd indonesia-ecommerce-data-analysis
   ```

2. **Pasang Dependensi Python:**
   Jalankan perintah berikut di terminal:
   ```bash
   pip install -r requirement.txt
   ```

*(Catatan: Kamu tidak perlu menginstal Node.js atau mengeksekusi paket npm, karena bundel komponen kustom React di folder `microslats_component/build` sudah dikompilasi secara permanen di dalam repositori ini).*

---

## Cara Menjalankan Proyek

Untuk menjalankan dashboard di komputer lokal kamu, gunakan perintah berikut di terminal:

```bash
python -m streamlit run app.py
```

Setelah perintah dijalankan, peramban web akan terbuka secara otomatis di alamat `http://localhost:8501`.

### Fitur Mode Tampilan
1. Buka menu navigasi di bagian kiri (*sidebar*).
2. Pilih mode antarmuka: **Normal** untuk tampilan standar analitis, atau **Mode Cihuy** untuk mengaktifkan pengalaman latar belakang animasi 3D WebGL.

---

## Struktur Folder

Berikut susunan direktori resmi proyek berdasarkan repositori:

```text
indonesia-ecommerce-data-analysis/
├── .devcontainer/
│   └── devcontainer.json        # Konfigurasi lingkungan pengembangan
├── assets/                      # Berkas gambar dan materi visual dashboard
│   ├── image.png
│   └── image2.png
├── data/                        # Manajemen dataset proyek
│   ├── clean/                   # Dataset hasil pembersihan (siap pakai)
│   │   └── indonesia_ecommerce_sales_clean.csv
│   ├── preparation/             # Dataset olahan intermediate / fitur spesifik
│   │   ├── data_jumlah_barang_kabupaten_bogor.csv
│   │   ├── data_kategori_kabupaten_bogor.csv
│   │   ├── data_tren_tahunan.csv
│   │   └── indonesia_ecommerce_sales_selesai.csv
│   └── raw/                     # Dataset mentah sebelum diproses
│       └── indonesia_ecommerce_sales_challenging.csv
├── microslats_component/        # Komponen kustom React WebGL (Mode Cihuy)
│   ├── build/                   # Hasil kompilasi bundel WebGL siap pakai
│   │   ├── assets/
│   │   └── index.html
│   ├── node_modules/
│   ├── index.html
│   ├── index.jsx
│   ├── MicroSlats.css
│   ├── MicroSlats.jsx
│   ├── package-lock.json
│   ├── package.json
│   └── vite.config.js
├── notebooks/                   # Jupyter Notebook untuk eksplorasi & analisis data
│   ├── 01_data_understanding.ipynb
│   └── 02_analysis_data.ipynb
├── streamlit/                   # Konfigurasi tema dan gaya kustom Streamlit
│   ├── config.toml
│   └── TechText.css
├── app.py                       # Berkas utama aplikasi Streamlit
├── README.md                    # Berkas dokumentasi utama proyek
└── requirement.txt              # Daftar pustaka Python yang dibutuhkan
```

---

## Panduan Kontribusi

Kontribusi dari anggota tim sangat dialu-alukan. Untuk membuat Pull Request:

1. Buat cabang (*branch*) baru dari `main`:
   ```bash
   git checkout -b fitur-baru-kamu
   ```
2. Lakukan perubahan kode dan buat commit yang jelas:
   ```bash
   git commit -m "feat: tambahkan fitur visualisasi baru"
   ```
3. Unggah perubahan ke repositori:
   ```bash
   git push origin fitur-baru-kamu
   ```
4. Kirimkan *Pull Request* (PR) ke cabang `main` di repositori GitHub kelompok.

---

## Lisensi

Proyek ini dibuat untuk keperluan akademik dan analisis internal kelompok. Seluruh hak cipta penggunaan kode disesuaikan dengan ketentuan tim pengembang.

---

## Penutup

Proyek ini menerapkan proses analisis data menggunakan Python, mulai dari memahami dan membersihkan dataset, melakukan eksplorasi data, membuat visualisasi, menyusun insight dan rekomendasi, hingga membangun dashboard interaktif berbasis Streamlit serta mendokumentasikan hasil analisis secara rapi.

Melalui proyek ini, diharapkan pola penjualan e-commerce dapat dipahami berdasarkan kategori produk, tren bulanan, dan wilayah transaksi. Hasil analisis dapat menjadi gambaran awal untuk mendukung evaluasi dan pengambilan keputusan bisnis berbasis data.