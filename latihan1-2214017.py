def functionHarga():
    print("Aplikasi pembelian tiket")

    nik = input("input nik anda = ")
    nama = input("input nama anda = ")
    tujuan = input("List tujuan \n A. samarinda Rp. 45.000 \n B. botang Rp. 45.000 \n C. longkali Rp. 45.000 \n input tujuan anda = ")
    jumlah = int(input("input jumlah tiket yang anda beli = "))

    hargaTujuan = 0
    destinasi = ""

    if tujuan == "A": 
        hargaTujuan = 45000
        destinasi = "samarinda"
    if tujuan == "B":
        hargaTujuan = 65000
        destinasi = "bontang"
    if tujuan == "C":
        hargaTujuan = 45000
        destinasi = "longkali"

    totalHarga = hargaTujuan * jumlah
    totalHargaPlusPajak = totalHarga * 0.1
    totalHargaAkhir = totalHarga + totalHargaPlusPajak

    print("--STRUK--")
    print("nik = ", nik)
    print("nama = ", nama)
    print("tujuan = ", destinasi)
    print("harga tujuan = Rp. ", hargaTujuan)
    print("jumlah tiket = ", jumlah)
    print("total harga = Rp. ", totalHarga)
    print("total harga plus pajak = Rp. ", int(totalHargaPlusPajak))
    print("total bayar = Rp. ", int(totalHargaAkhir))
    
    daftar = [nik, nama, destinasi]

    beliLagi = input("apakah anda ingin membeli lagi? ")
    if beliLagi == "y":
        functionHarga()
    else:
        print("terima kasih telah membeli tiket bersama kami")

functionHarga()