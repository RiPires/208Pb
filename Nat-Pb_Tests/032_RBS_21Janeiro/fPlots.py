#RiP
from matplotlib.pylab import *
import matplotlib.pyplot as plt


from VdG2Lists import *
from Ch2Energy import *
from SimNRA2Lists import *

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
    ## Calib. parameters:
    m = 2.3671
    b = 46.376
    Energy = ch2energy(Channel, m, b)


    fig, ax = plt.subplots()
    #ax.plot(Channel,Yield,'.', color ='xkcd:black', label=(str(dataLabel)))
    ax.semilogy(Energy,Yield,'+', color ='xkcd:black', label=(str(dataLabel)))
    legend = ax.legend(loc="best",ncol=2, shadow=False,fancybox=True,framealpha = 0.0,fontsize=20)
    legend.get_frame().set_facecolor('#DAEBF2')
    tick_params(axis='both', which='major', labelsize=22)
    xlabel('Energy (keV)',fontsize=22)
    #xlabel('Channel',fontsize=22)   
    ylabel('Yield', fontsize=22)
    show()
#############################################
#############################################

#######################################################
###   Plot two RBS .dat files funntion definition   ###
#######################################################
def VdG_PlotBoth(File1, label1, File2, label2):
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

    ## Calib. parameters:
    m = 2.3671
    b = 46.376

    Energy1 = ch2energy(Channel1, m, b)
    Energy2 = ch2energy(Channel2, m, b)

    fig, ax = plt.subplots()
    #ax.plot(Energy1,Yield1,'.', color ='xkcd:black', label=(str(label1)))
    #ax.plot(Energy2,Yield2,'+', color ='xkcd:red', label=(str(label2)))
    ax.semilogy(Energy1,Yield1,'*', color ='xkcd:black', label=(str(label1)))
    ax.semilogy(Energy2,Yield2,'+', color ='xkcd:red', label=(str(label2)))
    legend = ax.legend(loc="best",ncol=1, shadow=False,fancybox=True,framealpha = 0.0,fontsize=20)
    legend.get_frame().set_facecolor('#DAEBF2')
    tick_params(axis='both', which='major', labelsize=22)
    xlabel('Energy (keV)',fontsize=22)
    #xlabel('Channel',fontsize=22)
    ylabel('Yield', fontsize=22)
    show()
#############################################
#############################################


########################################################
###   Plot three RBS .dat files funntion definition   ###
########################################################
def VdG_Plot3(File1, File2, File3):
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

    ## Calib. parameters:
    m = 2.3671
    b = 46.376

    Energy1 = ch2energy(Channel1, m, b)
    Energy2 = ch2energy(Channel2, m, b)
    Energy3 = ch2energy(Channel3, m, b)

    fig, ax = plt.subplots()
    #ax.plot(Energy1,Yield1,'.', color ='xkcd:blue', label=(str(File1)))
    #ax.plot(Energy2,Yield2,'+', color ='xkcd:red', label=(str(File2)))
    #ax.plot(Energy3,Yield3,'*', color ='xkcd:green', label=(str(File3)))

    ax.semilogy(Energy1,Yield1,'.', color ='xkcd:black', label=(str('ERD')))
    ax.semilogy(Energy2,Yield2,'+', color ='xkcd:red', label=(str('RBS 1')))
    ax.semilogy(Energy3,Yield3,'*', color ='xkcd:blue', label=(str('RBS 2')))

    legend = ax.legend(loc="best",ncol=1, shadow=False,fancybox=True,framealpha = 0.0,fontsize=20)
    legend.get_frame().set_facecolor('#DAEBF2')
    tick_params(axis='both', which='major', labelsize=22)
    xlabel('Energy (keV)',fontsize=22)
    #xlabel('Channel',fontsize=22)
    ylabel('Yield', fontsize=22)
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
    m = 2.3671 #keV/Channel
    b = 46.376 #keV


    Energy1 = ch2energy(Channel1, m, b)
    Energy2 = ch2energy(Channel2, m, b)
    Energy3 = ch2energy(Channel3, m, b)
    Energy4 = ch2energy(Channel4, m, b)
    
    fig, ax = plt.subplots()
    #ax.plot(Energy1,Yield1,'.', color ='xkcd:blue', label=(str(File1)))
    #ax.plot(Energy2,Yield2,'+', color ='xkcd:red', label=(str(File2)))
    #ax.plot(Energy3,Yield3,'*', color ='xkcd:green', label=(str(File3)))
    #ax.plot(Energy4,Yield4,'^', color ='xkcd:black', label=(str(File4)))

    ax.semilogy(Energy1,Yield1,'.', color ='xkcd:blue', label=(str('No cleaning')))
    ax.semilogy(Energy2,Yield2,'+', color ='xkcd:red', label=(str('1st wash')))
    ax.semilogy(Energy3,Yield3,'*', color ='xkcd:green', label=(str('2nd wash')))
    ax.semilogy(Energy4,Yield4,'^', color ='xkcd:black', label=(str('3rd wash')))

    legend = ax.legend(loc="upper right",ncol=1, shadow=False,fancybox=True,framealpha = 0.0,fontsize=22)
    legend.get_frame().set_facecolor('#DAEBF2')
    tick_params(axis='both', which='major', labelsize=24)
    xlabel('Energy (keV)',fontsize=24)
    ylabel('Yield', fontsize=24)
    show()
#############################################
#############################################


def PlotRBSnSimNRA(FileRBS, FileSIM):
    """
    
    """

    ChannelRBS, YieldRBS = vdg2lists(FileRBS)
    ## Calib. parameters:
    m = 2.3671 #keV/Channel
    b = 46.376 #keV
    EnergyRBS = ch2energy(ChannelRBS, m, b)

    ChannelSim, YieldSim  = SimNRA2Lists(FileSIM)
    ## Calib. parameters:
    m = 2.3671 #keV/Channel
    b = 54. #keV
    EnergySim = ch2energy(ChannelSim, m, b)

    fig, ax = plt.subplots()
    ax.plot(EnergyRBS,YieldRBS,'.', color ='xkcd:blue', label=(str('RBS')))
    ax.plot(EnergySim,YieldSim,'+', color ='xkcd:red', label=(str('SimNRA')))

    legend = ax.legend(loc="upper right",ncol=1, shadow=False,fancybox=True,framealpha = 0.0,fontsize=22)
    legend.get_frame().set_facecolor('#DAEBF2')
    tick_params(axis='both', which='major', labelsize=24)
    xlabel('Energy (keV)',fontsize=24)
    ylabel('Yield', fontsize=24)
    show()