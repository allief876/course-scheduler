# File: graph_13519221.py
# 13519221 Allief Nuriman
# IF2211 2020-2

def readfile(m): # Akan membaca file lalu menyimpan di matriks dua dimensi, representasi, contoh: m[0][0] ialah matkul, m[0][i] dengan i > 0 ialah prasyarat-prasyarat matkul m[0][0]
    for i in range(len(m)): # Iterasi per line
        m[i] = m[i].replace(',','') # Delete tanda koma, ganti kosong
        m[i] = m[i].replace('.','') # Delete tanda titik, ganti kosong

    for i in range(len(m)):
        m[i] = m[i].split(" ") # Karena sekarang tiap baris cuma beda tanda " ", kita pisah lagi, sehingga dia bakal jadi array dua dimensi dengan m[0][i], i > 0 ialah prasyarat-prasyarat matkul m[0][0]
    
    return m

def tampilkanData(m):
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

def topSort(m):
    sem = 1
    while (len(m) != 0):
        print("Semester",end=' ')
        print(sem,end='')
        print(":",end=' ')
        terdelet = []
        for z in range(len(m)):
            if (len(m[z]) == 1):
                terdelet.append(m[z])
                print(m[z][0],end=' ')
        print()
        j = 0
        while (j < len(m)):
            if (len(m[j]) == 1):
                m.pop(j)
            else:
                j += 1
        i = 0
        while (i < len(m)):
            j = 0
            while (j < len(m[i])):
                if (SyaratDiambil(m[i][j],terdelet)):
                    m[i].pop(j)
                    j = len(m[i])
                else:
                    j += 1
            if (not (j < len(m[i]))):
                i += 1
        terdelet = []
        sem += 1

def SyaratDiambil(a,b):
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
                    if (j == len(a) - 1):
                        bebas = True
                j += 1
        else:
            bebas = False
        i += 1
    return bebas