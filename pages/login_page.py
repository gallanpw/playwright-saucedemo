from playwright.sync_api import Page, expect

class LoginPage:
    # URL
    URL = "https://www.saucedemo.com/"
    INVENTORY_URL = "https://www.saucedemo.com/inventory.html"

    # Locators
    USERNAME_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-button"
    PRODUCTS_TITLE = ".title" # Locator untuk judul halaman setelah login
    ERROR_MESSAGE = ".error-message-container.error"

    def __init__(self, page: Page):
        self.page = page

    # Fungsi untuk navigasi
    def goto(self):
        self.page.goto(self.URL)

    # Fungsi untuk melakukan proses login
    def login(self, username, password):
        self.page.fill(self.USERNAME_INPUT, username)
        self.page.fill(self.PASSWORD_INPUT, password)
        self.page.click(self.LOGIN_BUTTON)

    # Verifikasi keberhasilan login
    def verify_login_success(self):
        # 1. Pastikan URL telah berubah ke halaman inventory
        expect(self.page).to_have_url(self.INVENTORY_URL)
        # 2. Pastikan elemen khas (judul 'Products') ada
        expect(self.page.locator(self.PRODUCTS_TITLE)).to_have_text("Products")

    # Verifikasi kegagalan login
    def verify_login_failure(self, expected_message):
        """Memastikan pesan error yang tepat muncul di halaman."""
        # 1. Pastikan URL TIDAK berubah (tetap di halaman login)
        expect(self.page).to_have_url(self.URL)
        # 2. Pastikan elemen pesan error muncul dan berisi teks yang sesuai
        expect(self.page.locator(self.ERROR_MESSAGE)).to_have_text(expected_message)