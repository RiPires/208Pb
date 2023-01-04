#RiP
from matplotlib.pylab import *
import matplotlib.pyplot as plt
import csv

def PlotData(File):
    """
    Plots yield vs channel data from our .mca file

    INPUTS: "FileName.mca"
    OUTPUTS: yield vs channel plot
    """

    with open(File, 'r') as file:
        reader = csv.reader(file, delimiter="\n", skipinitialspace=True)
        data = list(reader)
    x = []
    y = []
    aux = []
    for i in range(12,len(data)-1):
        aux.append(data[i][0].split())
    for i in range(len(aux)):
        #x.append(float(0.004482*i-0.105144)) ## energy calibraion needs to be corrected
        x.append(float(i)) ## axes in channel
        y.append(float(aux[i][0]))

    fig, ax = plt.subplots()
    ax.plot(x,y,'.', color ='xkcd:black', label=(str(File)))
    #ax.semilogy(x,y,'^', color ='xkcd:purple', label=(str(File)))
    legend = ax.legend(loc="upper right",ncol=2, shadow=False,fancybox=True,framealpha = 0.0,fontsize=20)
    legend.get_frame().set_facecolor('#DAEBF2')
    tick_params(axis='both', which='major', labelsize=22)
    ##xlabel('Energy (MeV)',fontsize=22)
    xlabel('Channel',fontsize=22)
    ylabel('Counts', fontsize=22)
    grid()
    show()

    return
##################################################

PlotData('Data/Ra226_Calib_29-12.mca')
PlotData('Data/Ra226_E2.mca')
PlotData('Data/Ra226_F1.mca')
"""
PlotData('Data/Ra226_Calib_27-12.mca')
PlotData('Data/Ra226_D1.mca')
PlotData('Data/Ra226_E1.mca')

PlotData('Data/Ra226-Calib_20-12.mca')
PlotData('Data/Ra226-C1.mca')
PlotData('Data/Ra226-C1_after.mca')
PlotData('Data/Ra226-B2.mca')
PlotData('Data/Ra226-A2.mca')
PlotData('Data/Ra226-C1_stat.mca')
PlotData('Data/Ra226-A1.mca')
PlotData('Data/Ra226-C2.mca')
PlotData('Data/Ra226-A3.mca')"""