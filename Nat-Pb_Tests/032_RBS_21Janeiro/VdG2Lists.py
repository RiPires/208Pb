import csv

def vdg2lists(File):
    """
    Creates Channel and Yield lists from Van de Graaff aquisition .dat files
    INPUTS:
    str('FileName')
    OUTPUTS: Channel, Yield
    """
    with open(File, 'r') as file:
        reader = csv.reader(file, delimiter="\n", skipinitialspace=True)
        data = list(reader)
    Channel = []
    Yield = []
    aux = []
    for i in range(128):
        aux.append(data[i][0].split())
    for i in range(len(aux)):
        for k in range(8):
            Channel.append(int(8*i+k+1)) ## Axes in channel
            Yield.append(float(aux[i][k]))
    return Channel, Yield