def avioes(competidores, p_compr, p_compet):
    papeis_usados = competidores * p_compet
    if papeis_usados <= p_compr:
        return 'Suficiente'
    else:
        return 'Insuficiente'
