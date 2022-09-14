a = int(input('Masukkan range data: '))
data = dict()
for x in range(a):
    if x % 2 == 0:
        n = x
        f = 1
        for y in range(1,n+1):
            f = f * y
        data[x]=f
print(data)
c = int(input('Data ditampilkan :'))
if c in data.keys():
    print('Data ditemukan')
else:
    print('Data tidak ditemukan')
