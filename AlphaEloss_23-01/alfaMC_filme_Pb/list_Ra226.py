import csv

Output = open('Ra226_23-01_Calibrated.in', 'w') ## Change name of the output file according
                                          ## with the calibration in question
with open('Ra226_23-01.in', 'r') as file: ## Also change input file name
    reader = csv.reader(file, delimiter="\n", skipinitialspace=True)
    data = list(reader) 
counts = []
aux = []

for i in range(0,len(data)):
    aux.append(data[i][0].split())
for i in range(len(aux)):
    counts.append(int(aux[i][0]))

for i in range(len(counts)):
    Output.write("{:.3f}".format((0.004471*(i+1)+0.002075))+'\t'+str(counts[i])+'\n') ## 23 Jan. calibration 2

Output.close()