from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import cv2
import numpy as np
import tensorflow as tf

app = FastAPI()

print("Sedang memuat model AI TensorFlow... Tunggu sebentar...")
model = tf.keras.models.load_model("model_game_ringan.keras")
CLASSES = ['happy', 'sad', 'angry', 'surprised'] 
print("✅ Model TensorFlow berhasil dimuat dengan sempurna!")

# Pakai DSHOW biar kamera langsung ngebut nyalanya
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

@app.get("/")
def home():
    return {"status": "Mesin AI Aktif!"}

# 1. Endpoint untuk Game Ren'Py (Hanya kembalikan teks JSON biar ringan)
@app.get("/tebak_wajah")
def tebak_wajah():
    ret, frame = cap.read()
    if not ret:
        return {"error": "Kamera mati!"}
    
    gambar_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    gambar_pas = cv2.resize(gambar_rgb, (224, 224))
    gambar_siap = np.expand_dims(gambar_pas, axis=0) 
    
    prediksi = model.predict(gambar_siap, verbose=0)
    index_pemenang = np.argmax(prediksi[0])
    
    return {
        "emosi": CLASSES[index_pemenang],
        "akurasi": round(float(prediksi[0][index_pemenang]) * 100, 2)
    }

# ==========================================================
# 2. FITUR BARU: CCTV LIVE FEED UNTUK DILIHAT DI BROWSER!
# ==========================================================
def putar_kamera():
    while True:
        success, frame = cap.read()
        if not success:
            break
        
        # Prediksi Emosi secara Real-Time
        gambar_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        gambar_pas = cv2.resize(gambar_rgb, (224, 224))
        gambar_siap = np.expand_dims(gambar_pas, axis=0) 
        
        prediksi = model.predict(gambar_siap, verbose=0)
        index_pemenang = np.argmax(prediksi[0])
        emosi = CLASSES[index_pemenang]
        akurasi = round(float(prediksi[0][index_pemenang]) * 100, 2)
        
        # Tulis teks hasil prediksi ke atas layar video
        teks = f"{emosi} ({akurasi}%)"
        # Warna teks Hijau terang, ketebalan 3
        cv2.putText(frame, teks, (30, 60), cv2.FONT_HERSHEY_DUPLEX, 1.5, (0, 255, 0), 3)
        
        # Bungkus gambarnya jadi format JPEG untuk dikirim ke Web
        ret, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()
        
        # Tembakkan frame-nya terus menerus tanpa henti
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.get("/live")
def live_feed():
    return StreamingResponse(putar_kamera(), media_type="multipart/x-mixed-replace; boundary=frame")