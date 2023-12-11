# Klasifikasi Batu Gunting Kertas (Rock-Paper-Scissors) dengan Model CNN

Klasifikasi RPS (Rock-Paper-Scissors) adalah aplikasi web yang memungkinkan pengguna untuk mengunggah gambar dan menggunakan model pembelajaran mesin CNN untuk memprediksi apakah gambar tersebut merupakan batu, kertas, atau gunting.

## Instalasi
python version >= 3.10
Clone repositori ini
```git clone https://github.com/clarissa-sanindita/praktikum-ml-deploy```
Masuk ke direktori repositori
Buat sebuah venv
```python -m venv ./rpsvenv```
Aktifkan venv
- Command Prompt
```./rpesvenv/Scripts/activate.bat```
- Powershell
```./rpesvenv/Scripts/activate.ps```

Setelah itu install semua requirements
```pip install -r requirements```
Lalu jalankan flask
```python app.py```

Web dapat diakses dengan url ```localhost:5000```

## Dataset

Proyek ini memanfaatkan dataset Rock-Paper-Scissors yang berisi total 2520 gambar. Untuk memuat gambar, digunakan fungsi image_dataset_from_directory dari library TensorFlow, dengan pembagian dataset menjadi 70% untuk pelatihan, 15% untuk validasi, dan 15% untuk pengujian. Dataset ini diklasifikasikan dengan label kategori karena terdapat tiga label yang berbeda. Ukuran gambar yang digunakan adalah (150, 150) dan ukuran batch yang dipilih adalah 32.


## Teknologi yang Digunakan

- Flask sebagai framework web.
- TensorFlow dan Keras untuk model pembelajaran mesin.
- HTML, CSS, dan JavaScript untuk frontend.


## Model CNN

Model yang digunakan dalam aplikasi ini adalah Convolutional Neural Network (CNN). CNN adalah jenis jaringan saraf yang sangat efektif untuk analisis gambar. Model ini dilatih dengan dataset gambar batu, kertas, dan gunting untuk mengenali dan membedakan antara ketiga kategori tersebut.

**Accuracy Model**
![plotacc](https://github.com/clarissa-sanindita/praktikum-ml-deploy/assets/71714506/7671dd79-b79c-441b-a139-50f24d79b169)

**Graph Loss**
![plotloss](https://github.com/clarissa-sanindita/praktikum-ml-deploy/assets/71714506/1e32db8a-7440-4b77-8f1f-0c1a6e256733)

**Evaluasi dengan Laporan Klasifikasi**
![report](https://github.com/clarissa-sanindita/praktikum-ml-deploy/assets/71714506/d5dd8b71-2d69-4199-845a-e4858643ec77)

## Cara Penggunaan

Untuk menggunakan aplikasi, ikuti langkah-langkah berikut:

1. Buka aplikasi di web browser.
2. Pilih model yang ingin digunakan dari dropdown menu.
3. Unggah gambar yang ingin diprediksi.
4. Klik tombol 'Execute' untuk mendapatkan hasil prediksi.

## 👩‍💻Authors
[@clarissa-sanindita](https://www.github.com/clarissa-sanindita)
