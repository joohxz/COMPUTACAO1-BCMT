def PosNegZero(x):
    if x > 0:
        return str(x) + ' e positivo'
    elif x == 0:
        return str(x) + ' e zero'
    else:
        return str(x) + ' e negativo'
    