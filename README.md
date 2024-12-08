# Sistem Deteksi Slot Parkir Mobil dengan YOLOv5 Berbasis Raspberry Pi 4
**Project akhir mata kuliah Edge Intelligence and Computing - B**
![cover](assets/cover.jpg)

## Anggota Kelompok : ##
- **Virandy Bagaskara Syahwanto** - *215150307111028*
- **Rafi Athallah Kurniawan** - *215150307111030*
- **Ariajuna Yodyatara** - *215150301111025*
- **Yusril Ihza Ariyono** - *215150301111030*
- **Wafdannur Ramadhan** - *215150307111024*

## Project Domain
Proyek berfokus pada sistem deteksi slot parkir pintar yang menggunakan YOLOv5 untuk deteksi objek secara real-time. Sistem ini mendeteksi slot parkir yang kosong dan terisi dari video langsung, mencatat hasilnya, dan menampilkan data melalui dashboard web.

## Dasar Masalah
- Kurangnya informasi real-time slot parkir.
- Efisiensi pengelolaan parkir rendah.
- Keterbatasan sumber daya manusia.

## Solusi
- Menyediakan informasi real-time mengenai ketersediaan slot parkir.
- Memberikan kemudahan untuk pengelolaan sistem parkir.
- Implementasi AI untuk membantu pengelolaan parkir.

## Prasyarat
### Struktur Direktori Proyek

![Struktur File](assets/struktur-file-proyek.png)

### Persiapan Komponen
- **Raspberry Pi 4** : Edge device untuk proses deteksi slot parkir secara real-time.
- **Webcam** : Input video real-time untuk deteksi slot parkir. 
- **Power Adaptor** : Sumber daya sistem.
- **Tripod** : Menopang dan menstabilkan posisi webcam (Posisi yang stabil direkomendasikan agar inferensi berjalan dengan baik dan stabil)
- **Koneksi Internet** : Pastikan Raspberry Pi dan perangkat lain terhubung dalam satu jaringan yang sama.

### Persiapan Perangkat Lunak
- **Raspberry Pi OS** : Sistem operasi Raspberry Pi
- **Python 3.8 atau lebih baru** 
- **Flask Library** : Framework web untuk dashboard.
- **Flask-SocketIO Library** : Integrasi WebSocket untuk update data secara real-time.
- **OpenCV Library** : Menangkap video dari webcam dan menampilkan frame.
- **Ultralytics Library** : Menjalankan model YOLO.
- **Model YOLOv5 (You Only Look Once v5)**
- **CSV** : Mencatat log parkir.

Untuk menginstall library yang digunakan pada sistem, jalankan perintah :

`pip install -r requirements.txt`

## Arsitektur Umum
![Arsitektur Umum Sistem](assets/arsitektur.jpg)

## Tampilan Dashboard
![Dashboard](assets/dashboard.png)

## Demo
### Setup ###
- Hubungkan webcam ke Raspberry Pi.
- Hidupkan Raspberry Pi yang sudah diinstall dengan Raspberry OS.
- Pastikan Raspberry Pi terhubung dengan jaringan internet.
- Jika belum menginstall Python 3 dan pip pada Raspberry Pi, maka jalankan perintah :

`sudo apt update` 

`sudo apt install python3 python3-pip`

- Lalu, install git untuk melakukan clone repository :

`sudo apt install git`

- Lakukan clone repository, jalankan perintah :

`https://github.com/randybagaskr25/parking-slot-detection-edge-b.git`

`cd parking-slot-detection-edge-b`

- Install depedensi yang tercantum pada requirements.txt :

`pip install -r requirements.txt`

- Setelah memastikan semua telah terhubung dan terinstall, selanjutnya jalankan app.py :

`python app.py`

- Setelah menjalankan app.py, akses web dashboard dengam alamat yang muncul pada terminal.

Contoh :

`http://127.0.0.1:5000`

atau

`http://172.20.10.6:5000`

- Jika ingin keluar dari program, tekan CTRL + C.

Berikut merupakan video demo sistem :

[Demo Sistem](assets/demo.mp4)

## Kesimpulan
Proyek ini berhasil menciptakan sistem deteksi slot parkir real-time yang menggunakan model YOLO, dihubungkan dengan aplikasi web berbasis Flask dan SocketIO untuk menampilkan informasi jumlah slot kosong dan terisi secara langsung ke dashboard web. Selain itu, sistem ini mencatat hasil deteksi dalam file log CSV untuk analisis lebih lanjut. Meskipun deteksi dilakukan dengan cepat dan akurat, tantangan tetap ada pada kualitas gambar dan akurasi dalam kondisi lingkungan yang bervariasi.
