from playwright.sync_api import Page, expect

class CheckoutPage:
    
    # Locators
    CHECKOUT_BUTTON = "#checkout"
    FIRST_NAME_INPUT = "#first-name"
    LAST_NAME_INPUT = "#last-name"
    POSTAL_CODE_INPUT = "#postal-code"
    CONTINUE_BUTTON = "#continue"
    FINISH_BUTTON = "#finish"
    
    # Konfirmasi
    COMPLETE_HEADER = ".complete-header"
    COMPLETE_TEXT = "Thank you for your order!"
    

    def __init__(self, page: Page):
        self.page = page

    # Fungsi untuk memulai proses checkout dari halaman keranjang
    def start_checkout(self):
        self.page.click(self.CHECKOUT_BUTTON)

    # Fungsi untuk mengisi informasi data diri
    def fill_user_info(self, first_name, last_name, postal_code):
        self.page.fill(self.FIRST_NAME_INPUT, first_name)
        self.page.fill(self.LAST_NAME_INPUT, last_name)
        self.page.fill(self.POSTAL_CODE_INPUT, postal_code)
        self.page.click(self.CONTINUE_BUTTON)

    # Fungsi untuk menyelesaikan pemesanan
    def finish_order(self):
        # Asumsi sudah di halaman "Checkout: Overview"
        self.page.click(self.FINISH_BUTTON)

    # Verifikasi pemesanan berhasil
    def verify_order_success(self):
        expect(self.page.locator(self.COMPLETE_HEADER)).to_have_text(self.COMPLETE_TEXT)