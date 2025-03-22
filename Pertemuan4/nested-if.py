#Simulasi perhitungan kelulusan skor utbk

score = int(input("Masukkan skor UTBK: "))

if score >= 700:
    print("Selamat! Kamu berpeluang besar masuk PTN favoritmu.")
    if score <= 500:
        print("Kamu punya peluang sangat tinggi untuk diterima di PTN terbaik!")
    else:
        print("Skor kamu cukup tinggi, lebih semangat lagi.")
else:
    print("Skor kamu masih rendah,tetap semangat dan terus belajar.")
