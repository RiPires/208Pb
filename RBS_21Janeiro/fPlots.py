#RiP
from matplotlib.pylab import *
import matplotlib.pyplot as plt


from VdG2Lists import *
from Ch2Energy import *

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
    Channel, Yield = vdg2lists(File)

    ## x axes with energy calibration
    """
    for ch in Channel:
        ch = ((8*int(ch)+k+1)*2.3681+94.322)"""

    fig, ax = plt.subplots()
    ax.plot(Channel,Yield,'.', color ='xkcd:black', label=(str(dataLabel)))
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
        Plot
    """
    Channel1, Yield1 = vdg2lists(File1)
    Channel2, Yield2 = vdg2lists(File2)

    #Energy1 = ch2energy(Channel1)
    #Energy2 = ch2energy(Channel2)

    fig, ax = plt.subplots()
    ax.plot(Channel1,Yield1,'.', color ='xkcd:blue', label=(str(File1)))
    ax.plot(Channel2,Yield2,'+', color ='xkcd:red', label=(str(File2)))
    #ax.semilogy(Channel1,Yield1,'.', color ='xkcd:blue', label=(str(File1)))
    #ax.semilogy(Channel2,Yield2,'+', color ='xkcd:red', label=(str(File2)))
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


########################################################
###   Plot four RBS .dat files funntion definition   ###
########################################################
def VdG_Plot4(File1, File2, File3, File4):
    """
    Converts four .dat files from VdG RBS into yield and channel lists
    and plots 
    INPUTS:
        "FILENAME1.dat",'FILENAME2.dat', 'FILENAME3.DAT', 'FILENAME4.DAT'
    OUTPUTS:
        Plot
    """
    Channel1, Yield1 = vdg2lists(File1)
    Channel2, Yield2 = vdg2lists(File2)
    Channel3, Yield3 = vdg2lists(File3)
    Channel4, Yield4 = vdg2lists(File4)

    ## Calib. parameters:
    m = 2.

    Energy1 = ch2energy(Channel1)
    Energy2 = ch2energy(Channel2)
    Energy3 = ch2energy(Channel3)
    Energy4 = ch2energy(Channel4)
    
    fig, ax = plt.subplots()
    ax.plot(Energy1,Yield1,'.', color ='xkcd:blue', label=(str(File1)))
    ax.plot(Energy2,Yield2,'+', color ='xkcd:red', label=(str(File2)))
    ax.plot(Energy3,Yield3,'*', color ='xkcd:green', label=(str(File3)))
    ax.plot(Energy4,Yield4,'^', color ='xkcd:black', label=(str(File4)))

    #ax.semilogy(Channel1,Yield1,'.', color ='xkcd:blue', label=(str(File1)))
    #ax.semilogy(Channel2,Yield2,'+', color ='xkcd:red', label=(str(File2)))
    #ax.semilogy(Channel3,Yield3,'*', color ='xkcd:green', label=(str(File3)))
    #ax.semilogy(Channel4,Yield4,'^', color ='xkcd:black', label=(str(File4)))

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