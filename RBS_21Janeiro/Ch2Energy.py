def ch2energy(Channel, m, b):
    """
    Converts channel into energy for calibration parameters m - slope and b - intercept

    INPUTS:
    Channel - can be a list

    OUTPUTS:
    Energy list
    """
    for ch in Channel:
        ch = ((8*int(ch)+k+1)*m+b)
    
    return Channel