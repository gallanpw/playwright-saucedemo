# Makefile
.PHONY: headed slowmo inspector debug test

# Alias sederhana untuk menjalankan tes login dengan browser terbuka (headed)
headed:
	pytest tests/test_login.py --headed
	pytest tests/test_checkout.py --headed

# Alias yang Anda inginkan: headed dan slowmo
slowmo:
	pytest tests/test_login.py --headed --slowmo 1000
	pytest tests/test_checkout.py --headed --slowmo 1000

# Penting: Pastikan ada spasi setelah "=" jika Anda menggunakan shell tertentu.
inspector:
	PLAYWRIGHT_CLI_ARGS="--debug" pytest tests/test_login.py --headed --slowmo 1000
	PLAYWRIGHT_CLI_ARGS="--debug" pytest tests/test_checkout.py --headed --slowmo 1000

# Alias yang Anda inginkan: debug
debug:
	pytest tests/test_login.py --debug
	pytest tests/test_checkout.py --debug

# Alias standar untuk menjalankan semua tes secara headless
test:
	pytest