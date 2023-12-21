import os
os.system('clear')

a = True 
limit = 5
i = 5

while a:
    i += 1 
    print(f'Menjalankan program {i}')
    if i == limit:
        a = False
        print('Program Berhenti Disini!')
    else:
        a = True
