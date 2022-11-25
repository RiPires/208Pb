#RiP
from matplotlib.pylab import *
import matplotlib.pyplot as plt
import csv

#############################################
###   Plot RBS .dat funntion definition   ###
#############################################
def VdG_Plot(File, dataLabel):
    """
    Converts .dat files from VdG RBS into yield and channel lists
    INPUTS:
        "FILENAME.dat"
    OUTPUTS:
        Yield and Channel lists
    HOW TO USE:
        MyYield, MyChannel = VdG_dat2Lists("MyFile.mca")
    """
    with open(File, 'r') as file:
        reader = csv.reader(file, delimiter="\n", skipinitialspace=True)
        data = list(reader)
    ch = []
    y = []
    aux = []
    for i in range(128):
        aux.append(data[i][0].split())
    #print(aux)
    for i in range(len(aux)):
        for k in range(8):
            #ch.append(int(8*(i)+k+1)) ## axes in channel
            #ch.append((int(8*(i)+k+1))*2.3681+94.322) ## axes in keV for ALFAS
            ch.append((int(8*(i)+k+1))*2.4082+42.288) ## axes in keV for PROTONS
            y.append(float(aux[i][k]))
    
    fig, ax = plt.subplots()
    ax.plot(ch,y,'.', color ='xkcd:black', label=(str(dataLabel)))
    #ax.semilogy(ch,y,'.', color ='xkcd:purple', label=(str(File)))
    legend = ax.legend(loc="upper right",ncol=2, shadow=False,fancybox=True,framealpha = 0.0,fontsize=20)
    legend.get_frame().set_facecolor('#DAEBF2')
    tick_params(axis='both', which='major', labelsize=22)
    xlabel('Energy (keV)',fontsize=22)
    #xlabel('Channel',fontsize=22)   
    ylabel('Yield', fontsize=22)
    grid()
    show()
#############################################
#############################################

#######################################################
###   Plot two RBS .dat files funntion definition   ###
#######################################################
def VdG_PlotBoth(File1, File2):
    """
    Converts two .dat files from VdG RBS into yield and channel lists
    and plots both
    INPUTS:
        "FILENAME1.dat",'FILENAME2.dat'
    OUTPUTS:
        Plots
    """
    ## Creates channel yield lists for File1 and
    # converts channel to energy
    with open(File1, 'r') as file:
        reader = csv.reader(file, delimiter="\n", skipinitialspace=True)
        data = list(reader)
    ch1 = []
    y1 = []
    aux = []
    for i in range(128):
        aux.append(data[i][0].split())
    #print(aux)
    for i in range(len(aux)):
        for k in range(8):
            #ch1.append((int(8*(i)+k+1))*2.3681+94.322) ## axes in keV for ALFAS
            ch1.append((int(8*(i)+k+1))*2.4082+42.288) ## axes in keV for PROTONS
            y1.append(float(aux[i][k]))

    ## Creates channel yield lists for File2 and
    # converts channel to energy
    with open(File2, 'r') as file:
        reader = csv.reader(file, delimiter="\n", skipinitialspace=True)
        data = list(reader)
    ch2 = []
    y2 = []
    aux = []
    for i in range(128):
        aux.append(data[i][0].split())
    #print(aux)
    for i in range(len(aux)):
        for k in range(8):
            #ch1.append((int(8*(i)+k+1))*2.3681+94.322) ## axes in keV for ALFAS
            ch1.append((int(8*(i)+k+1))*2.4082+42.288) ## axes in keV for PROTONS
            y2.append(float(aux[i][k]))
    
    fig, ax = plt.subplots()
    #ax.plot(ch1,y1,'.', color ='xkcd:blue', label=(str(File1)))
    #ax.plot(ch2,y2,'+', color ='xkcd:red', label=(str(File2)))
    ax.semilogy(ch1,y1,'.', color ='xkcd:blue', label=(str(File1)))
    ax.semilogy(ch2,y2,'+', color ='xkcd:red', label=(str(File2)))
    legend = ax.legend(loc="upper right",ncol=1, shadow=False,fancybox=True,framealpha = 0.0,fontsize=20)
    legend.get_frame().set_facecolor('#DAEBF2')
    tick_params(axis='both', which='major', labelsize=22)
    xlabel('Energy (keV)',fontsize=22)
    ylabel('Yield', fontsize=22)
    grid()
    show()
#############################################
#############################################

###                 Plots                     ###

"""
###############   ALFAS   ###############
VdG_Plot('1122/alfas/RBS1run_1.dat', 'Calib Ta-V-Nb') # Calibration V-Ta-Nb    

VdG_Plot('1122/alfas/RBS1run2.dat', 'target 1 - 21 mm') ## Target 1 - large hole
VdG_Plot('1122/alfas/RBS1run3.dat', 'target 1 - 23 mm') ## Target 1 - large hole
VdG_Plot('1122/alfas/RBS1run4.dat', 'target 1 - 25 mm') ## Target 1 - large hole
VdG_Plot('1122/alfas/RBS1run5.dat', 'target 1 - 27 mm') ## Target 1 - large hole

VdG_Plot('1122/alfas/RBS1run8.dat', 'target 2 - 44 mm') ## Target 2 - formvar
VdG_Plot('1122/alfas/RBS1run09.dat', 'target 2 - 46 mm') ## Target 2 - formvar

VdG_Plot('1122/alfas/RBS1run10.dat', 'target 3 - 55 mm') ## Target 3 - small hole
VdG_Plot('1122/alfas/RBS1run11.dat', 'target 3 - 57 mm') ## Target 3 - small hole

VdG_Plot('1122/alfas/RBS1run12.dat', 'target 4 - 66 mm') ## Target 4 - small hole
VdG_Plot('1122/alfas/RBS1run14.dat', 'target 4 - 65 mm') ## Target 4 - small hole

#################################################
VdG_PlotBoth('1122/alfas/RBS1run10.dat', '1122/alfas/RBS1run11.dat')
VdG_PlotBoth('1122/alfas/ERDrun10.dat', '1122/alfas/ERDrun11.dat')
VdG_PlotBoth('1122/alfas/RBS2run10.dat', '1122/alfas/RBS2run11.dat')
"""

###############   PROTOES   ###############
VdG_Plot('1122/protoes/RBS1run16.dat', 'Calib Ta-V-Nb') # Calibration V-Ta-Nb    

VdG_Plot('1122/protoes/RBS1run_17.dat', 'target 1 - 21 mm') ## Target 1 - large hole
VdG_Plot('1122/protoes/RBS1run18.dat', 'target 1 - 23 mm') ## Target 1 - large hole
VdG_Plot('1122/protoes/RBS1run19.dat', 'target 1 - 21 mm') ## Target 1 - large hole
VdG_Plot('1122/protoes/RBS1run20.dat', 'target 1 - 25 mm') ## Target 1 - large hole
VdG_Plot('1122/protoes/RBS1run21.dat', 'target 1 - 27 mm') ## Target 1 - large hole

VdG_Plot('1122/protoes/RBS1run22.dat', 'target 2 - 44 mm') ## Target 2 - formvar
VdG_Plot('1122/protoes/RBS1run23.dat', 'target 2 - 46 mm') ## Target 2 - formvar

VdG_Plot('1122/protoes/RBS1run24.dat', 'target 3 - 55 mm') ## Target 3 - small hole
VdG_Plot('1122/protoes/RBS1run25.dat', 'target 3 - 57 mm') ## Target 3 - small hole

VdG_Plot('1122/protoes/RBS1run26.dat', 'target 4 - 66 mm') ## Target 4 - small hole
VdG_Plot('1122/protoes/RBS1run27.dat', 'target 4 - 65 mm') ## Target 4 - small hole