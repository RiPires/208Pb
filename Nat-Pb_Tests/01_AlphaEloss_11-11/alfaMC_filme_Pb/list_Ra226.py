import csv

Output = open('Ra226_Calibrated.in', 'w')

with open('Ra226.in', 'r') as file:
    reader = csv.reader(file, delimiter="\n", skipinitialspace=True)
    data = list(reader) 
counts = []
aux = []

for i in range(0,len(data)):
    aux.append(data[i][0].split())
for i in range(len(aux)):
    counts.append(int(aux[i][0]))

for i in range(len(counts)):
    Output.write("{:.3f}".format((0.004479*(i+1)-0.00168))+'\t'+str(counts[i])+'\n')

Output.close()