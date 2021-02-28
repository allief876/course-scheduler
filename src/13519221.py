import graph_13519221 as dag

file = open("matkul.txt",'r')
cc = file.read().splitlines()
m = dag.readfile(cc) # Baca file lalu masukkan ke m
dag.topSort(m)