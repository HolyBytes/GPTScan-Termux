# 🛠️ GPTScan Termux Edition - Panduan Lengkap

## 🚀 Apa itu GPTScan?

**GPTScan Termux Edition** adalah tool multi-fungsi untuk Termux yang menggabungkan beberapa fungsi penting dalam satu aplikasi:

### ✨ Fitur Utama
- 🔍 **Shodan Scanner** - Scan IP untuk info keamanan, lokasi, port terbuka
- 🦠 **VirusTotal Scanner** - Cek URL/file hash untuk deteksi malware
- ☀️ **Weather Checker** - Informasi cuaca real-time berdasarkan kota
- 🤖 **GPT-3.5 Turbo Chat** - Assistant AI untuk berbagai keperluan
- 📊 **System Monitor** - Monitoring RAM, CPU, storage device

**Dibuat oleh**: Ade Pratama (HolyBytes)

## 📦 Instalasi

### 1. Persiapan Sistem
```bash
# Termux
pkg update && pkg install python git

# Ubuntu/Debian
sudo apt update && sudo apt install python3 python3-pip git

# CentOS/RHEL
sudo yum install python3 python3-pip git
```

### 2. Install Dependencies
```bash
pip3 install requests psutil colorama
```

### 3. Download & Jalankan
```bash
git clone https://github.com/HolyBytes/GPTScan-Termux.git
cd GPTScan-Termux
python3 gptscan.py
```

## 🔧 Setup API Keys

Untuk menggunakan semua fitur, kamu perlu API key gratis dari:

- **Shodan**: [account.shodan.io](https://account.shodan.io/)
- **VirusTotal**: [virustotal.com/gui/join-us](https://www.virustotal.com/gui/join-us)
- **OpenWeather**: [openweathermap.org/api](https://openweathermap.org/api)
- **OpenRouter**: [openrouter.ai/keys](https://openrouter.ai/keys)

Masukkan API key di bagian `API_KEYS` dalam script.

## 🎯 Keunggulan

### 👍 Pros
- **4-in-1 Tool** - Multiple functions dalam satu aplikasi
- **Gratis & Open Source** - Tanpa biaya tersembunyi
- **Tampilan Colorful** - Interface terminal yang menarik
- **Cross Platform** - Support Termux, Linux, Windows

### 👎 Cons
- **Membutuhkan API Key** - Beberapa fitur perlu registrasi
- **Processing Sequential** - Belum support multithreading
- **Error Handling Sederhana** - Pesan error masih basic

## 🔥 Roadmap Pengembangan

**Fitur Mendatang:**
- File encryption/decryption
- Network scanner (ping, traceroute)
- Direct file upload ke VirusTotal
- Interactive mode tanpa menu angka
- System monitoring dengan grafik

## 🛠️ Troubleshooting

### Error Module Not Found
```bash
pip3 install requests psutil colorama --upgrade
```

### API Key Invalid
- Verifikasi API key di website masing-masing
- Pastikan key belum expired
- Cek limit harian API

### Permission Error
- Jangan gunakan `sudo` kecuali diperlukan
- Untuk Windows: ganti `os.system('clear')` dengan `os.system('cls')`

### Connection Timeout
- Periksa koneksi internet
- Untuk proxy, tambahkan konfigurasi proxy di requests

## 📋 Requirements.txt
```
requests>=2.25.1
psutil>=5.8.0
colorama>=0.4.4
```

Install dengan: `pip3 install -r requirements.txt`

## 💡 Tips Penggunaan

1. **GitHub Codespaces**: Environment sudah include Python & pip
2. **Termux**: Gunakan `pkg` untuk install package sistem
3. **Keamanan**: Selalu gunakan tool untuk tujuan legal dan etis
4. **Performance**: API memiliki rate limit, gunakan secukupnya

## 🎭 Target User

✅ Enthusiast Termux  
✅ Developer yang butuh quick access ke multiple API  
✅ Pemula yang belajar Python networking  
✅ Security researcher (ethical use)  

## 🤝 Kontribusi

Punya ide fitur baru atau menemukan bug? Kontribusi di:
- GitHub: HolyBytes/GPTScan-Termux
- Buat issue atau pull request
- Community helpful untuk beginners

---

*Happy Scanning! 🔍✨*

**Legal Notice**: Tool ini 100% gratis. Gunakan secara legal dan etis. Beberapa API memiliki limit penggunaan harian.
