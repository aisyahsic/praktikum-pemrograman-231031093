#praktikum-c4

nim = ['2','3','1','0','3','1','0','9','3']
print(nim)

print('item indeks 0 (pertama)',nim[0])
print('item indeks 1 (kedua)',nim[1])

print(f'item indeks 0 (pertama){nim[0]}')
print(f'item indeks 1 (kedua){nim[1]}')
print(f'item indeks terakhir {nim[len(nim)-1]}')
print(f'item indeks terakhir {nim[-1]}')
print(f'item indeks (pertama) {nim[-len(nim)]}')
print()
#latihan list      
data = ['Aisyah',2023,'Aktif']
nilai= [90,89,93,97]

print('Nama: '+ data[0])
print('angkatan:', data[1])
print('status: '+ data[2])
print()
print(f'{data[0]} status kuliah\t: {data[2]}')
print(f'Data terbesar nilai adalah\t: {nilai[3]}')
print(f'Data terkecil nilai adalah\t: {nilai[1]}')
print(f'Rata-rata Nilai adalah\t: {sum(nilai)/len(nilai)}')
print()
data = ('mahasiswa1',2023,'Aktif')
nilai= (90,89,93,97)

print(data[1])
print(data[-1])
print(nilai[1:-1])
print()

#latihan nested list
data = [('Aisyah',2023,'Aktif'),

(90,89,93,97),
(20,22),
('S1-Reguler','Ganjil')]

print(data[0][0])
print(data[-1][0])
print(data[2][0:])
print()
print(f'Program pendidikan Aisyah: {data[0][0]} {data[-1][0]}\')
print(f'Angkatan: {data[0][1]} {data[-1][1]}\')
print(f'Jumlah nilai {data[0][0] adalah: {len(data[1])}\')
print  


