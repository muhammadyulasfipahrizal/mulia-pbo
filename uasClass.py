class TiketPesawat:
    def __init__(self, asal, tujuan, harga):
        self.asal = asal
        self.tujuan = tujuan
        self.harga = harga

    def hitung_total_bayar(self, jumlah):
        return self.harga * jumlah

    def tampilkan_informasi(self, jumlah):
        total_bayar = self.hitung_total_bayar(jumlah)

        print("Informasi Pembelian Tiket Pesawat")
        print("=================================")
        print("Rute: {} -> {}".format(self.asal, self.tujuan))
        print("Harga Tiket: Rp. {}".format(self.harga))
        print("Jumlah Tiket: {}".format(jumlah))
        print("Total Bayar: Rp. {}".format(total_bayar))


rute = {
    1: ("Balikpapan", "Jakarta", 800000),
    2: ("Balikpapan", "Surabaya", 600000)
}

print("Pilih rute:")
for key, value in rute.items():
    print("{} - {}: Rp. {}".format(key, value[1], value[2]))

pilihan = int(input("Masukkan pilihan: "))

if pilihan in rute:
    asal, tujuan, harga = rute[pilihan]
    jumlah = int(input("Masukkan jumlah tiket: "))

    tiket_pesawat = TiketPesawat(asal, tujuan, harga)
    tiket_pesawat.tampilkan_informasi(jumlah)
else:
    print("Pilihan tidak valid. Silakan pilih opsi yang tersedia.")
