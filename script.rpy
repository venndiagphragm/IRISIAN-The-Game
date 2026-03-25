# Ini adalah file script utama untuk Game Ren'Py "Dunia IRISIAN"
# Versi 2.0: FULL CAMERA CONTROL
# Pemain memutuskan pilihan bukan dari klik menu, tapi dari ekspresi wajah!

init python:
    import urllib.request
    import json

    def get_emotion():
        """
        Fungsi ini dipanggil untuk menembak API FastAPI otak_ai.py
        menggunakan modul bawaan Python (urllib & json)
        """
        try:
            req = urllib.request.Request("http://localhost:8000/tebak_wajah")
            with urllib.request.urlopen(req, timeout=5) as response:
                if response.status == 200:
                    data = json.loads(response.read().decode('utf-8'))
                    if "emosi" in data:
                        return data["emosi"]
        except Exception as e:
            pass
        return "neutral"

# Deklarasi karakter
define p = Character("Pemain", color="#c8ffc8")
define npc = Character("???", color="#ffc8c8")
define sys = Character("Sistem Kamera", color="#ffffc8")

# Mulai ceritanya dari sini
label start:
    
    # Variabel pelacak poin emosi
    $ poin_happy = 0
    $ poin_sad = 0
    $ poin_angry = 0
    $ poin_surprised = 0
    
    # =========================================================
    # 1. OPENING (Babak Pengenalan)
    # =========================================================
    scene black with fade
    "Selamat Datang di Dunia IRISIAN"
    "Suara yang kuingat dari masa lalu... memanggilku"
    "Kesadaran memudar... Apa yang kamu rasakan?"

    sys "📸 Memindai emosi dari wajahmu..."
    "{i}(Tatap ke arah kamera, siapkan ekspresimu, lalu KLIK/ENTER untuk memotret!){/i}"
    
    # Trigger API
    $ current_emotion = get_emotion()

    if current_emotion == "happy":
        $ poin_happy += 2
        p "Terdereksi: 😊 (Happy)"
    elif current_emotion == "sad":
        $ poin_sad += 2
        p "Terdeteksi: 😢 (Sad)"
    elif current_emotion == "angry":
        $ poin_angry += 2
        p "Terdeteksi: 😡 (Angry)"
    elif current_emotion == "surprised":
        $ poin_surprised += 2
        p "Terdeteksi: 😲 (Surprised)"
    else:
        sys "Gagal membaca emosi. Memasuki rute netral/sad secara default..."
        $ current_emotion = "sad"

    # =========================================================
    # 2. PERCABANGAN PERTAMA
    # =========================================================
    if current_emotion == "happy":
        jump branch1_happy
    elif current_emotion == "sad":
        jump branch1_sad
    elif current_emotion == "angry":
        jump branch1_angry
    elif current_emotion == "surprised":
        jump branch1_surprised

# --- SKENARIO JIKA AWALNYA HAPPY ---
label branch1_happy:
    # scene langit_cerah with dissolve
    "Seseorang yang tampak kebingungan mencari barang tiba-tiba menghampiriku."
    npc "Sudah kucari kemana-mana tapi belum ketemu! Apakah kamu yang membawa perabotan ini?"
    
    sys "Pilihan Aksi (Pilih dengan Wajahmu!): \n😊 (Happy) -> Membantunya \n😢 (Sad) -> Menjauhinya \n😡 (Angry) -> Kesal dituduh \n😲 (Surprised) -> Kaget dan bingung"
    "{i}(Tunjukkan ekspresimu ke kamera dan KLIK untuk mengonfirmasi pilihan!){/i}"
    
    $ action_emotion = get_emotion()
    
    if action_emotion == "happy":
        $ poin_happy += 1
        "➡️ Kamu tersenyum (Happy) dan mencoba membantunya mencari barang tersebut."
    elif action_emotion == "sad":
        $ poin_sad += 1
        "➡️ Kamu cemberut (Sad), memilih mundur karena tak tahu cara membantu."
    elif action_emotion == "angry":
        $ poin_angry += 1
        "➡️ Kamu mengerutkan dahi (Angry), merasa kesal dituduh membawa barangnya."
    elif action_emotion == "surprised":
        $ poin_surprised += 1
        "➡️ Kamu terkejut (Surprised) sambil melihat sekeliling, bingung dengan situasi aneh ini."
    
    jump narrative_transition

# --- SKENARIO JIKA AWALNYA SAD ---
label branch1_sad:
    # scene mendung with dissolve
    "Aku melihat seseorang tersungkur sambil menangis murung di sudut jalan."
    npc "Tempat ini terlalu sepi... kamu siapa? Tolong beritahu aku jalan keluar dari labirin ini..."
    
    sys "Pilihan Aksi (Pilih dengan Wajahmu!): \n😊 (Happy) -> Menghiburnya \n😢 (Sad) -> Turut bersedih \n😡 (Angry) -> Menyuruhnya bangkit \n😲 (Surprised) -> Terkejut menanyakan jalan keluar"
    "{i}(Tunjukkan ekspresimu ke kamera dan KLIK untuk mengonfirmasi pilihan!){/i}"
    
    $ action_emotion = get_emotion()
    
    if action_emotion == "happy":
        $ poin_happy += 1
        "➡️ Kamu tersenyum hangat (Happy) dan mencoba menenangkannya agar tidak menangis."
    elif action_emotion == "sad":
        $ poin_sad += 1
        "➡️ Kamu menatap iba (Sad), ikut duduk di sampingnya merasakan kepedihannya."
    elif action_emotion == "angry":
        $ poin_angry += 1
        "➡️ Kamu merasa geram (Angry), memaksanya untuk berdiri dan menghadapi kenyataan."
    elif action_emotion == "surprised":
        $ poin_surprised += 1
        "➡️ Kamu terbelalak (Surprised), baru sadar bahwa tempat ini dipercaya sebagai labirin."
        
    jump narrative_transition

# --- SKENARIO JIKA AWALNYA ANGRY ---
label branch1_angry:
    # scene langit_merah with dissolve
    "Sesosok bayangan tiba-tiba muncul di hadapanmu dengan sikap yang sangat waspada!"
    npc "Siapa di sana?! Jangan mendekat! Siapa yang mengirimmu ke sini, hah?!"
    
    sys "Pilihan Aksi (Pilih dengan Wajahmu!): \n😊 (Happy) -> Mengangkat tangan tanda damai \n😢 (Sad) -> Takut dan diam \n😡 (Angry) -> Balas membentak \n😲 (Surprised) -> Kaget dan tidak merespon"
    "{i}(Tunjukkan ekspresimu ke kamera dan KLIK untuk mengonfirmasi pilihan!){/i}"
    
    $ action_emotion = get_emotion()
    
    if action_emotion == "happy":
        $ poin_happy += 1
        "➡️ Kamu mencoba tersenyum (Happy), menunjukkan bahwa dirimu bukanlah ancaman baginya."
    elif action_emotion == "sad":
        $ poin_sad += 1
        "➡️ Wajahmu memelas (Sad), kakimu gemetar melihat ketegangan ini."
    elif action_emotion == "angry":
        $ poin_angry += 1
        "➡️ Emosimu ikut naik (Angry). Kamu bersiap di posisi bertarung, tak mau kalah gertakan!"
    elif action_emotion == "surprised":
        $ poin_surprised += 1
        "➡️ Tanganmu terangkat refleks ke atas (Surprised), terlalu kaget untuk berkata-kata."
        
    jump narrative_transition

# --- SKENARIO JIKA AWALNYA SURPRISED ---
label branch1_surprised:
    # scene langit_biru with dissolve
    "Tiba-tiba, dari balik kabut terang bercahaya, muncul seseorang tanpa peringatan."
    npc "Akhirnya kau datang juga di tempat ini! Kau pasti terkejut kan? Banyak yang belum kau ketahui..."
    
    sys "Pilihan Aksi (Pilih dengan Wajahmu!): \n😊 (Happy) -> Mengikuti dengan senang hati \n😢 (Sad) -> Ragu dan menjaga jarak \n😡 (Angry) -> Curiga akan dijebak \n😲 (Surprised) -> Ingin tahu rahasia tempat ini"
    "{i}(Tunjukkan ekspresimu ke kamera dan KLIK untuk mengonfirmasi pilihan!){/i}"
    
    $ action_emotion = get_emotion()
    
    if action_emotion == "happy":
        $ poin_happy += 1
        "➡️ Dengan wajah berseri (Happy), rasa penasaranku mengalahkan rasa ragu, aku berjalan mengikutinya."
    elif action_emotion == "sad":
        $ poin_sad += 1
        "➡️ Kamu menarik nafas panjang (Sad) dan mundur perlahan, enggan bersentuhan dengan hal tak kasat mata."
    elif action_emotion == "angry":
        $ poin_angry += 1
        "➡️ Tumbuh rasa tidak suka di dadamu (Angry). Kamu melontarkan kalimat tajam penuh curiga."
    elif action_emotion == "surprised":
        $ poin_surprised += 1
        "➡️ Matamu kembali terbuka lebar (Surprised), segera mencecarnya dengan ribuan pertanyaan tentang rahasia tempat ini."
        
    jump narrative_transition

# =========================================================
# 3. NARRATIVE TRANSITION (Jeda Antar Babak)
# =========================================================
label narrative_transition:
    "Meskipun begitu... perjalanan tetaplah berlanjut."
    "Tiba-tiba, terdengar suara gemuruh ledakan aneh dari kejauhan yang mengguncang tanah!"
    
    sys "📸 Merekam reaksi spontanmu terhadap kejadian baru... \n{i}(Seperti biasa, siapkan wajah lalu KLIK layar!){/i}"
    $ current_emotion = get_emotion()

    # Tambah poin emosi berdasarkan hasil kedua
    if current_emotion == "happy":
        $ poin_happy += 2
        "Melihat reruntuhan itu, rasa antusias barumu lahir (Happy). Kamu melihatnya sebagai petualangan menarik."
    elif current_emotion == "sad":
        $ poin_sad += 2
        "Rintik hujan tiba-tiba turun (Sad). Hati menjadi sendu seiring kerusakan yang kau tatap lurus."
    elif current_emotion == "angry":
        $ poin_angry += 2
        "Udara memanas (Angry). Rasa jengkel membakar saat mencium aroma gosong dari puing."
    elif current_emotion == "surprised":
        $ poin_surprised += 2
        "Dunia berputar seketika (Surprised). Ada sesuatu ajaib terangkat dari bekas ledakan barusan!"
    else:
        "Suasana terasa sunyi dan dingin."
        
    "Kamu terus berjalan menembus halang rintang di sekitarmu, menyusuri batas dimensi Dunia IRISIAN..."

# =========================================================
# 5. THE JUDGMENT (Fase Penghitungan Akhir)
# =========================================================
label judgment:
    scene black with fade
    "Cahaya menyelubungimu perlahan. Fase evaluasi dimulai."
    sys "Mari kita lihat cerminan terdalam dari hatimu melalui ekspresi-ekspresimu..."
    
    # Kalkulasi Emosi Dominan via Python
    python:
        emotions_dict = {
            "happy": poin_happy,
            "sad": poin_sad,
            "angry": poin_angry,
            "surprised": poin_surprised
        }
        max_score = max(emotions_dict.values())
        
        # Mengecek apakah ada nilai maksimum yang sama (Tie)
        max_emotions = [k for k, v in emotions_dict.items() if v == max_score]
        
        if len(max_emotions) > 1:
            dominant_emotion = "tie"
        else:
            dominant_emotion = max_emotions[0]

# =========================================================
# 6. RESOLUSI & MULTIPLE ENDINGS
# =========================================================
    if dominant_emotion == "happy":
        jump ending_optimist
    elif dominant_emotion == "sad":
        jump ending_reflector
    elif dominant_emotion == "angry":
        jump ending_resolute
    elif dominant_emotion == "surprised":
        jump ending_explorer
    else:
        jump ending_balanced

label ending_optimist:
    "🏆 GELAR: \n☀️ THE OPTIMIST"
    "Dilihat dari bagaimana Anda menyelesaikan konflik dengan wajah gembira, Anda adalah The Optimist."
    "Anda memandang dunia dengan penuh senyuman dan selalu ada ruang untuk sisi positif dalam kegelapan."
    jump game_over

label ending_reflector:
    "🏆 GELAR: \n🌧️ THE REFLECTOR"
    "Dilihat dari empati dan kesedihan yang Anda rasakan selama cerita, Anda adalah The Reflector."
    "Anda mampu memahami derita yang tidak terucap melalui mata yang berair. Empati luar biasa."
    jump game_over

label ending_resolute:
    "🏆 GELAR: \n🔥 THE RESOLUTE / THE CHALLENGER"
    "Kecepatan Anda merespon konflik dengan amarah memperlihatkan jiwa The Resolute."
    "Dinding tebal atau tantangan besar pun bersedia Anda pukul sampai hancur. Kegigihan yang menyala!"
    jump game_over

label ending_explorer:
    "🏆 GELAR: \n✨ THE EXPLORER"
    "Sepanjang cerita berlalu, keterkejutan selalu hadir di wajah Anda mengartikan rasa antusias yang tiada habisnya, Anda The Explorer."
    "Selalu awas karena Anda menginginkan eksplorasi tanpa batas."
    jump game_over

label ending_balanced:
    "🏆 GELAR: \n⚖️ THE BALANCED SOUL"
    "Rupanya skor Anda imbang di beberapa aspek. Anda adalah The Balanced Soul."
    "Mengatur ekspresi pada porsinya masing-masing menandakan kecerdasan emosional yang tinggi."
    jump game_over

label game_over:
    "Terima kasih telah bermain di Dunia IRISIAN versi Kontrol Kamera Emosional!"
    return
