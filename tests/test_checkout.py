import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage

# Data Kredensial Positif
VALID_USERNAME = "standard_user"
VALID_PASSWORD = "secret_sauce"

# Data Checkout
FIRST_NAME = "Tester"
LAST_NAME = "Automation"
POSTAL_CODE = "12345"

def test_successful_checkout_e2e(page: Page):
    """
    Skenario E2E: Login, tambah item, dan selesaikan checkout dengan sukses.
    """
    # 1. Inisialisasi Page Objects
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    checkout_page = CheckoutPage(page)
    
    # A. LOGIN
    login_page.goto()
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    login_page.verify_login_success() # Pastikan masuk ke halaman produk
    
    # B. TAMBAH ITEM KE KERANJANG
    inventory_page.add_item_to_cart()
    inventory_page.goto_cart()
    
    # C. CHECKOUT: ISI DATA DIRI
    checkout_page.start_checkout()
    checkout_page.fill_user_info(FIRST_NAME, LAST_NAME, POSTAL_CODE)
    
    # D. CHECKOUT: FINISH
    checkout_page.finish_order()
    
    # E. VERIFIKASI KEBERHASILAN
    checkout_page.verify_order_success()