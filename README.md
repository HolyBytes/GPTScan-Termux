# 🛠️ GPTScan Termux Edition - Panduan Lengkap

## 🚀 Apa Sih GPTScan Itu?

**GPTScan Termux Edition** adalah tool multi-fungsi yang bikin hidup kamu di Termux jadi lebih mudah! Tool ini nggak cuma buat satu keperluan doang, tapi bisa buat:

* 🔍 **Scan Keamanan** - Cek IP sama URL biar tau aman atau nggak
* ☀️ **Cek Cuaca** - Tau cuaca real-time tanpa buka browser
* 🤖 **Chat AI** - Ngobrol sama GPT-3.5 Turbo buat bantuin tugas
* 📊 **Monitor Sistem** - Liat spesifikasi HP/komputer kamu

**Dibuat sama**: Ade Pratama (HolyBytes) 💝

## ✨ Fitur-Fitur Keren

### 🕵️ **Shodan Scanner**
Mau tau info lengkap tentang suatu IP? Tinggal masukin aja, langsung dapet:
* Lokasi geografis
* Port yang terbuka
* Provider internet (ISP)
* Device apa yang kepasang

*Contoh: Scan server kantor buat mastiin keamanannya*

### 🦠 **VirusTotal Scanner**
Curiga sama file atau link tertentu? Scan dulu sebelum dibuka:
* Cek URL mencurigakan
* Verifikasi file hash (MD5/SHA256)
* Tau langsung ada malware atau nggak

*Contoh: Cek link download yang dikirim temen*

### 🌤️ **OpenWeather Checker**
Pengen tau cuaca sekarang atau besok? Gampang banget:
* Cuaca real-time
* Suhu, kelembaban, tekanan udara
* Masukkan nama kota aja

*Contoh: Cek cuaca sebelum jalan-jalan*

### 💬 **GPT-3.5 Turbo Chat**
Butuh bantuan AI? Langsung chat aja:
* Tanya soal coding
* Minta translate dokumen
* Brainstorming ide kreatif

*Contoh: "Buatin script Python buat backup file"*

### 📱 **System Info**
Pengen tau spesifikasi device kamu? Satu klik kelar:
* RAM dan penggunaan memori
* Info CPU dan OS
* Storage yang tersisa

## 👍 Yang Bikin Tool Ini Keren

### 🎨 **Tampilan Ciamik**
* Warna-warni di terminal (nggak boring!)
* ASCII Art yang eye-catching
* Info ditampilkan rapi dalam box

### 🔧 **Serba Bisa**
* 4 fungsi berbeda dalam 1 tool
* Nggak perlu install app terpisah-pisah

### 📱 **Support Multi Platform**
* Jalan mulus di Termux Android
* Bisa juga di Linux/Windows

### 🆓 **Open Source**
* Gratis selamanya
* Bisa dimodif sesuai kebutuhan

## 😅 Kekurangannya Apa?

### 🔑 **Butuh API Key**
* Beberapa fitur perlu API key gratis/berbayar
* Tapi tenang, banyak yang gratis kok!

### ⚠️ **Error Handling Masih Sederhana**
* Kadang pesan error kurang jelas
* *Tapi udah diupdate terus kok!*

### 📦 **Fitur Masih Terbatas**
* VirusTotal belum bisa upload file langsung
* Scan masih jalan satu-satu (belum multithreading)

## 🔥 Yang Lagi Dikembangkan

### 🆕 **Fitur Baru**
* Enkripsi/dekripsi file
* Network scanner (ping, traceroute)
* Upload file langsung ke VirusTotal

### 🛠️ **Perbaikan**
* Error handling yang lebih baik
* Logging buat debug
* Performa yang lebih cepat

### 🎨 **UI/UX**
* Mode interaktif tanpa menu angka
* Grafik simple buat monitoring sistem

## 🎬 Tampilan Awal & Akhir

**Waktu Mulai**:
* Logo ASCII yang keren
* Info versi terbaru
* Spesifikasi sistem kamu langsung keliatan

**Waktu Keluar**:
* Pesan goodbye yang friendly
* Copyright info
* Ctrl+C juga ditangani dengan baik

## 🎯 Cocok Buat Siapa?

✅ **Kamu yang suka ngutak-ngatik Termux**
✅ **Developer yang butuh akses cepat ke API**
✅ **Pemula yang belajar Python**
✅ **Siapa aja yang pengen tool serba guna**

## ⚖️ Penting! Pakainya Secara Legal Ya

Tool ini **100% gratis**, tapi:
* Beberapa API punya limit harian
* Selalu pakai buat hal yang legal dan etis
* Jangan disalahgunakan ya!

## 🤝 Mau Kontribusi?

Punya ide buat fitur baru? Nemuin bug? Gas langsung ke GitHub HolyBytes!

**Pro tip**: Kalo ada yang bingung, jangan ragu tanya di Issues GitHub. Community-nya helpful banget!

---

# 📱 Panduan Install GPTScan di Termux & Terminal

Halo! Mau install GPTScan di Termux atau terminal lain? Tenang aja, ikuti guide ini step by step pasti bisa! 🚀

## 🎯 Yang Kamu Butuhkan

Sebelum mulai, pastikan kamu punya ini dulu ya:

1. **Python 3.x** (pakai yang terbaru aja biar lancar)
2. **Pip** (buat install package Python)
3. **Package Python** yang diperlukan:
   - `requests` - buat ngambil data dari internet
   - `psutil` - buat info sistem
   - `colorama` - buat tampilan warna-warni

## 🔧 Langkah Instalasi

### Step 1: Cek Python & Pip

Pertama, pastikan dulu Python sama Pip udah terinstall:

```bash
python3 --version
pip3 --version
```

Kalau belum ada, install dulu:

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install python3 python3-pip
```

**CentOS/RHEL:**
```bash
sudo yum install python3 python3-pip
```

**Termux:**
```bash
pkg update
pkg install python
```

### Step 2: Install Package Python

Sekarang install package yang dibutuhkan:

```bash
pip3 install requests psutil colorama
```

### Step 3: Download GPTScan

Clone repo-nya:

```bash
git clone https://github.com/HolyBytes/GPTScan-Termux.git
cd GPTScan-Termux
```

### Step 4: Jalankan Script

Tinggal run aja:

```bash
python3 nama_script.py
```

## 🔥 Troubleshooting - Kalau Ada Error

### ❌ Error: "ModuleNotFoundError"

**Masalah**: Muncul error kayak gini:
```
ModuleNotFoundError: No module named 'requests'
```

**Solusi**: Install ulang package-nya:
```bash
pip3 install requests psutil colorama --upgrade
```

### ❌ Error API Key Gak Valid

**Masalah**: API Shodan, VirusTotal, dll error terus

**Solusi**: 
- Ganti API key di bagian `API_KEYS` dengan key yang bener
- Dapetin API key baru di:
  - [Shodan](https://account.shodan.io/)
  - [VirusTotal](https://www.virustotal.com/gui/join-us)
  - [OpenWeather](https://openweathermap.org/api)
  - [OpenRouter](https://openrouter.ai/keys)

### ❌ Error Platform Gak Support

**Masalah**: Script cuma jalan di Termux/Linux tapi kamu pakai Windows

**Solusi**: Edit bagian yang spesifik platform. Contoh:
- `os.system('clear')` → `os.system('cls')` untuk Windows

### ❌ Error Koneksi Internet

**Masalah**: Timeout atau gagal konek ke API

**Solusi**: 
- Cek koneksi internet kamu
- Kalau pakai proxy, tambahin ini di script:

```python
proxies = {
    'http': 'http://proxy-ip:port',
    'https': 'http://proxy-ip:port'
}
response = requests.get(url, proxies=proxies)
```

### ❌ Error Permission

**Masalah**: Gak bisa akses resource sistem

**Solusi**: 
- Jangan pakai `sudo` kecuali emang perlu
- Di GitHub Codespaces, pastikan environment punya permission yang cukup

## 💡 Tips Buat GitHub Codespaces

1. Setelah buka repo di Codespaces, jalanin di terminal:
   ```bash
   pip install -r requirements.txt
   ```
2. Kalau gak ada file requirements.txt, install manual kayak di atas
3. Codespaces udah sedia Python & pip by default, jadi gampang!

## 📝 File requirements.txt (Opsional)

Kamu bisa bikin file `requirements.txt` isinya:

```
requests>=2.25.1
psutil>=5.8.0
colorama>=0.4.4
```

Terus install dengan:

```bash
pip3 install -r requirements.txt
```

## 🎉 Kesimpulan

Udah deh! Kalau ikutin guide ini, pasti GPTScan bakal jalan smooth di Termux atau terminal kamu. Kalau masih ada masalah, coba cek lagi step by step-nya ya!

*Happy Scanning! 🔍✨*
