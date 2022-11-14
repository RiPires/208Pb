#RiP
from matplotlib.pylab import *
import matplotlib.pyplot as plt
import csv

def PlotData(File):

    with open(File, 'r') as file:
        reader = csv.reader(file, delimiter="\n", skipinitialspace=True)
        data = list(reader)
    
    energy = []
    counts = []
    aux = []
    
    for i in range(2,len(data)): ## 2 is the third line
        aux.append(data[i][0].split())
    for i in range(len(aux)):
        energy.append(float(aux[i][0]))
        counts.append(float(aux[i][1]))

    fig, ax = plt.subplots()
    ax.plot(energy,counts,'-', color ='xkcd:red', label=(str(File)))
    legend = ax.legend(loc="upper right",ncol=1, shadow=True,fancybox=True,framealpha = 0.0,fontsize=20)
    legend.get_frame().set_facecolor('#DAEBF2')
    tick_params(axis='both', which='major', labelsize=22)
    xlabel('Energy',fontsize=22)
    ylabel('Yield', fontsize=22)
    show()

#Energy in detector

# Source calibration
#PlotData("Edet.csv")


def NormalizeInRnage(data):
    """
    Finds the max. value in a specific range
    and Normalizes a list to it 
    returns a new list 
    """
    new_data = []
    for i in range(100, len(data)):
        new_data.append(data[i])
    max_value = max(new_data)
    
    norm_data = []
    for entrie in data:
        norm_data.append(entrie/max_value)
    return norm_data

##   Plots both spectrums from data and simulation   ###############################
def PlotBoth(dataFile, simuFile):

    ### opens data file and fills lists   ###
    with open(dataFile, 'r') as fileData:
        reader = csv.reader(fileData, delimiter="\n", skipinitialspace=True)
        data = list(reader)
    data_Energy = []
    data_Counts = []
    aux = []
    for i in range(12,len(data)-1): ## 12
        aux.append(data[i][0].split())
    for i in range(len(aux)):
        data_Energy.append(float(0.004479*i-0.00168)) ## convert channel to energy, calibration updated
        data_Counts.append(float(aux[i][0]))

    ###   opens simulation file and fills lists   ###
    with open(simuFile, 'r') as fileSimu:
        reader = csv.reader(fileSimu, delimiter="\n", skipinitialspace=True)
        dataSimu = list(reader)
    simu_Energy = [] ## in keV
    simu_Counts = []
    aux = []
    for i in range(2,len(dataSimu)): ## 2 is the third line
        aux.append(dataSimu[i][0].split())
    for i in range(len(aux)):
        simu_Energy.append(float(aux[i][0]))
        simu_Counts.append(float(aux[i][1]))

    
    data_Counts = NormalizeInRnage(data_Counts)
    simu_Counts = NormalizeInRnage(simu_Counts)
    
    ###   Plots   ###
    fig, ax = plt.subplots()
    ax.plot(data_Energy,data_Counts,'.', color ='xkcd:black', label=(str(dataFile)))
    ax.plot(simu_Energy,simu_Counts,'-', color ='xkcd:red', label=(str(simuFile)))
    legend = ax.legend(loc="upper right",ncol=1, shadow=True,fancybox=True,framealpha = 0.0,fontsize=20)
    legend.get_frame().set_facecolor('#DAEBF2')
    tick_params(axis='both', which='major', labelsize=22)
    xlabel('Energy [MeV]',fontsize=22)
    ylabel('Normalized yield', fontsize=22)
    show()

    return
########################################################################

PlotBoth('AlphaEloss_11-11/Ra226_Calib.mca', 'Edet_Calib.csv')
PlotBoth('AlphaEloss_11-11/Ra226_BigHole.mca', 'Edet_560nm.csv')
PlotBoth('AlphaEloss_11-11/Ra226_SmallHole.mca', 'Edet_560nm.csv')