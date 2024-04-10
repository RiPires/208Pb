def ch2energy(Channel, m, b):
    """
    Converts channel into energy for calibration parameters m - slope and b - intercept

    INPUTS:
    Channel - can be a list

    OUTPUTS:
    Energy list
    """
    Energy = []
    for ch in Channel:
        energy = (int(ch)*m+b)
        Energy.append(energy)
    
    return Energy