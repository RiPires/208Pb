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
    for i in range(len(aux)):
        for k in range(8):
            ch.append(int(8*(i)+k+1)) ## axes in channel
            #ch.append((int(8*(i)+k+1))*2.3681+94.322) ## axes in keV for ALFAS w/ RBS1
            #ch.append((int(8*(i)+k+1))*2.4082+42.288) ## axes in keV for PROTONS w/ RBS1
            y.append(float(aux[i][k]))
    
    fig, ax = plt.subplots()
    ax.plot(ch,y,'.', color ='xkcd:black', label=(str(dataLabel)))
    #ax.semilogy(ch,y,'.', color ='xkcd:purple', label=(str(File)))
    legend = ax.legend(loc="upper right",ncol=2, shadow=False,fancybox=True,framealpha = 0.0,fontsize=20)
    legend.get_frame().set_facecolor('#DAEBF2')
    tick_params(axis='both', which='major', labelsize=22)
    #xlabel('Energy (keV)',fontsize=22)
    xlabel('Channel',fontsize=22)   
    ylabel('Yield', fontsize=22)
    grid()
    show()
#############################################
#############################################

#############################################
###   Plot RBS .dat funntion definition   ###
#############################################
def VdG_Plot_logy(File, dataLabel):
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
    for i in range(len(aux)):
        for k in range(8):
            ch.append(int(8*(i)+k+1)) ## axes in channel
            #ch.append((int(8*(i)+k+1))*2.3681+94.322) ## axes in keV for ALFAS w/ RBS1
            #ch.append((int(8*(i)+k+1))*2.4082+42.288) ## axes in keV for PROTONS w/ RBS1
            y.append(float(aux[i][k]))
    
    fig, ax = plt.subplots()
    #ax.plot(ch,y,'.', color ='xkcd:black', label=(str(dataLabel)))
    ax.semilogy(ch,y,'.', color ='xkcd:purple', label=(str(dataLabel)))
    legend = ax.legend(loc="upper right",ncol=2, shadow=False,fancybox=True,framealpha = 0.0,fontsize=20)
    legend.get_frame().set_facecolor('#DAEBF2')
    tick_params(axis='both', which='major', labelsize=22)
    #xlabel('Energy (keV)',fontsize=22)
    xlabel('Channel',fontsize=22)   
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
            ch1.append((int(8*(i)+k+1))*2.3681+94.322) ## axes in keV for ALFAS
            #ch1.append((int(8*(i)+k+1))*2.4082+42.288) ## axes in keV for PROTONS
            #ch1.append(int(8*i+k+1)) ## Axes in channel
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
            ch2.append((int(8*(i)+k+1))*2.3681+94.322) ## axes in keV for ALFAS
            #ch2.append((int(8*(i)+k+1))*2.4082+42.288) ## axes in keV for PROTONS
            #ch2.append(int(8*i+k+1)) ## Axes in channel
            y2.append(float(aux[i][k]))
    
    fig, ax = plt.subplots()
    ax.plot(ch1,y1,'.', color ='xkcd:blue', label=(str(File1)))
    ax.plot(ch2,y2,'+', color ='xkcd:red', label=(str(File2)))
    #ax.semilogy(ch1,y1,'.', color ='xkcd:blue', label=(str(File1)))
    #ax.semilogy(ch2,y2,'+', color ='xkcd:red', label=(str(File2)))
    legend = ax.legend(loc="upper left",ncol=1, shadow=False,fancybox=True,framealpha = 0.0,fontsize=20)
    legend.get_frame().set_facecolor('#DAEBF2')
    tick_params(axis='both', which='major', labelsize=22)
    xlabel('Energy (keV)',fontsize=22)
    #xlabel('Channel',fontsize=22)
    ylabel('Yield', fontsize=22)
    grid()
    show()
#############################################
#############################################

###                 Plots                     ###

###############   PROTOES   ###############
"""
VdG_Plot('0123/RBS1run01.dat', 'Calib Ta-V-Nb') # Calibration V-Ta-Nb
VdG_Plot('0123/RBS1run02.dat', 'Calib Ta-V-Nb') # Calibration V-Ta-Nb    

VdG_Plot('0123/RBS1run03.dat', 'target 4 - 20 mm') # Target 4 - no cleaning
VdG_Plot('0123/RBS1run04.dat', 'target 4 - 22 mm') # Target 4 - no cleaning

VdG_Plot('0123/RBS1run05.dat', 'target 5 - 33 mm') # Target 5 - 1 dip
VdG_Plot('0123/RBS1run06.dat', 'target 5 - 35 mm') # Target 5 - 1 dip

VdG_Plot('0123/RBS1run07.dat', 'target 6 - 44 mm') # Target 6 - 2 dips
VdG_Plot('0123/RBS1run08.dat', 'target 6 - 46 mm') # Target 6 - 2 dips
"""

VdG_Plot('0123/RBS1run09.dat', 'target 7 - 56 mm') # Target 7 - 3 dips
VdG_Plot('0123/RBS1run10.dat', 'target 7 - 58 mm') # Target 7 - 3 dips

VdG_Plot('0123/RBS1run11.dat', 'target 1 - 15 mm') # Target 1 
VdG_Plot('0123/RBS1run12.dat', 'target 1 - 20 mm') # Target 1 
VdG_Plot('0123/RBS1run13.dat', 'target 1 - 20 mm') # Target 1 

VdG_Plot('0123/RBS1run14.dat', 'target 2 - 55 mm') # Target 2
VdG_Plot('0123/RBS1run15.dat', 'target 2 - 60 mm') # Target 2 

VdG_Plot('0123/RBS1run16.dat', 'target E2 - 15 mm') # Target E2 
VdG_Plot('0123/RBS1run17.dat', 'target E2 - 20 mm') # Target E2
VdG_Plot('0123/RBS1run18.dat', 'target E2 - 20 mm - 180º') # Target E2 - 180º

VdG_Plot('0123/RBS1run19.dat', 'Formvar - 44 mm') # Target Formvar
VdG_Plot('0123/RBS1run20.dat', 'Formvar - 46 mm') # Target Formvar 










