#Simulasi perhitungan kelulusan skor utbk

score = int(input("Masukkan skor UTBK: "))

if score >= 700:
    print("Selamat! Kamu berpeluang besar masuk PTN favoritmu!")
elif score >= 600:
    print("Selamat! Kamu memiliki peluang besar untuk diterima di PTN.")
elif score >= 550:
    print("Nilai kamu hampir mencapai batas aman, lebih giat belajarnya.")
elif score >= 500:
    print("Kesempatan masih terbuka, pertimbangkan strategi pemilihan universitas kamu.")
else:
    print("Skor kamu masih di bawah standar, lebih giat lagi belajarnya.")