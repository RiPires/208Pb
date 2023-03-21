import csv

def SimNRA2Lists(File):
    """
    Converts .csv files with output from SimNRA Fits into
    lists of channel and yield to be used to plot with matplotlib
    INPUTS:
        "FILENAME.dat
    OUTPUTS:
     
     """

    with open(File, 'r') as file:
        reader = csv.reader(file, delimiter="\n", skipinitialspace=True)
        data = list(reader)
    Channel = []
    Yield = []
    aux = []
    #print(data)
    for i in range(1,len(data)):
        aux.append(data[i][0].split())
    print(aux)
    for i in range(len(aux)):
        for k in range(18):
            Channel.append(aux[i][0])
            Yield.append(aux[i][2])
    
    print(len(Channel))

    return Channel, Yield