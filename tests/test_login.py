import pytest
import os
from playwright.sync_api import Page
from pages.login_page import LoginPage # Sesuaikan path impor
from dotenv import load_dotenv

# ----------------- LOADING ENVIRONMENT VARIABLES ------------------
load_dotenv()

# Data Kredensial from .env
VALID_USERNAME = os.getenv("SAUCEDEMO_USERNAME_VALID")
VALID_PASSWORD = os.getenv("SAUCEDEMO_PASSWORD_VALID")
INVALID_USERNAME = os.getenv("SAUCEDEMO_USERNAME_INVALID")
INVALID_PASSWORD = os.getenv("SAUCEDEMO_PASSWORD_INVALID")

# Pastikan data terambil (optional check)
if not VALID_USERNAME or not VALID_PASSWORD:
    raise ValueError("Pastikan SAUCEDEMO_USERNAME_VALID dan SAUCEDEMO_PASSWORD_VALID diatur di file .env")

def test_successful_login(page: Page):
    """
    Skenario Positif: Memastikan pengguna dapat login
    dengan kredensial yang valid.
    """
    # 1. Inisialisasi Page Object
    login_page = LoginPage(page)
    
    # 2. Navigasi ke halaman login
    login_page.goto()
    
    # 3. Lakukan login dengan kredensial yang valid
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    
    # 4. Verifikasi bahwa login berhasil dan masuk ke halaman inventory
    login_page.verify_login_success()

# ---------------------------------------------------------------------------------------

def test_login_with_wrong_password(page: Page):
    """
    Skenario A: Menguji login dengan Username Benar, Password SALAH.
    """
    # 1. Inisialisasi Page Object
    login_page = LoginPage(page)
    
    # 2. Navigasi ke halaman login
    login_page.goto()
    
    # 3. Lakukan login dengan Password SALAH
    login_page.login(VALID_USERNAME, INVALID_PASSWORD)
    
    # 4. Verifikasi bahwa login GAGAL dan pesan error muncul
    expected_error = "Epic sadface: Username and password do not match any user in this service"
    login_page.verify_login_failure(expected_error)

# ---------------------------------------------------------------------------------------

def test_login_with_wrong_username(page: Page):
    """
    Skenario B: Menguji login dengan Username SALAH, Password Benar.
    """
    # 1. Inisialisasi Page Object
    login_page = LoginPage(page)
    
    # 2. Navigasi ke halaman login
    login_page.goto()
    
    # 3. Lakukan login dengan Username SALAH
    login_page.login(INVALID_USERNAME, VALID_PASSWORD)
    
    # 4. Verifikasi bahwa login GAGAL dan pesan error muncul
    expected_error = "Epic sadface: Username and password do not match any user in this service"
    login_page.verify_login_failure(expected_error)