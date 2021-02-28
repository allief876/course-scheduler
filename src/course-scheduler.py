import directed_acyclic_graph as dag

file = open("matkul.txt",'r')
cc = file.read().splitlines()

print(cc[0][0])