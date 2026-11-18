print("===== WELCOME TO LAND OF DAWN =====")

total_belanja = 0

while True:
    nama_makanan = input("\nMasukkan nama makanan: ")
    harga = int(input("Masukkan harga makanan: Rp"))
    jumlah = int(input("Masukkan jumlah pembelian: "))

    subtotal = harga * jumlah
    total_belanja += subtotal

    print("Subtotal: Rp", subtotal)

    lanjut = input("Tambah makanan lagi? (y/n): ")

    if lanjut.lower() != "y":
        break

# Menghitung diskon
if total_belanja > 100000:
    diskon = total_belanja * 10 / 100
else:
    diskon = 0

total_bayar = total_belanja - diskon

# Menampilkan hasil
print("\n===== STRUK PEMBAYARAN =====")
print("Total Belanja : Rp", total_belanja)
print("Diskon 10%    : Rp", diskon)
print("Total Bayar   : Rp", total_bayar)
print("============================")
print("Terima kasih telah berbelanja!")