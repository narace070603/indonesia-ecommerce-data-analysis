# Indonesia E-Commerce Sales Analysis & Interactive Dashboard

![Streamlit](https://img.shields.io/badge/Streamlit-1.66.1-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.14-3776AB?style=for-the-badge&logo=python&logoColor=white)
![React](https://img.shields.io/badge/React-18-61DAFB?style=for-the-badge&logo=react&logoColor=black)
![Three.js](https://img.shields.io/badge/Three.js-WebGL-000000?style=for-the-badge&logo=three.js&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active_Development-brightgreen?style=for-the-badge)

Aplikasi web interaktif untuk menganalisis performa data penjualan e-commerce di Indonesia secara komprehensif. Proyek ini menyajikan temuan analitis bisnis utama, visualisasi tren transaksi, serta integrasi komponen khusus berbasis React WebGL (Mode Cihuy) untuk memberikan pengalaman visual modern.

---

## Tautan Demo Live

Aplikasi ini telah dideploy dan dapat diakses langsung secara publik melalui tautan berikut:
* **Streamlit Cloud:** https://share.streamlit.io

---

## Daftar Isi

* [Gambaran Umum Dataset](#gambaran-umum-dataset)
* [Pertanyaan Bisnis & Hasil Analisis](#pertanyaan-bisnis--hasil-analisis)
* [Fitur Dashboard](#fitur-dashboard)
* [Tumpukan Teknologi & Alat](#tumpukan-teknologi--alat)
* [Tahapan Analisis Data](#tahapan-analisis-data)
* [Panduan Instalasi & Persiapan](#panduan-instalasi--persiapan)
* [Cara Penggunaan](#cara-penggunaan)
* [Struktur Folder](#struktur-folder)
* [Panduan Kontribusi](#panduan-kontribusi)
* [Lisensi](#lisensi)
* [Tim Pengembang](#tim-pengembang)

---

## Gambaran Umum Dataset

Dataset yang digunakan dalam analisis ini adalah **Indonesia E-commerce Sales Challenging**, yang berisi data transaksi penjualan e-commerce di Indonesia.

* **Nama Dataset:** Indonesia E-commerce Sales Challenging
* **Sumber:** Kaggle
* **Link Dataset:** [Kaggle - Indonesia E-Commerce Sales](https://www.kaggle.com/datasets/zkyfauzi/indonesia-ecommerce-sales)
* **Format File:** CSV
* **Jumlah Data Awal:** 18.868 baris dan 19 kolom

### Kolom Utama yang Digunakan
* `product_categories`: Kategori produk yang dibeli.
* `total_pembayaran`: Total pembayaran transaksi.
* `status_pesanan`: Status pesanan transaksi.
* `total_qty`: Jumlah produk yang dibeli.
* `kota_kabupaten`: Wilayah lokasi transaksi.
* `order_date`: Tanggal terjadinya transaksi.
* `order_id`: Identitas unik transaksi.

---

## Pertanyaan Bisnis & Hasil Analisis

### Visualisasi 1: Kategori Produk dengan Pendapatan Tertinggi
* **Hasil:** Kategori **Seal / Baut / Roof** menghasilkan pendapatan tertinggi berdasarkan analisis transaksi yang hanya memiliki satu kategori produk.
* **Insight:** Pembatasan analisis pada transaksi satu kategori dilakukan agar nilai pembayaran transaksi yang memiliki beberapa kategori tidak dihitung secara berulang.
* **Rekomendasi:** Kategori ini perlu diprioritaskan dalam perencanaan stok dan strategi penjualan dengan tetap memperhatikan tren permintaan pelanggan.

### Visualisasi 2: Tren Penjualan Bulanan Tahun 2024
* **Hasil:** Evaluasi dilakukan terhadap transaksi berstatus *selesai* dari Januari hingga November 2024 untuk melihat dinamika penjualan setiap bulan.
* **Insight:** Grafik tren bulanan membantu mengamati naik-turunnya volume dan nilai penjualan secara historis selama periode Januari–November 2024.
* **Rekomendasi:** Informasi tren dapat dimanfaatkan untuk evaluasi kinerja bulanan dan membantu efisiensi perencanaan persediaan gudang. *(Catatan: Data belum mencakup bulan Desember 2024)*.

### Visualisasi 3: Kategori Produk Terpopuler di Kabupaten Bogor
* **Pertanyaan Bisnis:** Kategori produk apa yang paling banyak dibeli di Kabupaten Bogor?
* **Hasil:** Kategori **Celengan** menjadi produk terpopuler di Kabupaten Bogor dengan mencatatkan **350 transaksi unik**.
* **Insight:** Celengan merupakan kategori produk dengan jumlah transaksi unik tertinggi di wilayah Kabupaten Bogor.
* **Rekomendasi:** Penjual dapat memanfaatkan temuan ini untuk mengevaluasi promosi wilayah dan menjaga ketersediaan stok produk Celengan khusus di area Kabupaten Bogor.

---

## Fitur Dashboard

1. **Visualisasi Data Interaktif:** Menyajikan metrik pendapatan, tren penjualan bulanan, dan produk populer menggunakan grafik Plotly yang dinamis.
2. **Kustomisasi Tampilan (Mode Cihuy):** Fitur latar belakang animasi 3D WebGL buatan kustom (React + Micro Slats) yang dapat diaktifkan atau dimatikan via sidebar.
3. **Filter Data Dinamis:** Memungkinkan pengguna menyaring data berdasarkan rentang tanggal, kategori produk, dan wilayah penjualan secara real-time.
4. **Pembersihan Data Otomatis:** Dashboard membaca data hasil pembersihan secara konsisten untuk menjamin akurasi informasi yang ditampilkan.

---

## Tumpukan Teknologi & Alat

* **Bahasa Pemrograman:** Python 3.x
* **Pengolahan & Analisis Data:** Pandas, NumPy
* **Visualisasi Data:** Plotly Express, Matplotlib
* **Kerangka Kerja Dashboard:** Streamlit
* **Komponen Antarmuka Kustom:** React, Tailwind CSS, Three.js / WebGL (Micro Slats)
* **Lingkungan Pengembangan:** Jupyter Notebook, Visual Studio Code
* **Manajemen Kode & Deployment:** Git, GitHub, Streamlit Community Cloud

---

## Tahapan Analisis Data

1. **Data Understanding:** Memahami struktur dataset, ketersediaan baris dan kolom, tipe data, deteksi nilai kosong (*missing values*), data duplikat, serta gambaran awal transaksi.
2. **Data Cleaning & EDA:** Melakukan penanganan *missing values*, penghapusan duplikasi, perbaikan tipe data, serta filtering transaksi valid untuk eksplorasi distribusi kategori dan wilayah.
3. **Visualisasi & Analisis Insight:** Menyusun visualisasi dan menarik kesimpulan bisnis untuk menjawab pertanyaan seputar pendapatan, tren bulanan, dan potensi pasar regional.
4. **Pengembangan Dashboard:** Membangun antarmuka web interaktif menggunakan Streamlit agar hasil analisis mudah dipahami oleh pemangku kepentingan.

---

## Panduan Instalasi & Persiapan

### Prasyarat
Pastikan perangkat kamu sudah terpasang:
* Python versi 3.10 atau yang lebih baru
* Git

### Langkah Instalasi

1. **Kloning Repositori:**
   ```bash
   git clone [https://github.com/narace070603/indonesia-ecommerce-data-analysis.git](https://github.com/narace070603/indonesia-ecommerce-data-analysis.git)
   cd indonesia-ecommerce-data-analysis
Pasang Dependensi Python:
Jalankan perintah berikut di terminal:

Bash
pip install -r requirement.txt
(Catatan: Kamu tidak perlu menginstal Node.js atau mengeksekusi perintah npm, karena bundel komponen kustom React pada folder microslats_component/build sudah dikompilasi secara permanen di dalam repositori ini).

Cara Penggunaan
Jalankan perintah berikut di terminal komputer kamu:

Bash
python -m streamlit run app.py
Peramban web akan otomatis terbuka di alamat http://localhost:8501.

Fitur Mode Tampilan
Buka menu navigasi di sisi kiri (sidebar).

Pilih mode antarmuka: Normal untuk tampilan analitis standar, atau Mode Cihuy untuk mengaktifkan pengalaman latar belakang animasi 3D WebGL.

Struktur Folder
Berikut susunan direktori resmi dari repositori ini:

Plaintext
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
└── README.md
└── requirement.txt              # Daftar pustaka Python yang dibutuhkan

Panduan Kontribusi
Kontribusi dari anggota tim sangat dialu-alukan. Untuk mengirimkan fitur baru:

Buat branch baru dari main:

Bash
git checkout -b fitur-dashboard
Simpan dan buat commit atas perubahan kode:

Bash
git commit -m "feat: add dashboard layout, WebGL mode, and updated README"
Unggah branch ke repositori:

Bash
git push origin fitur-dashboard
Buka halaman GitHub repositori kelompok dan buat Pull Request (PR) ke branch main.

Lisensi
Proyek ini dibuat untuk keperluan akademik dan analisis internal kelompok. Seluruh hak cipta penggunaan kode disesuaikan dengan ketentuan tim pengembang.

Tim Pengembang
Kelompok Analisis Data E-Commerce - Pemrosesan Data, Visualisasi Analisis, Pengembangan Dashboard Streamlit, dan Integrasi Komponen WebGL.