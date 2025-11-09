# 🧪 Playwright Automation Project - Sauce Demo

Proyek ini berisi *suite* otomatisasi pengujian menggunakan **Playwright** dan **Pytest** dengan bahasa pemrograman Python untuk menguji fungsionalitas di aplikasi demo [Sauce Demo](https://www.saucedemo.com/).

---

## 🚀 1. Persiapan dan Instalasi

Ikuti langkah-langkah di bawah ini untuk menyiapkan lingkungan pengujian Anda.

### A. Prasyarat

Pastikan Anda telah menginstal:

1.  **Python** (Versi 3.8+)
2.  **pip** (Package installer for Python)

### B. Instalasi Dependensi

1.  **Buat Virtual Environment** (Sangat disarankan untuk mengisolasi dependensi):
    ```bash
    python -m venv venv
    ```

2.  **Aktifkan Virtual Environment**:
    * **macOS / Linux:**
        ```bash
        source venv/bin/activate
        ```
    * **Windows (Command Prompt):**
        ```bash
        venv\Scripts\activate
        ```

3.  **Instal Playwright dan Pytest Plugins**:
    ```bash
    pip install pytest pytest-playwright python-dotenv
    ```

4.  **Instal Browser Drivers Playwright**:
    Perintah ini akan mengunduh dan menginstal *browser driver* (Chromium, Firefox, WebKit) yang diperlukan.
    ```bash
    playwright install
    ```

---

## 🔒 2. Konfigurasi Kredensial (File `.env`)

Untuk menjaga keamanan, semua kredensial dan data sensitif disimpan dalam variabel lingkungan dan diakses melalui file **`.env`**. File ini **TIDAK** disertakan dalam Git *repository* (diabaikan oleh `.gitignore`).

### Langkah Setup Kredensial

1.  **Buat File `.env`**: Di *root* direktori proyek Anda, buat file baru bernama **`.env`** atau rename file **`.env-example`** menjadi **`.env`**.

2.  **Salin dan Isi Data**: Tambahkan variabel berikut ke dalam file `.env` yang baru Anda buat, ganti contoh nilai sesuai kebutuhan:

    ```env
    # .env
    
    # Kredensial Login
    SAUCEDEMO_USERNAME_VALID=example_username
    SAUCEDEMO_PASSWORD_VALID=example_password

    SAUCEDEMO_USERNAME_INVALID=example_username
    SAUCEDEMO_PASSWORD_INVALID=example_password

    # Data Checkout (Digunakan dalam skenario E2E)
    SAUCEDEMO_FIRST_NAME=example_first_name
    SAUCEDEMO_LAST_NAME=example_last_name
    SAUCEDEMO_POSTAL_CODE=example_postal_code
    ```

---

## 📂 3. Struktur Proyek

Proyek ini mengikuti pola **Page Object Model (POM)** untuk menjaga kode tetap rapi dan mudah dirawat.

---

## ▶️ 4. Cara Menjalankan Tes

Semua perintah dijalankan dari *root* direktori proyek Anda (`playwright-saucedemo/`).

### A. Mode Standar (Headless - Cepat)

Menjalankan semua tes tanpa tampilan *browser* (mode *headless*).

```bash
pytest
```

### B. Menggunakan Alias (Makefile - Disarankan)
Kami menyediakan Makefile untuk memudahkan menjalankan perintah yang lebih kompleks, seperti membuka browser atau debugging.

| Alias (make ...) | Perintah yang Dijalankan | Deskripsi |
|------------------|--------------------------|-----------|
| make test | pytest | Menjalankan semua tes secara headless. |
| make headed | pytest ... --headed | Menjalankan semua tes dengan browser terbuka. |
| make slowmo | pytest ... --headed --slowmo 1000 | Menjalankan tes dengan browser terbuka dan jeda 1s antar aksi (untuk visualisasi). |
| make inspector | PLAYWRIGHT_CLI_ARGS="--debug" pytest ... --headed | Mengaktifkan Playwright Inspector. Berguna untuk debugging interaksi UI, locator, dan alur tes. |
| make debug | pytest ... --debug | Menghasilkan log debugging internal Pytest. Berguna untuk mendiagnosis masalah pengumpulan tes atau plugin Pytest. |