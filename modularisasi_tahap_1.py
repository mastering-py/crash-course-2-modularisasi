"""
Program menghitung luas segitiga
luas_segita = alas * tinggi / 2
"""
print('Menghitung luas segitiga 1')
alas = 10
tinggi = 6
luas_segitiga = alas * tinggi / 2

print(f'Segitiga dengan alas = {alas} dan tinggi = {tinggi} memiliki luas = {int(luas_segitiga)}')

print('\nMenghitung luas segitiga 2 dengan copy paste')
alas = 20
tinggi = 2
luas_segitiga = alas * tinggi / 2

print(f'Segitiga dengan alas = {alas} dan tinggi = {tinggi} memiliki luas = {luas_segitiga}')

print(f'\nMenghitung luas segitiga menggunakan fungsi, argumen, input dan return')
def hitung_luas_segitiga(alas, tinggi):
    luas_segitiga = alas * tinggi / 2
    return luas_segitiga

# Pemanggilan:
# cara 1 (langsung menampilkan dengan fungsi print()):
# print(hitung_luas_segitiga(20, 2))

# cara 2 (menampung ke dalam variable):
# a = hitung_luas_segitiga(20, 2)
# print(a)

# cara 3 (menggunakan input):
alas = int(input("Masukkan alas: "))
tinggi = int(input("Masukkan tinggi: "))
print(f'Segitiga dengan alas = {alas} dan tinggi = {tinggi} memiliki luas = {hitung_luas_segitiga(alas, tinggi)}')

# lainnya:
# print(f'Luas segitiga adalah: {hitung_luas_segitiga(10, 6)}')
# print(f'Luas segitiga adalah: {hitung_luas_segitiga(10, 3)}')
# a = hitung_luas_segitiga(20, 6)
# print(f'Luas segitiga adalah: {a}')

# print(f'\nMenghitung luas segitiga menggunakan 2 fungsi, argumen dan input')
# def hitung_luas_segitiga(alas, tinggi):
#     luas_segitiga = alas * tinggi / 2
#     print(f'Segitiga dengan alas = {alas} dan tinggi = {tinggi} memiliki luas = {luas_segitiga}')
#
# def Utama():
#     a = int(input("Masukkan alas: "))
#     b = int(input("Masukkan tinggi: "))
#     hitung_luas_segitiga(a, b)
#
# Utama()

