#coding:utf8

from cmath import sqrt
from matplotlib.pylab import *
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


def Calibracao(E, Ch, dCh):
   
    sx=0.0 #Declaração de variáveis para simplificar os somatórios 
    sy=0.0 #que são precisos para calcular os paremetros da reta
    sxy=0.0
    sxx=0.0
    syy=0.0
    sinv=0.0
#   delta=0.0

    for i in range(0,len(Ch)): #De acordo com as listas criadas, calcula os somatórios
                                    #que usamos de seguida
        sx+=E[i]/((dCh[i])**2)
        sy+=Ch[i]/((dCh[i])**2)
        sxy+=(E[i]*Ch[i])/((dCh[i])**2)
        sxx+=((E[i])**2)/((dCh[i])**2)
        syy+=((Ch[i])**2)/((dCh[i])**2)
        sinv+= 1/((dCh[i])**2)
            
    delta = sinv*sxx - (sx*sx)

    m=(sinv*sxy-sx*sy)/(delta)    #Calcula o declive
    b= (sxx*sy-sx*sxy)/(delta)    #Calcula a ordenada na origem
    sigma_m = (sinv/delta)**(0.5) #Calcula incerteza associada ao declive
    sigma_b = (sxx/delta)**(0.5)  #Calcula incerteza associada à ordenada na origem   

    print('E [MeV] = (', "{:.6f}".format(1/m), '+-',"{:.6f}".format(
        sigma_m/m**2),') x Channel + (',"{:.6f}".format(b/m), '+-', "{:.6f}".format(
            ((sigma_b/m)**2+(b*sigma_m/m**2)**2)**0.5), ')')
    print()

    X = np.linspace( min(E), max(E))
    Y = m*X+b
 
    fig, ax = plt.subplots()
    ax.errorbar(E,Ch,dCh,None,'.', color ='xkcd:dark sky blue', label='alphas $^{226}$Ra')
    ax.plot(X,Y,color='xkcd:dark blue',label='Linear fit')
    legend = ax.legend(loc="upper left",ncol=1, shadow=True,fancybox=True,framealpha = 1.0,fontsize=20)
    legend.get_frame().set_facecolor('#DAEBF2')
    tick_params(axis='both', which='major', labelsize=22)
    xlabel('Energy [keV]',fontsize=22)
    ylabel('Channel', fontsize=22)
    grid()
    show()
    
    return'-------------------------'


def Calib_Wout_Uncer(BackEnergy, SurfaceChannel):

    slope, intercept, r_value, p_value, std_err = stats.linregress(SurfaceChannel, BackEnergy)  
    print('E [MeV] = ',"{:.6f}".format(slope),' * Ch +',"{:.6f}".format(intercept))
    print()
    #print('############################# \n')

    X = np.linspace(min(SurfaceChannel), max(SurfaceChannel))
    Y = slope*X+intercept
    
    fig, ax = plt.subplots()
    ax.plot(SurfaceChannel,BackEnergy,'.', color ='xkcd:dark sky blue',label = 'Resolution points')
    ax.plot(X,Y,color='xkcd:dark blue',label='Linear fit')
    legend = ax.legend(loc="upper center",ncol=1, shadow=True,fancybox=True,framealpha = 1.0,fontsize=20)
    legend.get_frame().set_facecolor('#DAEBF2')
    tick_params(axis='both', which='major', labelsize=22)
    xlabel('1/$\sqrt{E}$',fontsize=22)
    ylabel('R = $\sigma/{E}$', fontsize=22)
    grid()
    show()

    return'-------------------------'



##   Input for energy calibration   in MeV   ##
Energies = [1563.72,
1738.61,
1851.42,
1917.12,
1957.01
]

Channels = [643.,
712.,
761.,
792.,
808.
]

Sigmas = [1.,
1.,
1.,
1.,
1.
]

print('Calibração w/out/ Uncertainties:')
Calib_Wout_Uncer(Energies, Channels)

print('Calibração:')
Calibracao(Energies, Channels, Sigmas)