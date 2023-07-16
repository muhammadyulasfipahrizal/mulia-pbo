def total_bayar(harga_tiket, jumlah_tiket):
    return harga_tiket * jumlah_tiket

rute = {
    1: ("Balikpapan", "Jakarta", 800000),
    2: ("Balikpapan", "Surabaya", 600000)
}

print("Pilih rute:")
for key, value in rute.items():
    print("{} - {}: Rp. {}".format(key, value[1], value[2]))

pilihan = int(input("Masukkan pilihan: "))

if pilihan in rute:
    asal, tujuan, harga_tiket = rute[pilihan]
    jumlah_tiket = int(input("Masukkan jumlah tiket: "))
    print("Informasi Pembelian Tiket")
    print("=========================")
    print("Rute: {} -> {}".format(asal, tujuan))
    print("Harga: Rp. {}".format(harga_tiket))
    print("Jumlah Tiket: {}".format(jumlah_tiket))
    print("Total: Rp. {}".format(total_bayar(harga_tiket, jumlah_tiket)))
else:
    print("Pilihan tidak valid")