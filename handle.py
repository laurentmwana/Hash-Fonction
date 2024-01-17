LENGHT_CHARACATER = 256
LENGHT_MODULO = 251
LENGHT_COMPARATOR_BINARY = 8

def hashed(string: str) -> tuple:
    
    """Permet de hasher une chaine
    Args:
        string (str): la chaine a hashé
    Returns:
        tuple: le résultat final (chaine hashée)
    """
    z = ''
    tab = 0
    lenght_string = len(string)
    for index in range(lenght_string):
        tab += (ord(string[index]) * (LENGHT_CHARACATER ** ((lenght_string - index) - 1)))
    tab = tab % LENGHT_MODULO
    
    binary = format(tab, 'b')
    
    lenght_binary = len(binary)
    
    if lenght_binary < LENGHT_COMPARATOR_BINARY:
        for index in range(LENGHT_COMPARATOR_BINARY - lenght_binary):
            z += '0'
    binary = z + binary
    
    return binary, format(tab, 'x')