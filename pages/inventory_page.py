from playwright.sync_api import Page, expect

class InventoryPage:
    
    # Locators
    PRODUCTS_TITLE = ".title"
    ADD_TO_CART_BUTTON = "#add-to-cart-sauce-labs-backpack" # Kita pakai 1 item spesifik
    SHOPPING_CART_LINK = ".shopping_cart_link"

    def __init__(self, page: Page):
        self.page = page

    # Fungsi untuk memverifikasi berada di halaman produk
    def verify_on_inventory_page(self):
        expect(self.page.locator(self.PRODUCTS_TITLE)).to_have_text("Products")

    # Fungsi untuk menambahkan item
    def add_item_to_cart(self):
        self.page.click(self.ADD_TO_CART_BUTTON)

    # Fungsi untuk navigasi ke keranjang
    def goto_cart(self):
        self.page.click(self.SHOPPING_CART_LINK)