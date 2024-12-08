# Sistem Deteksi Slot Parkir Mobil dengan YOLOv5 Berbasis Raspberry Pi 4
**Project akhir mata kuliah Edge Intelligence and Computing - B**

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
### Persiapan Komponen
- **Raspberry Pi 4** : Edge device untuk proses deteksi slot parkir secara real-time.
- **Webcam** : Input video real-time untuk deteksi slot parkir. 
- **Power Adaptor** : Sumber daya sistem.
- **Tripod** : Menopang dan menstabilkan posisi webcam (Posisi yang stabil direkomendasikan agar inferensi berjalan dengan baik dan stabil)

### Persiapan Perangkat Lunak
- **Python 3.8 atau lebih baru** 
- **Flask Library** : Framework web untuk dashboard.
- **Flask-SocketIO** : Integrasi WebSocket untuk update data secara real-time.
- **OpenCV Library** : Menangkap video dari webcam dan menampilkan frame.
- **Model YOLOv5 (You Only Look Once v5)**
- **CSV** : Mencatat log parkir.

## Arsitektur Umum

## Tampilan Dashboard

## Demo

## Kesimpulan
