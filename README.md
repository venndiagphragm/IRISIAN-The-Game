# 👁️ Resonance of the IRISIANS: AI-Powered Visual Novel

**Resonance of the IRISIANS** adalah sebuah game Visual Novel interaktif eksperimental di mana **ekspresi wajah pemain di dunia nyata** secara langsung memengaruhi alur cerita di dalam game. 

Alih-alih hanya memilih opsi melalui klik *mouse*, game ini menggunakan kamera laptop (Webcam) dan model *Machine Learning* (Computer Vision) untuk membaca emosi pemain secara *real-time* (Bahagia, Sedih, Marah, Terkejut) dan membawa mereka ke percabangan cerita serta *ending* yang berbeda.

---

## ✨ Fitur Utama
- **Real-Time Emotion Recognition:** Mendeteksi 4 jenis emosi dasar (`happy`, `sad`, `angry`, `surprised`) menggunakan model TensorFlow/Keras yang ringan.
- **Zero-Lag Architecture:** Menggunakan sistem *Multi-threading* antara antarmuka kamera (OpenCV) dan pemrosesan AI, sehingga video berjalan mulus di 30 FPS.
- **Client-Server Integration:** AI berjalan sebagai *Local API Server* independen yang berkomunikasi secara instan dengan *engine* Ren'Py.
- **Dynamic Storytelling:** 4 Rute cerita unik dan 5 *Multiple Endings* yang ditentukan oleh kalkulasi emosi dominan pemain selama permainan.

---

## 🛠️ Arsitektur Sistem (The Engine)
Proyek ini mengusung arsitektur **"Dua Kamar"** untuk mencegah *bottleneck* performa. Ren'Py fokus merender grafis, sementara Python menangani beban berat AI di latar belakang.

```text
       [ WAJAH PEMAIN ]
              │
              ▼
         [ WEBCAM ] 
              │ (Video 30 FPS)
              ▼
=========================================================
 🧠 KAMAR 1: MESIN AI (otak_ai.py)
=========================================================
 1. JALUR MATA     : OpenCV menangkap gambar & 
                     memunculkan Jendela Pop-up CCTV.
              │
              ▼
 2. JALUR OTAK     : TensorFlow memproses gambar 
                     (tiap 0.1 detik) -> Ekstraksi Emosi.
              │
              ▼
 3. JALUR API      : Server Python berjaga di Port 8000
                     membawa hasil tebakan terakhir.
=========================================================
              ▲
              │ (GET Request: "Beri aku emosinya!")
              │ (Response JSON: {"emosi": "happy", "akurasi": 98.5})
              ▼
=========================================================
 🎮 KAMAR 2: GAME ENGINE (Ren'Py)
=========================================================
 - Mengeksekusi script.rpy
 - Menampilkan Visual Novel
 - Mengubah rute cerita berdasarkan respons API
=========================================================
