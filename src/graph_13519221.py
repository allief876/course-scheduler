# File: graph_13519221.py
# 13519221 Allief Nuriman
# IF2211 2020-2
# Modul untuk [Pseudo] Graf

def readfile(m): # Akan membaca file lalu menyimpan di matriks dua dimensi, representasi, contoh: m[0][0] ialah matkul, m[0][i] dengan i > 0 ialah prasyarat-prasyarat matkul m[0][0]
    for i in range(len(m)): # Iterasi per line
        m[i] = m[i].replace(',','') # Delete tanda koma, ganti kosong
        m[i] = m[i].replace('.','') # Delete tanda titik, ganti kosong

    for i in range(len(m)):
        m[i] = m[i].split(" ") # Karena sekarang tiap baris cuma beda tanda " ", kita pisah lagi, sehingga dia bakal jadi array dua dimensi dengan m[0][i], i > 0 ialah prasyarat-prasyarat matkul m[0][0]
    
    return m

def tampilkanData(m): # Pada dasarnya ini dibuat untuk melakukan uji coba apakah isi file masuk ke variabel
    for i in range(len(m)):
        if (len(m[i]) == 1):
            print("Mata kuliah",end=' ')
            print(m[i][0],end=' ')
            print("tidak mempunyai prasyarat apapun")
        else:
            print("Mata kuliah",end=' ')
            print(m[i][0],end=' ')
            print("mempunyai prasyarat sebagai berikut:")
            for j in range(1,len(m[i])):
                print(m[i][j])
    print()


# Algoritma melakukan topologicalSorting, pada dasarnya
# variabel m berisi array dua dimensi
 # m[i][0] untuk i >= 0 merepresentasikan mata kuliah
 # dan m[i][j] untuk i >= 0 dan j > 0 merepresentasikan mata kuliah prasyarat m[i][0]
def topSort(m):
    sem = 1
    while (len(m) != 0): # Fungsi berjalan hingga m sudah berisi 0 elemen
        print("Semester",end=' ') 
        print(sem,end='')
        print(":",end=' ')
        terdelet = [] # Array ini digunakan untuk menyimpan semua mata kuliah yang
        for z in range(len(m)): # mempunyai "busur masuk" sebanyak 0, dengan kata lain hanya berisi m[0][0]
            if (len(m[z]) == 1):
                terdelet.append(m[z])
                print(m[z][0],end=' ')
        print()
        j = 0
        while (j < len(m)): # Dibuat untuk menghapus mata kuliah dgn busur masuk 0
            if (len(m[j]) == 1): # len(m[j]) == 1 mengimplikasikan hanya berisi m[0][0]
                m.pop(j)
            else:
                j += 1
        i = 0 # Navigasi ulang array of array m, untuk menghapus matkul dgn busur masuk 0 pd matkul yg membutuhkan m[0][0]
        while (i < len(m)): # Ini dilakukan karena m[0][0] sudah diambil
            j = 0
            while (j < len(m[i])):
                if (SyaratDiambil(m[i][j],terdelet)): # Karena terdelet adalah array of array dan m[i][j] adalah string, saya membuat
                    m[i].pop(j) # fungsi khusus untuk menangani ini
                    j = len(m[i])
                else:
                    j += 1
            if (not (j < len(m[i]))):
                i += 1
        terdelet = [] # Reset array of array yang menampung sekumpulan m[i][0] untuk iterasi selanjutnya
        sem += 1



def SyaratDiambil(a,b): # Fungsi khusus untuk menangani apakah terdapat elemen array of array yang sama persis dengan string a
    bebas = False
    i = 0
    while (i < len(b) and not bebas):
        bebas = False
        if (len(a) == len(b[i][0])):
            j = 0
            while (j < len(a)):
                if (a[j] != b[i][0][j]):
                    bebas = False
                else:
                    if (j == len(a) - 1): # Misalkan semua char pada a dan b sama persis
                        bebas = True # Maka kita set True
                j += 1
        else:
            bebas = False
        i += 1
    return bebas # Lalu kirimkan