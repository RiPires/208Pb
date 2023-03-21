from fPlots import *

###   Plot 4 cleaning stages 
VdG_Plot4('0123/RBS1run04.dat','0123/RBS1run06.dat','0123/RBS1run08.dat', '0123/RBS1run10.dat')

### Plot formvar
VdG_Plot('0123/RBS1run20.dat', 'Formvar')
VdG_Plot3('0123/ERDrun20.dat', '0123/RBS1run20.dat', '0123/RBS2run20.dat')

### Plot E2 0º and 180º
VdG_PlotBoth('0123/RBS1run17.dat', 'Target E2 - 0º', '0123/RBS1run18.dat', 'Target E2 - 180º')

### Targets 1 and 2
VdG_PlotBoth('0123/RBS1run13.dat', 'Target 1', '0123/RBS1run15.dat', 'Target 2')

### Target 2 - all det
VdG_Plot3('0123/ERDrun15.dat', '0123/RBS1run15.dat', '0123/RBS2run15.dat')

