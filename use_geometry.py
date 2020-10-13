print('Menggunakan from:')
from geometri.segitiga import hitung_luas_segitiga, info as info_segitiga
from geometri.persegipanjang import hitung_luas_persegi_panjang, info as info_persegipanjang
# from geometri.persegipanjang import hitung_luas_persegi_panjang, hitung_luas_segitiga

print(info_segitiga())
print(f'hitung_luas_segitiga {hitung_luas_segitiga(10, 3)}')

print(info_persegipanjang())
print(f'hitung_luas_persegi_panjang {hitung_luas_persegi_panjang(10, 3)}')

print('-' * 100)

print('Menggunakan import:')
import geometri.segitiga

print(f'hitung_luas_segitiga {geometri.segitiga.hitung_luas_segitiga(10, 3)}')

print('-' * 100)

print('Menggunakan import alias (as):')
import geometri.segitiga as gs

print(f'hitung_luas_segitiga {gs.hitung_luas_segitiga(10, 3)}')

print('-' * 100)


