# Input Data
# NIM : 1124102195 
# NAMA : Scendy Aprianda Islamy

#study kasus = buatkan inputan data mahasiswa dan menyimpannya didalam dictionary.

#dictionary untuk menyimpan data
mahasiswa = {}

#inputan data dari mahasiswa
mahasiswa['Nama'] = input('Masukkan Nama : ')
mahasiswa['NIM'] = int(input('Masukkan NIM : '))
mahasiswa['Jurusan'] = input('Masukkan Jurusan : ')

#menampilkan data
print('Terimakasih sudah memasukkan data')
print('---------------------------------')
print('Nama :', mahasiswa['Nama'])
print('NIM :', mahasiswa['NIM'])
print('Jurusan :', mahasiswa['Jurusan'])
print('---------------------------------')
