a = 0
b = 1
fact= {0 : 1}
rangee = int(input('Masukan range data : '))
for i in range(rangee//2):
    z = 1
    for j in range(1,a+1):
        z = z * j
    fact[a] = z
    a += 2
print(fact)
n = int(input('Data ditampilkan : '))
if n >= rangee :
    print('Data tidak ditemukan')
elif n%2 == 1 :
    print('Data tidak ditemukan')
else :
    print(f'Data ditemukan {n} : {fact[n]}')


