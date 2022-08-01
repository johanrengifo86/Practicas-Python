def compruebaMail(mailUsuario):
    """ 
    la función compruebaMail evalúa un mail
    recibido en busca de la @. Si tiene una @
    es correcto, si tiene más de una @ es incorrecto
    si la @ está al final es incorrecto

    >>> compruebaMail('johan@cursos.es')
    True

    >>> compruebaMail('johancursos.es@')
    False

    >>> compruebaMail('johancursos.es')
    False

    >>> compruebaMail('johan@cursos.es@')
    False
    """

    arroba = mailUsuario.count('@')

    if (arroba !=1 or mailUsuario.rfind('@')==(len(mailUsuario)-1) or mailUsuario.find('@')==0):
        return False
    else:
        return True

import doctest
doctest.testmod()