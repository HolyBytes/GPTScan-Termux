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

Happy scanning! 🔍✨
