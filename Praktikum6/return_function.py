# NIM : 1124102195 
# NAMA : Scendy Aprianda Islamy

def hitung_luas(panjang, lebar):
    luas = panjang * lebar
    return luas

nama_bangunan = input("Nama bangunan : ")
panjang = float(input("Panjang : "))
lebar = float(input("Lebar : "))

luas_total = hitung_luas(panjang, lebar)
print("Bangunan      :", nama_bangunan)
print("Panjang       :", panjang, "m")
print("Lebar         :", lebar, "m")
print("Luas bangunan :", luas_total, "m²")