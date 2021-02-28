# File: 13519221.py
# 13519221 Allief Nuriman
# IF2211 2020-2
# Main program, jalankan ini

import graph_13519221 as dag

print("Program ini secara otomatis akan berjalan untuk melakukan sorting pada matkul.txt")
file = open("matkul.txt",'r')
cc = file.read().splitlines()
m = dag.readfile(cc) # Baca file lalu masukkan ke m
dag.topSort(m)