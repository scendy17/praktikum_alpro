# NIM : 1124102195 
# NAMA : Scendy Aprianda Islamy

def hitung_diskon(harga, diskon_persen):
    diskon = harga * (diskon_persen / 100)
    harga_setelah_diskon = harga - diskon
    return harga_setelah_diskon

nama_barang = input("Nama barang : ")
harga_barang = float(input("Harga barang : "))
diskon = float(input("Diskon : "))

harga_final = hitung_diskon(harga_barang, diskon)
print(f"\nBarang: {nama_barang}")
print(f"Harga awal : Rp.{int(harga_barang):,d}")
print(f"Diskon     : {diskon}%")
print(f"Harga akhir: Rp.{int(harga_final):,d}")
