print("Nama          :Aisyah")
print("Nim           :231031093")
print("prodi         :Sistem Informasi C")
print("Tanggal Lahir :05-08-2005")
#operator penugasan
print()
a =93
a +=1
print ('Nilai a +=1 akan menjadi',a)
a =93
a -=1
print ('Nilai a -=1 akan menjadi',a)
a =93
a *=2
print ('Nilai a *=2 akan menjadi',a)
a =93
a /=2
print ('Nilai a /=2 akan menjadi',a)
a =93
a %=2
print ('Nilai a %=2 akan menjadi',a)
a =93
a //=2
print ('Nilai a //=2 akan menjadi',a )
a =93
a **=2
print ('Nilai a **=2 akan menjadi',a )
#OR
b = True
print ('Nilai b =',b )
b |= False
print ('Nilai b|= False akan menjadi',b )
b = False
print ('Nilai b =',b )
b |= False
print ('Nilai b|= False akan menjadi',b )
# AND
b = True
print ('Nilai b =',b )
b &= False
print ('Nilai b&= False akan menjadi',b )
b = False
print ('Nilai b =',b )
b &= False
print ('Nilai b&= False akan menjadi',b )
# XOR
b = True
print ('Nilai b =',b )
b ^= False
print ('Nilai b^= False akan menjadi',b )
b = False
print ('Nilai b =',b )
b ^= False
print ('Nilai b^= False akan menjadi',b )
# Shifting
c =0b0100
print ('Nilai c =',format (c , '04b') )
c >>=1
print ('Nilai c > >=1 akan menjadi ',format (c , '04b') )
c =0b0100
c <<=1
print ('Nilai c < <=1 akan menjadi ',format (c , '04b') )

#operator Komparasi/Perbandingan
a =8 
b =13
print (’ ================== Besar dari 13 ’)
hasil = a >13
print (a ,’> 13 adalah ’, hasil )
hasil = b >13
print (b ,’> 13 adalah ’, hasil )

print (' ================== Kecil dari 13')

print (a ,’< 13 adalah ’, hasil )

print (b ,’< 13 adalah ’, hasil )

print (’ ================== Besar atau sama dari 13 ’)

print (a ,’ >= 13 adalah ’, hasil )

print (b ,’ >= 13 adalah ’, hasil )

print (’ ================== Besar atau sama dari 13 ’)

print (a ,’== 13 adalah ’, hasil )

print (b ,’== 13 adalah ’, hasil )

print (’ ================== Tidak sama dengan 13 ’)

print (a ,’!= 13 adalah ’, hasil )

print (b ,’!= 13 adalah ’, hasil )

#logika
print (’ ============= NOT ============= ’)
a=True
c = not a
print ('a adalah a', a) 
print (’ - - - - - -c = not a- - - - - - - NOT ’)
print (’c adalah ’,c )

print (’ ============= OR ============= ’)
a=True
b=True
c=a or b
print (a, 'OR', b, 'menjadi',c)

a=True
b=True
c=a or b
print (a, 'OR', b, 'menjadi', c)

a=True
b=True
c=a or b
print (a, 'OR',b, 'menjadi',c)

a=False
b=True
c=a or b
print(a, 'OR',b,'menjaadi',c)

a=False
b=False
c=a or b
print(a, 'OR',b,'menjaadi',c)

print (’ ============= AND ============= ’)
a=True
b=True
c=a and b
print (a ,’AND ’,b ,’menjadi ’,c )

a=True
b=False
c=a and b 
print (a ,’AND ’,b ,’menjadi ’,c)

a=False
b=True
c=a and b
print (a ,’AND ’,b ,’menjadi ’,c)

a=False
b=False
c=a and b 
print (a ,’AND ’,b ,’menjadi ’,c)

print (’ ============= XOR ============= ’)
a=True
b=True
c = a ^ b
print (a ,’^’,b ,’menjadi ’,c )

a=True
b=False
c = a ^ b
print (a ,’^’,b ,’menjadi ’,c )

a=False
b=True
c = a ^ b
print (a ,’^’,b ,’menjadi ’,c )

a=False
b=False
c = a ^ b
print (a ,’^’,b ,’menjadi ’,c )

# TUGAS
# Buat kode untuk masing masing operator berikut
print (’ ============= NAND ============= ’)
print (’ ============= NOR ============== ’)
print (’ ============= NXOR ============= ’)

#membership
print (’ ======================= IN ’)
nama_lengkap = ’ Bacharuddin Jusuf Habibie ’
test = ’a’
cek = test in nama_lengkap
print ( test +’ terdapat di ’+ nama_lengkap +’ adalah ’+ str( cek ) )

test = ’rud 
cek = test in nama_lengkap
print ( test +’ terdapat di ’+ nama_lengkap +’ adalah ’+ str( cek ) )

test = ’bac ’
cek = test in nama_lengkap
print ( test +’ terdapat di ’+ nama_lengkap +’ adalah ’+ str( cek ) )

print (’ ======================= NOT IN ’)
nama_lengkap = ’ Bacharuddin Jusuf Habibie ’
test = ’a’
cek = test not in nama_lengkap
print ( test +’ tidak terdapat di ’+ nama_lengkap +’ adalah ’+str ( cek←-
) )

test = ’rud ’
cek = test not in nama_lengkap
print ( test +’ tidak terdapat di ’+ nama_lengkap +’ adalah ’+str ( cek←-
) )

test = ’bac ’
cek = test not in nama_lengkap
print ( test +’ tidak terdapat di ’+ nama_lengkap +’ adalah ’+str ( cek←-
) )

# TUGAS
# Dengan cara yang sama buat operator in dan not in , ubah nama ←-
lengkap menjadi nama masing - masing dengan uji test
test1 = ab # pilih dua huruf berurut yang ada pada nama anda
test2 = ba # balik dua huruf tersebut
test3 = ’a’
test4 = ’i’
test5 = ’u’
test6 = ’e’
test7 = ’o’
