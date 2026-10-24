# E-Commerce Performance Dashboard & Interactive Analytics

![Streamlit](https://img.shields.io/badge/Streamlit-1.66.1-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.14-3776AB?style=for-the-badge&logo=python&logoColor=white)
![React](https://img.shields.io/badge/React-18-61DAFB?style=for-the-badge&logo=react&logoColor=black)
![Three.js](https://img.shields.io/badge/Three.js-WebGL-000000?style=for-the-badge&logo=three.js&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active_Development-brightgreen?style=for-the-badge)

Aplikasi web interaktif untuk menganalisis performa data penjualan e-commerce secara komprehensif. Aplikasi ini menggabungkan visualisasi data analitis dengan pengalaman visual modern melalui integrasi komponen khusus berbasis React WebGL (Mode Cihuy).

---

## Tautan Demo Live

Aplikasi ini telah dideploy dan dapat diakses langsung secara publik melalui tautan berikut:
* **Streamlit Cloud:** https://share.streamlit.io

---

## Daftar Isi

* [Fitur Utama](#fitur-utama)
* [Tumpukan Teknologi](#tumpukan-teknologi)
* [Panduan Instalasi & Persiapan](#panduan-instalasi--persiapan)
* [Cara Penggunaan](#cara-penggunaan)
* [Struktur Folder](#struktur-folder)
* [Panduan Kontribusi](#panduan-kontribusi)
* [Lisensi](#lisensi)
* [Tim Pengembang](#tim-pengembang)

---

## Fitur Utama

1. **Analisis Transaksi Interaktif:** Menampilkan metrik utama penjualan, pendapatan, tren waktu, dan distribusi wilayah menggunakan grafik Plotly yang responsif.
2. **Kustomisasi Tampilan (Mode Cihuy):** Fitur latar belakang animasi 3D/WebGL buatan kustom yang dibangun dengan React dan Micro Slats, dapat diaktifkan atau dimatikan secara fleksibel melalui sidebar.
3. **Filter Data Dinamis:** Memungkinkan pengguna menyaring data berdasarkan rentang tanggal, kategori produk, dan wilayah penjualan secara real-time.
4. **Pembersihan Data Otomatis:** Sistem membaca data dari alur pemrosesan yang telah dibersihkan secara konsisten untuk memastikan akurasi visualisasi.

---

## Tumpukan Teknologi

* **Bahasa Pemrograman Utama:** Python 3.x
* **Kerangka Kerja Dashboard:** Streamlit
* **Visualisasi Data:** Plotly Express, Pandas, NumPy
* **Komponen Antarmuka Kustom:** React, Tailwind CSS, Three.js / WebGL (Micro Slats)
* **Manajemen Kode & Deployment:** Git, GitHub, Streamlit Community Cloud

---

## Panduan Instalasi & Persiapan

### Prasyarat
Sebelum menjalankan aplikasi di lingkungan lokal, pastikan perangkat kamu telah terpasang:
* Python versi 3.10 atau yang lebih baru
* Git

### Langkah Instalasi

1. **Kloning Repositori:**
   ```bash
   git clone https://github.com/narace070603/indonesia-ecommerce-data-analysis.git
   cd indonesia-ecommerce-data-analysis
   ```

2. **Pasang Dependensi Python:**
   Jalankan perintah berikut untuk menginstal seluruh pustaka yang dibutuhkan:
   ```bash
   pip install -r requirement.txt
   ```

*(Catatan: Kamu tidak perlu menginstal Node.js atau mengeksekusi paket npm, karena bundel komponen kustom React di folder `microslats_component/build` sudah dikompilasi secara permanen di dalam repositori ini).*

---

## Cara Penggunaan

Untuk menjalankan dashboard di komputer lokal kamu, gunakan perintah berikut di terminal:

```bash
python -m streamlit run app.py
```

Setelah perintah dijalankan, peramban web akan terbuka secara otomatis di alamat `http://localhost:8501`.

### Fitur Mode Tampilan
1. Buka menu navigasi di bagian kiri (sidebar).
2. Pilih mode antarmuka: **Normal** untuk tampilan standar analitis, atau **Mode Cihuy** untuk mengaktifkan pengalaman latar belakang animasi 3D WebGL.

---

## Struktur Folder

Berikut adalah gambaran susunan direktori resmi proyek ini berdasarkan repositori:

```text
indonesia-ecommerce-data-dashboard/
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
└── requirement.tx               # Daftar pustaka Python yang dibutuhkan
```

---

## Panduan Kontribusi

Kontribusi dari anggota tim atau pengembang luar sangat dialu-alukan. Untuk berkontribusi:

1. Buat fork dari repositori ini atau buat cabang (branch) baru dari `main`:
   ```bash
   git checkout -b fitur-baru-kamu
   ```
2. Lakukan perubahan kode dan buat commit yang jelas:
   ```bash
   git commit -m "feat: menambahkan visualisasi distribusi wilayah"
   ```
3. Unggah perubahan ke repositori:
   ```bash
   git push origin fitur-baru-kamu
   ```
4. Kirimkan Pull Request (PR) ke cabang `main` untuk direview bersama.

---

## Lisensi

Proyek ini dibuat untuk keperluan akademik dan analisis internal kelompok. Seluruh hak cipta penggunaan kode disesuaikan dengan ketentuan tim pengembang.

---

## Tim Pengembang

* **Raja Jamsut & Tim** - Pengembangan Dashboard, Integrasi WebGL, Analisis Data, dan Pengolahan Visualisasi.