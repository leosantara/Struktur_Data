import time
def iteratif(n, list):
    for i in range(6,n+1):
        z2 = i - 2
        z1 = i//2
        a = (list[z1-1])+(list[z2-1])
        list.append(a)
    print(f'Iteratif suku ke-{n} : ',list[n-1])
list = [1,2,3,4,5]
n = int(input('suku ke-'))
mulai = time.time()
iteratif(n, list)
akhir = time.time()
print(f'Waktu Iteratif suku ke-{n} : ', akhir-mulai)

def rekursif(n):
    list= [1,2,3,4,5]
    if n <= 5 :
        return list[n-1]
    else :
        return rekursif(n//2)+rekursif(n-2)
#n = int(input('Suku ke-'))
mulai = time.time()
print(f'Rekursif suku ke-{n} :',  rekursif(n))
akhir = time.time()
print(f'Waktu Rekursif suku ke-{n} : ',akhir-mulai)
