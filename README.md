# Day35-DockerIntroduction18
# Overview

Proyek ini adalah proyek untuk melakukan ETL sederhana. Proyek ini melibatkan teknologi berikut:
-Bahasa pemrograman Python
-Docker
-PostgreSQL
direktori data: berisi semua data yang sudah diunduh dari https://www.kaggle.com/datasets/datascientistanna/customers-dataset
direktori etl: berisi semua skrip python yang digunakan untuk melakukan ETL
ETL (Extract, Transform, Load)
Ini adalah langkah-langkah ETL yang saya gunakan:

# ETL (Extract, Transfrom and Load)
## Ectract
Tahap ekstraksi digunakan untuk mengekstrak data dari sumber data. Karena dalam database ini kita hanya memiliki satu format data, maka saya hanya menggunakan perpustakaan pandas untuk mengekstrak data dari csv ke data frame dan mengembalikan data frame tersebut.

## Transform
Setelah data diekstraksi, tahap transformasi dilakukan untuk memodifikasi data sesuai kebutuhan. Transformasi ini mencakup berbagai operasi seperti pengubahan format data, perhitungan nilai tambahan, pembersihan data, dan penggabungan data. Dalam skrip tersebut, beberapa transformasi dilakukan, seperti penentuan kategori pendapatan berdasarkan nilai pendapatan tahunan dan penentuan kelompok umur berdasarkan rentang umur tertentu. Hasil transformasi akan memastikan bahwa data siap digunakan untuk analisis lebih lanjut atau aplikasi bisnis.

## Load
Tahap terakhir adalah pemuatan data, di mana data yang telah diekstraksi dan diubah dimuat ke dalam sistem penyimpanan yang permanen. Dalam skrip tersebut, data dimuat ke dalam tabel baru "transformed_customers" dalam database PostgreSQL. Tabel baru dibuat dengan menggunakan perintah SQL CREATE TABLE, dan struktur tabel ditentukan berdasarkan data hasil transformasi. Data hasil transformasi dimasukkan ke dalam tabel baru menggunakan perintah SQL INSERT INTO, sehingga data disimpan secara permanen dalam sistem.

