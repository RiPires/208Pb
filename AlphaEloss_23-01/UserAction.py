#RiP
from PlotData import*
from Calibration import*
from PlotSpectrum import*


###   Plot DATA   ###
#PlotData('23-01/Ra226-Calib.mca')
#PlotData('23-01/Ra226-Calib2.mca')
#PlotData('23-01/Ra226-Target1.mca')
#PlotData('23-01/Ra226-Target2.mca')
#PlotData('23-01/Ra226-E2.mca')
#####################


###   CALIBRATION   ###
##   Input for energy calibration !! 20 Dez. !! in MeV   ##

#Energies = [7.68682, 6.00230, 5.48952, 5.30438, 4.78434]
#Channels = [1729., 1349., 1234., 1192., 1076.]
#Sigmas = [2.549235046, 2.799612686, 1.95119738, 2.024096602, 2.15619203]

#print('Calibration 23 Jan.:')
#Calibracao(Energies, Channels, Sigmas)
###########################################################
#######################


###   Plot simulated SPECTRUM   ###

#PlotBoth('23-01/Ra226-Calib2.mca', 'Calib2.csv')
PlotBoth('23-01/Ra226-Target1.mca', '1750nm.csv')
PlotBoth('23-01/Ra226-Target2.mca', '1650nm.csv')

###   Energies lists for stop. power tables   ###
#################################################