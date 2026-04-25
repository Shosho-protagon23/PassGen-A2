# Password Strength & Generator (v2)

> Aplikasi desktop GUI Python yang menggabungkan dua alat dalam satu jendela: **pengecek kekuatan password secara real-time** dan **generator password acak** — dengan tampilan dark mode bergaya terminal.

---

## Apa yang Baru di Versi Ini?

Versi ini adalah pengembangan signifikan dari [versi sebelumnya (genA1)](#perbandingan-dengan-versi-sebelumnya). Bukan sekadar generator, aplikasi ini kini juga dapat **menganalisis password yang sudah Anda miliki**.

### Fitur Baru

| Fitur Baru | Keterangan |
|------------|-----------|
| **Password Strength Checker** | Analisis kekuatan password secara real-time saat mengetik |
| **Sistem Penilaian Skor (0–6)** | Skor dihitung berdasarkan panjang dan kompleksitas karakter |
| **Indikator Warna** | Merah (Lemah), Oranye (Sedang), Hijau (Kuat) |
| **Deteksi via Regex** | Menggunakan Regular Expression untuk mendeteksi jenis karakter |
| **Slider Panjang Password** | Kontrol panjang pakai slider, bukan Spinbox |
| **Layout Dua Seksi** | UI dipisah menjadi dua panel: Cek Kekuatan & Generate |

---

## Perbandingan dengan Versi Sebelumnya

| Aspek | genA1 (v1) | genA2 (v2) |
|-------|-----------|-----------|
| Fungsi utama | Generator saja | Generator + Strength Checker |
| Kontrol panjang | Spinbox (6–32) | Slider / Scale (8–32) |
| Panjang default | 12 karakter | 16 karakter |
| Pilihan karakter | Checkbox (huruf besar, angka, simbol) | Selalu full charset — tidak bisa dikustomisasi |
| Analisis password | ✗ Tidak ada | ✅ Real-time saat mengetik |
| Sistem skor | ✗ Tidak ada | ✅ Skor 0–6 berbasis panjang + regex |
| Feedback visual | ✗ Tidak ada | ✅ Label warna dinamis |
| Deteksi karakter | ✗ Tidak ada | ✅ Regex (huruf kecil, besar, angka, simbol) |
| Jumlah panel UI | 1 panel | 2 panel (LabelFrame) |

---

## Fitur Lengkap

- **Strength Checker real-time** — password dianalisis setiap kali Anda mengetik (event `KeyRelease`)
- **Penilaian skor 0–6** berdasarkan:
  - Panjang ≥ 8 karakter (+1)
  - Panjang ≥ 12 karakter (bonus +1)
  - Mengandung huruf kecil (+1)
  - Mengandung huruf besar (+1)
  - Mengandung angka (+1)
  - Mengandung simbol (+1)
- **Generator password** acak dengan panjang 8–32 karakter menggunakan full charset
- **Salin ke clipboard** dengan satu klik

---

## Tabel Indikator Kekuatan

| Skor | Status | Warna |
|------|--------|-------|
| 0 – 2 | LEMAH (Weak) | 🔴 Merah |
| 3 – 4 | SEDANG (Medium) | 🟠 Oranye |
| 5 – 6 | KUAT (Strong) | 🟢 Hijau |

---

## Persyaratan

- Python 3.x
- `tkinter` (bawaan Python)
- `re` (bawaan Python)

Tidak ada dependensi eksternal.

---

## Cara Menjalankan

```bash
python pass_gen_genA2.py
```

---

## Cara Penggunaan

### Cek Kekuatan Password
1. Ketik password di kolom input pada **Seksi 1**
2. Indikator kekuatan akan otomatis muncul dan berubah warna saat Anda mengetik

### Generate Password Baru
1. Geser **slider** di **Seksi 2** untuk menentukan panjang (8–32 karakter)
2. Klik **GENERATE RANDOM**
3. Klik **Copy Result** untuk menyalin ke clipboard

---

## Struktur Kode

```
pass_gen_genA2.py
│
└── class SecurityTool
    ├── __init__()          # Inisialisasi UI dua panel
    ├── check_strength()    # Analisis kekuatan password via regex (real-time)
    ├── generate_password() # Generate password acak full charset
    └── copy_pass()         # Salin password ke clipboard
```

---

## Keterbatasan

- Charset generator selalu menggunakan kombinasi penuh (huruf + angka + simbol) — tidak bisa dikustomisasi seperti versi v1
- Password di Strength Checker ditampilkan tersembunyi (`show="*"`) namun tidak ada tombol show/hide
- Tidak ada integrasi langsung antara hasil generate dengan strength checker (dikomentari di kode)

---

*Built by Ech0_f0xtr0t · Shosho-protagon23*