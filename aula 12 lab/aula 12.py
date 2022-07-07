def bolos(farinha, ovos, azeite):
    #Função que calcula quantos bolos conseguem ser feitos de acordo com os parâmetros dados
    farinha_t = farinha + 0
    ovoss = ovos + 0
    azeites = azeite+ 0
    bolo = 0
    while farinha_t >= 2 and ovoss >= 3 and azeites >= 5:
        farinha_t -= 2
        ovoss -= 3
        azeites -= 5
        bolo += 1
    return bolo

def pares():
    #Função que conta quantos números pares existem até tal número dado
    num = int(input('Escolha um número para verificar quantos números pares tem até ele:'))
    contagem = 0
    for (i) in range(0, num):
        if i % 2 == 0:
            contagem = contagem + 1
    return contagem

def login_senha():
    #A função cria um cadastro de login para o usuário e a senha não pode ser igual que o login
    login = str(input('Digite seu login:'))
    senha = str(input('Digite sua senha:'))
    dicionario = {}
    while login == senha:
        print('Não é possível criar a conta, por favor escolha um senha diferente de seu login')
        senha = str(input('Digite sua senha:'))

    dicionario[login] = senha
    condicao = str(input('Deseja verificar o banco de dados? (sim) ou (não):'))
    if condicao == 'sim':
        print('Conta criada com sucesso!',dicionario)
    else:
        print('Conta criada com sucesso!')

def impar():
    #Função que conta quantos números ímpares existem até tal número dado
    num = int(input('Escolha um número para verificar quantos números impares tem até ele:'))
    contagem = 0
    for (i) in range(0, num):
        if i % 2 != 0:
            contagem = contagem + 1
    return contagem
