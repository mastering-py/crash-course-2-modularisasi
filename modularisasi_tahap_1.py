"""
Program menghitung luas segitiga
luas_segita = alas * tinggi / 2
"""
print('Menghitung luas segitiga 1:')
alas = 10
tinggi = 6
luas_segitiga = alas * tinggi / 2

print(f'Segitiga dengan alas = {alas} dan tinggi = {tinggi} memiliki luas = {int(luas_segitiga)}')

print('-' * 100)

print('Menghitung luas segitiga 2 dengan copy paste:')
alas = 20
tinggi = 2
luas_segitiga = alas * tinggi / 2

print(f'Segitiga dengan alas = {alas} dan tinggi = {tinggi} memiliki luas = {luas_segitiga}')

print('-' * 100)

print(f'Memebuat fungsi hitung_luas_segitiga:')
def hitung_luas_segitiga(alas, tinggi):
    luas_segitiga = alas * tinggi / 2
    return luas_segitiga


# Pemanggilan:
# cara 1 (langsung menampilkan dengan fungsi print()):
print(hitung_luas_segitiga(10, 6))
print(hitung_luas_segitiga(20, 2))

print('-' * 5)

# cara 2 (menampung ke dalam variable):
a = hitung_luas_segitiga(20, 2)
print(a)

print('-' * 5)

# cara 3 (menggunakan input):
alas = int(input("Masukkan alas: "))
tinggi = int(input("Masukkan tinggi: "))
print(f'Segitiga dengan alas = {alas} dan tinggi = {tinggi} memiliki luas = {hitung_luas_segitiga(alas, tinggi)}')

print('-' * 5)

# lainnya:
print(f'Luas segitiga adalah: {hitung_luas_segitiga(10, 6)}')
print(f'Luas segitiga adalah: {hitung_luas_segitiga(20, 2)}')
a = hitung_luas_segitiga(100, 2)
print(f'Luas segitiga adalah: {a}')

print('-' * 100)

print(f'Menghitung luas segitiga menggunakan 2 fungsi, argumen dan input')
def hitung_luas_segitiga(alas, tinggi):
    luas_segitiga = alas * tinggi / 2
    return luas_segitiga
    # print(f'Segitiga dengan alas = {alas} dan tinggi = {tinggi} memiliki luas = {luas_segitiga}')  # print dapat juga
    # ditampung disini, asalkan return dihilangkan

def Utama():
    # Cara 1:
    # print(hitung_luas_segitiga(20, 2))

    # Cara 2:
    # a = hitung_luas_segitiga(20, 2)
    # print(a)

    # Cara 3:
    a = int(input("Masukkan alas: "))
    b = int(input("Masukkan tinggi: "))
    # print(hitung_luas_segitiga(a, b))
    # atau
    c = hitung_luas_segitiga(a, b)
    print(f'Segitiga dengan alas = {a} dan tinggi = {b} memiliki luas = {c}')

Utama()
