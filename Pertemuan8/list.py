#list daftar belanja
belanja = ["Beras", "Telur", "Gula", "Garam"]

#mengecek apakah ada di daftar belanja?
if "Minyak" in belanja:
    print("Minyak sudah ada di daftar.")
else:
    print("Minyak belum ada, akan ditambahkan.")
    belanja.append("Minyak")

#hasil akhir
print("Daftar belanja:", belanja)