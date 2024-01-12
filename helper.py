import hashlib

USE_HASH = 256

def hashed(value: str) -> str:
    """ Permet d'encoder une chaine de caractère en utilisant le système de (hash)
    Args:
        value (str): la chaine a encodé
    Returns:
        str: la chaine encodée
    """
    # on encode la chaine en utf-8, pour accepter aussi les caractères accentuer (é, à, etc.)
    # puis on va hasher la chaine
    return hashlib.sha256(value.encode()).hexdigest()



def readline(message: str) -> str:
    """ Permet d'afficher un champs de saisi à l'utilisateur
    Args:
        message (str): le texte a affiché
    Returns:
        str: la valeur saisie
    """
    response = None
    while response is None or response == "":
        response = input(message)
        
    return response






