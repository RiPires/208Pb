###   PrintLists definition   ###
def PrintLists(ini, fin, step):

    """
    Inputs
    
    ini: initial value
    fin: final value
    step: increment

    Outputs

    writes desired list, each number line by line, to file "Energies.txt", by default
    """
    
    ini = float(ini)
    fin = float(fin)
    step = float(step)
    
    file = open('Energies.txt', 'w')

    for i in range(int(1/step*ini), int(1/step*fin+1), int(1/step*step)):
        file.write("{:.5f}".format(i*step) + '\n')
    file.close()
###   ********** *********   ###


###   Inputs for printing list   ###
Initial = input(str('Initial value = \t'))
Final = input(str('Final value = \t\t'))
Increment = input(str('Increment = \t\t'))

PrintLists(Initial, Final, Increment)

###   Checks for more lists .......


###   Let's change this document   ###
