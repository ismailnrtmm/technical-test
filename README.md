Test Scenario: Perbedaan Harga

Description: Test Scenario ini memeriksa apakah harga pemesanan di database sesuai dengan harga sesuai jadwal untuk tanggal dan waktu mulai yang sama..
Preconditions: Database berisi data pemesanan dan jadwal seperti yang disebutkan.
Steps:
Mengambil data pemesanan dari database.
Mengambil data jadwal dari database.
Untuk setiap pemesanan, bandingkan tanggal dan waktu mulai dengan data jadwal.
Jika ditemukan kecocokan, verifikasi bahwa harga pemesanan cocok dengan harga yang dijadwalkan.
Expected Result: Setiap perbedaan harga antara pemesanan dan jadwal terdeteksi dan dilaporkan.

Test Scenario: Double Booking 

Description: Test scenario ini memeriksa apakah terdapat pemesanan ganda (beberapa pemesanan untuk tempat, tanggal, dan waktu yang sama) dalam database.
Preconditions: Database berisi data pemesanan seperti yang disebutkan dalam pernyataan masalah.
Steps:
Mengambil data pemesanan dari database.
Buat kamus untuk melacak jumlah pemesanan untuk setiap kombinasi unik tempat, tanggal, waktu mulai, dan waktu selesai.
Untuk setiap pemesanan, tingkatkan jumlah yang sesuai di kamus.
Periksa apakah hitungan lebih besar dari 1, menunjukkan pemesanan ganda.
Expected Result: Setiap kejadian pemesanan ganda terdeteksi dan dilaporkan.
