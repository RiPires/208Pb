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
            ch1.append((int(8*(i)+k+1))*2.3681+94.322) ## axes in keV 
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

#######################################################
###   Plot four RBS .dat files funntion definition   ###
#######################################################
def VdG_Plot4(File1, File2, File3, File4):
    """
    Converts four .dat files from VdG RBS into yield and channel lists
    and plots both
    INPUTS:
        "FILENAME1.dat",'FILENAME2.dat','FILENAME3.dat','FILENAME4.dat'
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
            ch1.append((int(8*(i)+k+1))*2.3671+46.376) ## axes in keV for ALFAS
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
            ch2.append((int(8*(i)+k+1))*2.3671+46.376) ## axes in keV for ALFAS
            #ch2.append((int(8*(i)+k+1))*2.4082+42.288) ## axes in keV for PROTONS
            #ch2.append(int(8*i+k+1)) ## Axes in channel
            y2.append(float(aux[i][k]))


    ## Creates channel yield lists for File3 and
    # converts channel to energy
    with open(File3, 'r') as file:
        reader = csv.reader(file, delimiter="\n", skipinitialspace=True)
        data = list(reader)
    ch3 = []
    y3 = []
    aux = []
    for i in range(128):
        aux.append(data[i][0].split())
    #print(aux)
    for i in range(len(aux)):
        for k in range(8):
            ch3.append((int(8*(i)+k+1))*2.3671+46.376) ## axes in keV for ALFAS
            #ch2.append((int(8*(i)+k+1))*2.4082+42.288) ## axes in keV for PROTONS
            #ch2.append(int(8*i+k+1)) ## Axes in channel
            y3.append(float(aux[i][k]))

    
    ## Creates channel yield lists for File4 and
    # converts channel to energy
    with open(File4, 'r') as file:
        reader = csv.reader(file, delimiter="\n", skipinitialspace=True)
        data = list(reader)
    ch4 = []
    y4 = []
    aux = []
    for i in range(128):
        aux.append(data[i][0].split())
    #print(aux)
    for i in range(len(aux)):
        for k in range(8):
            ch4.append((int(8*(i)+k+1))*2.3671+46.376) ## axes in keV for ALFAS
            #ch2.append((int(8*(i)+k+1))*2.4082+42.288) ## axes in keV for PROTONS
            #ch2.append(int(8*i+k+1)) ## Axes in channel
            y4.append(float(aux[i][k]))
    
    fig, ax = plt.subplots()
    #ax.plot(ch1,y1,'.', color ='xkcd:blue', label=(str(File1)))
    #ax.plot(ch2,y2,'+', color ='xkcd:red', label=(str(File2)))
    #ax.plot(ch3,y3,'*', color ='xkcd:green', label=(str(File3)))
    #ax.plot(ch4,y4,'^', color ='xkcd:orange', label=(str(File4)))

    ax.semilogy(ch1,y1,'.', color ='xkcd:blue', label=(str('No cleaning')))
    ax.semilogy(ch2,y2,'+', color ='xkcd:red', label=(str('1st wash')))
    ax.semilogy(ch3,y3,'*', color ='xkcd:green', label=(str('2nd wash')))
    ax.semilogy(ch4,y4,'^', color ='xkcd:black', label=(str('3rd wash')))

    legend = ax.legend(loc="bottom center",ncol=1, shadow=False,fancybox=True,framealpha = 0.0,fontsize=20)
    legend.get_frame().set_facecolor('#DAEBF2')
    tick_params(axis='both', which='major', labelsize=22)
    xlabel('Energy (keV)',fontsize=22)
    #xlabel('Channel',fontsize=22)
    ylabel('Yield', fontsize=22)
    show()
#############################################
#############################################

###                Plots                ###
###############   PROTOES   ###############
###              165º RBS1              ###
""" VdG_Plot('0323/RBS1run01.dat', 'Calib Ta-V-Nb - 5 mm') # Calibration V-Ta-Nb

VdG_Plot_logy('0323/RBS1run2.dat', 'Target 1 - 25 mm') # Target 1 - 25 mm
VdG_Plot_logy('0323/RBS1run03.dat', 'Target 1 - 26 mm')
VdG_Plot_logy('0323/RBS1run4.dat', 'Target 1 - 28 mm') 
VdG_Plot_logy('0323/RBS1run5.dat', 'Target 1 - 30 mm') 
VdG_Plot_logy('0323/RBS1run6.dat', 'Target 1 - 32 mm') 
VdG_Plot_logy('0323/RBS1run7.dat', 'Target 1 - 34 mm') 
VdG_Plot_logy('0323/RBS1run8.dat', 'Target 1 - 36 mm') 

VdG_Plot_logy('0323/RBS1run9.dat', 'Target 3 - 14 mm') # Target 3
VdG_Plot_logy('0323/RBS1run10.dat', 'Target 3 - 20 mm')
VdG_Plot_logy('0323/RBS1run11.dat', 'Target 3 - 26 mm')

VdG_Plot_logy('0323/RBS1run12.dat', 'Target 6 - 52 mm') # Target 6
VdG_Plot_logy('0323/RBS1run13.dat', 'Target 6 - 58 mm')
VdG_Plot_logy('0323/RBS1run14.dat', 'Target 6 - 63 mm')

VdG_Plot_logy('0323/RBS1run15.dat', 'Target 7 - 63 mm') # Target 7
VdG_Plot_logy('0323/RBS1run16.dat', 'Target 7 - 58 mm')
VdG_Plot_logy('0323/RBS1run17.dat', 'Target 7 - 52 mm') """

VdG_Plot_logy('0323/RBS1run18.dat', 'Target 8 - 26 mm') # Target 8
VdG_Plot_logy('0323/RBS1run19.dat', 'Target 8 - 20 mm')
VdG_Plot_logy('0323/RBS1run20.dat', 'Target 8 - 14 mm')

###              140º RBS2              ###
""" VdG_Plot('0323/RBS2run01.dat', 'Calib Ta-V-Nb - 5 mm') # Calibration V-Ta-Nb

VdG_Plot_logy('0323/RBS2run2.dat', 'Target 1 - 25 mm') # Target 1 - 25 mm
VdG_Plot_logy('0323/RBS2run03.dat', 'Target 1 - 26 mm')
VdG_Plot_logy('0323/RBS2run4.dat', 'Target 1 - 28 mm') 
VdG_Plot_logy('0323/RBS2run5.dat', 'Target 1 - 30 mm') 
VdG_Plot_logy('0323/RBS2run6.dat', 'Target 1 - 32 mm') 
VdG_Plot_logy('0323/RBS2run7.dat', 'Target 1 - 34 mm') 
VdG_Plot_logy('0323/RBS2run8.dat', 'Target 1 - 36 mm') 

VdG_Plot_logy('0323/RBS2run9.dat', 'Target 3 - 14 mm') # Target 3
VdG_Plot_logy('0323/RBS2run10.dat', 'Target 3 - 20 mm')
VdG_Plot_logy('0323/RBS2run11.dat', 'Target 3 - 26 mm')

VdG_Plot_logy('0323/RBS2run12.dat', 'Target 6 - 52 mm') # Target 6
VdG_Plot_logy('0323/RBS2run13.dat', 'Target 6 - 58 mm')
VdG_Plot_logy('0323/RBS2run14.dat', 'Target 6 - 63 mm')

VdG_Plot_logy('0323/RBS2run15.dat', 'Target 7 - 63 mm') # Target 7
VdG_Plot_logy('0323/RBS2run16.dat', 'Target 7 - 58 mm')
VdG_Plot_logy('0323/RBS2run17.dat', 'Target 7 - 52 mm') """

VdG_Plot_logy('0323/RBS2run18.dat', 'Target 8 - 26 mm') # Target 8
VdG_Plot_logy('0323/RBS2run19.dat', 'Target 8 - 20 mm')
VdG_Plot_logy('0323/RBS2run20.dat', 'Target 8 - 14 mm')