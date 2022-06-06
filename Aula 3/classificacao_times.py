def classificacao(cv,ce,cs,fv,fe,fs):
    cormengo_p = (cv * 3) + (ce * 1)
    flaminthians_p = (cv * 3) + (ce * 1)
    if cormengo_p > flaminthians_p:
        return 'Cormengo'
    if flaminthians_p > cormengo_p:
        return 'Flaminthians'
    elif flaminthians_p == cormengo_p:
        if cs > fs:
            return 'Cormengo'
        elif fs >  cs:
            return 'Flaminthians'
        elif cs == fs:
            return 'Empate'