#coding:utf8

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

    m=(sinv*sxy-sx*sy)/(delta) #Calcula o declive
    b= (sxx*sy-sx*sxy)/(delta) #Calcula a ordenada na origem
    sigma_m = (sinv/delta)**(0.5)#Calcula incerteza associada ao declive
    sigma_b = (sxx/delta)**(0.5) #Calcula incerteza associada à ordenada na origem   

    print('E (MeV) = (', "{:.6f}".format(1/m), '+-',"{:.6f}".format(
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


def Resolucao(R, sqrtE):

    slope, intercept, r_value, p_value, std_err = stats.linregress(sqrtE, R)  
    #print(' slope=',"{:.4f}".format(slope),'\n',
    #      'intercept=',"{:.4f}".format(intercept),'\n',
    #      'R² = ', "{:.5f}".format(r_value**2),'\n',
    #      'std_Err = ',"{:.4f}".format(std_err),'\n')
    print('R = ',"{:.6f}".format(slope),' * 1/np.sqrt(E) +',"{:.6f}".format(intercept))
    print()
    #print('############################# \n')

    X = np.linspace(min(sqrtE), max(sqrtE))
    Y = slope*X+intercept
    
    fig, ax = plt.subplots()
    ax.plot(sqrtE,R,'.', color ='xkcd:dark sky blue',label = 'Resolution points')
    ax.plot(X,Y,color='xkcd:dark blue',label='Linear fit')
    legend = ax.legend(loc="upper center",ncol=1, shadow=True,fancybox=True,framealpha = 1.0,fontsize=20)
    legend.get_frame().set_facecolor('#DAEBF2')
    tick_params(axis='both', which='major', labelsize=22)
    xlabel('1/$\sqrt{E}$',fontsize=22)
    ylabel('R = $\sigma/{E}$', fontsize=22)
    grid()
    show()

    return'-------------------------'


def Resolucao_C_erros(R, sqrtE, dR):

    sx=0.0 #Declaração de variáveis para simplificar os somatórios 
    sy=0.0 #que são precisos para calcular os paremetros da reta
    sxy=0.0
    sxx=0.0
    syy=0.0
    sinv=0.0
    #   delta=0.0

    for i in range(0,len(R)): #De acordo com as listas criadas, calcula os somatórios
                                    #que usamos de seguida
        sx+=sqrtE[i]/((dR[i])**2)
        sy+=R[i]/((dR[i])**2)
        sxy+=(sqrtE[i]*R[i])/((dR[i])**2)
        sxx+=((sqrtE[i])**2)/((dR[i])**2)
        syy+=((R[i])**2)/((dR[i])**2)
        sinv+= 1/((dR[i])**2)
            
    delta = sinv*sxx - (sx*sx)

    m=(sinv*sxy-sx*sy)/(delta) #Calcula o declive
    b= (sxx*sy-sx*sxy)/(delta) #Calcula a ordenada na origem
    sigma_m = (sinv/delta)**(0.5)#Calcula incerteza associada ao declive
    sigma_b = (sxx/delta)**(0.5) #Calcula incerteza associada à ordenada na origem   

    print('R = (', "{:.6f}".format(1/m), '+-',"{:.6f}".format(
        sigma_m/m**2),') x 1/sqrt(E) + (',"{:.6f}".format(b/m), '+-', "{:.6f}".format(
            ((sigma_b/m)**2+(b*sigma_m/m**2)**2)**0.5), ')')
    print()

    X = np.linspace( min(sqrtE), max(sqrtE))
    Y = m*X+b

    fig, ax = plt.subplots()
    ax.errorbar(sqrtE,R,dR,None,'.', color ='xkcd:dark sky blue', label='alphas $^{226}$Ra')
    ax.plot(X,Y,color='xkcd:dark blue',label='Linear fit')
    legend = ax.legend(loc="upper left",ncol=1, shadow=True,fancybox=True,framealpha = 1.0,fontsize=20)
    legend.get_frame().set_facecolor('#DAEBF2')
    tick_params(axis='both', which='major', labelsize=22)
    xlabel('Energy [keV]',fontsize=22)
    ylabel('Channel', fontsize=22)
    grid()
    show()

    return'-------------------------'
###   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!   ###

##   Input for energy calibration !! 20 Dez. !! in MeV   ##

Energies = [7.68682, 6.00230, 5.48952, 5.30438, 4.78434]
Channels = [1719., 1343., 1227., 1186., 1070.]
Sigmas = [2.85510, 2.60492, 2.25344, 2.47031, 2.35025]

print('Calibration 20 Dez.:')
Calibracao(Energies, Channels, Sigmas)
###########################################################

##   Input for energy calibration !! 27 Dez. !! in MeV   ##

Energies = [7.68682, 6.00230, 5.48952, 5.30438, 4.78434]
Channels = [1712., 1337., 1223., 1181., 1066.]
Sigmas = [2.79761, 1.95953, 1.99854, 2.28614, 2.20823]

print('Calibration 27 Dez.:')
Calibracao(Energies, Channels, Sigmas)
###########################################################

##   Input for energy calibration !! 29 Dez. !! in MeV   ##

Energies = [7.68682, 6.00230, 5.48952, 5.30438, 4.78434]
Channels = [1719., 1343., 1229., 1187., 1071.]
Sigmas = [3.11420, 2.94006, 2.14722, 2.00866, 2.06549]

print('Calibration 29 Dez.:')
Calibracao(Energies, Channels, Sigmas)
###########################################################