# coding: utf-8 
def getNext(password):
    """
    Série de tests exprimés en doctest
    >>> getNext('a')
    'b'
    >>> getNext('az')
    'ba'
    >>> getNext('bc')
    'bd'
    """
    if password == '':
        raise chaineVide('le mdp est vide')
    pwd = list(password)  #1 On récupère chaque caractère de la chaine du mot de passe. On stocke tous les caractères dans pwd.
    found = False
    endOfLife = True
    i=len(pwd)-1
    

    while not found:
        if pwd[i] < 'z':
           pwd[i] = chr(ord(pwd[i])+1)  #2 Si le caractère est inférieur à z, alors on ajoute 1 au code ASCII récupéré grâce à la fonction ord() de ce caractère, et on écrase la nouvelle valeur du caractère 
           found = True
           endOfLife = False
        else:
           pwd[i] = 'a'
           i = i-1

    if endOfLife:
        raise endofLifeException('Fin de vie du mdp')
    
    return ''.join(pwd) #3 On retourne le nouveau mot de passe sous forme de chaîne de caractères



# Grâce à ce fragment de code, si vous exécutez ce fichier, les tests doctests seront exécutés également. 
# Si vous ne voulez plus que les tests s'exécutent, commentez les deux lignes ci-dessous. 
# Si vous préférez lancer vos tests à la main, commentez également les lignes, et utilisez "python -m doctest pass.py" en console. 
if __name__ == "__main__":
    import doctest
    doctest.testmod()
