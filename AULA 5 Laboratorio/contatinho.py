def criar(nome, telefone= "", email="", instagram=""):
    contato = [nome, telefone, email, instagram]
    telefone = [contato[1]]
    contato_n = [contato[0], telefone[:], contato[2], contato[3]]
    return contato_n
    
def atualizar(contato_n, i, info):
    if i >= 0 and i <= 3:
        if i == 1:
            if info in contato_n[i]:
                return contato_n
            else:
                contato_n[i] = contato_n[i] + [info]
        else:
            contato_n[i] = info
            return contato_n
    else:
        return contato_n
