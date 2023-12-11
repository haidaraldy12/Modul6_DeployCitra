# Modul6_DeployCitra
Python Website Modul 6


#Klasifikasi permainan Batu Gunting Kertas
Proyek Klasifikasi Gambar tangan menyerupai Batu, Gunting, Kertas menggunakan Flask dan Model Machine Learning.

# Pendahuluan
Proyek ini bertujuan untuk membangun aplikasi web sederhana menggunakan Flask yang dapat melakukan klasifikasi gambar untuk mengidentifikasi apakah gambar tersebut menunjukkan tangan membentuk batu, gunting, atau kertas. Model machine learning telah dilatih sebelumnya menggunakan dataset gambar tangan yang mencakup ketiga kelas tersebut.

# Fitur Utama
Upload Gambar: Pengguna dapat mengunggah gambar tangan ke aplikasi untuk diprediksi oleh model.
Pilih Gambar: Terdapat 25 gambar acak yang dapat dipilih oleh pengguna untuk melihat hasil prediksi.
Hasil Prediksi: Aplikasi menampilkan hasil prediksi, akurasi, lama waktu prediksi, input gambar yang diprediksi, dan label gambar yang diprediksi.
Struktur Direktori yang Jelas: Proyek memiliki struktur direktori yang terorganisir dengan baik untuk memudahkan pengembangan dan pemeliharaan.

# Instalasi
Pastikan Anda memiliki Python terinstal di sistem Anda.

Buat dan aktifkan lingkungan virtual:

# bash
.\env\Scripts\activate  # Untuk Windows
Instal paket-paket yang diperlukan:

# bash
Copy code
pip install -r requirements.txt
Penggunaan
Jalankan aplikasi Flask:

#bash
Copy code
python app.py
Buka browser dan akses http://localhost:5000.

Unggah gambar atau pilih gambar dari daftar yang disediakan.

Lihat hasil prediksi yang mencakup label klasifikasi, akurasi, dan waktu prediksi.

# Struktur Direktori
bash
Copy code
/your_project
   /env
   /static
       /images
   /templates
       index.html
       result.html
   /models
       model.h5
       model.json
       model.tflite
   app.py
   requirements.txt
   README.md

Lisensi
Proyek ini dilisensikan di bawah [nama lisensi]. Lihat berkas LICENSE untuk informasi lebih lanjut.

Kontak
Jika Anda memiliki pertanyaan atau umpan balik, jangan ragu untuk menghubungi [nama Anda] di [email Anda] atau melalui akun media sosial Anda.
