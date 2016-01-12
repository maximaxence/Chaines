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

def hasSeries(password):
    pwd = list(password) 
    i=0
    ok = False

    while i<len(pwd)-2:
        if ord(pwd[i]) == ord(pwd[i+1]-1) == ord(pwd[i+2]-2):
            ok = True
        i = i+1

    return ok

def hasNoBadChar(password):
    pwd = list(password)
    i=0
    ok = True

    while i<len(pwd):
        if pwd[i] == 'i' || pwd[i] == 'o' || pwd[i] == 'l':
            ok = False
        i = i+1

    return ok

def hasTwoPairs(password):
    pwd = list(password)
    i=0
    j=0
    nbPair = 0
    tmp =''

    while i<len(pwd):
        while j<len(pwd):
            if pwd[j] == pwd[i] && pwd[j] != tmp:
                nbPair = nbPair +1
                tmp = pwd[j]
            j = j+1
        i = i+1

    if nbPair > 1:
        return True

    return False
            
    


# Grâce à ce fragment de code, si vous exécutez ce fichier, les tests doctests seront exécutés également. 
# Si vous ne voulez plus que les tests s'exécutent, commentez les deux lignes ci-dessous. 
# Si vous préférez lancer vos tests à la main, commentez également les lignes, et utilisez "python -m doctest pass.py" en console. 
if __name__ == "__main__":
    import doctest
    doctest.testmod()
