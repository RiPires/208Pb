import csv

Output = open('Ra226_29-12_Calibrated.in', 'w') ## Change name of the output file according
                                          ## with the calibration in question
with open('Ra226_29-12.in', 'r') as file: ## Also change input file name
    reader = csv.reader(file, delimiter="\n", skipinitialspace=True)
    data = list(reader) 
counts = []
aux = []

for i in range(0,len(data)):
    aux.append(data[i][0].split())
for i in range(len(aux)):
    counts.append(int(aux[i][0]))

for i in range(len(counts)):
    #Output.write("{:.3f}".format((0.004470*(i+1)-0.00-2.406))+'\t'+str(counts[i])+'\n') ## 20 Dez. calibration
    #Output.write("{:.3f}".format((0.004492*(i+1)+2.816))+'\t'+str(counts[i])+'\n') ## 27 Dez. calibration
    Output.write("{:.3f}".format((0.004479*(i+1)+13.297))+'\t'+str(counts[i])+'\n') ## 29 Dez. calibration

Output.close()