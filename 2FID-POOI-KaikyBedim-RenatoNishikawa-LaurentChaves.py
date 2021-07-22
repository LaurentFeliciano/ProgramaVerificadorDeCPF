# Laurent Chaves Assis Feliciano
# Kaiky Bedim
# Renato Minoru Nishikawa
# 2°F Informática
# 25/05/2021
# POOI 2° Bimestre
# Alberson Wander

# --------------------------------------------------------------------------------------------------------------------------#

# Variáveis Percentuais e Estatísticas:

qnt_cpf_testados=0
qnt_cpf_validos=0
qnt_cpf_invalidos=0
porcent_invalidos=0
porcent_validos=0


# Variáveis Usuais durante o Código:

dicionario={}
lista = []
aux_verificador1 = (10, 9, 8, 7, 6, 5, 4, 3, 2)
aux_verificador2 = (11, 10, 9, 8, 7, 6, 5, 4, 3, 2)
soma = 0
aux = 0
tabela_cpf = []
CPF = ""


# Início do Código:

print(75*"-")
print("\033[30;45m*Programa em Linguagem Python para verificar a Condição de um CPF inserido*\033[m")
print(75*"-")
r = input("Deseja iniciar o programa de validação de CPF's?(Digite '\033[4;33msim\033[m' ou '\033[4;33mnão\033[m' ):")


# Verificação da resposta do usuário:

while r != 'sim' and r != 'não':
    r = input("\033[4;31mResposta inválida, tente novamente (sim ou não):\033[m ")


# Início do Teste de CPF:

while r == 'sim':
    dicionario['cpf'] = (input('\nDigite seu cpf: '))

    # Teste de dimensão do CPF:
    while len(dicionario['cpf']) != 11:
        dicionario['cpf'] = (input('\033[4;31mCPF com proporções inválidas, digite novamente:\033[m '))


# Verificador do 1° Dígito:

    # Passando os 9 primeiros dígitos para a tabela_cpf:

    for cont in range(0, 9, 1):
       tabela_cpf.append(dicionario['cpf'][cont])

    # Fazendo a multiplicação e a soma para gerar o Primeiro Dígito Verificador:

    for cont in range(0, 9, 1):
        aux = float(tabela_cpf[cont])
        soma = soma + aux * aux_verificador1[cont]

    # Divisão do número gerado anteriormente por 11 e definição do Primeiro Dígito:

    rest = soma % 11
    if rest < 2:
        pri_digito = 0
    else:
        pri_digito = 11 - rest

    # Verificador do 2º Dígito:

    # Zerando a variável soma e adicionando o pri_digito a tabela_cpf:
    soma = 0
    tabela_cpf.append(int(pri_digito))

    # Fazendo a multiplicação e a soma para gerar o Segundo Dígito Verificador:

    for cont in range(0,10,1):
        aux = float(tabela_cpf[cont])
        soma = soma + aux * aux_verificador2[cont]

    # Divisão do número gerado anteriormente por 11 e definição do Segundo Dígito:

    rest = soma % 11
    if rest < 2:
        seg_digito = 0
    else:
        seg_digito = 11 - rest
    tabela_cpf.append(int(seg_digito))

    # Gerando o CPF com o primeiro e segundo dígito na variável CPF:

    for cont in range (0,11,1):
        CPF = f'{CPF}{tabela_cpf[cont]}'

    # Determinação da validação do CPF:

    if dicionario['cpf'] == CPF:
        dicionario['Condição'] = "Válido"
        qnt_cpf_testados += 1
        qnt_cpf_validos += 1
    else:
        dicionario['Condição'] = "Inválido"
        qnt_cpf_testados+= 1
        qnt_cpf_invalidos += 1
    print(f'O CPF {dicionario["cpf"]} é \033[4;33m{dicionario["Condição"]}\033[m')

    # Realização de uma cópia do CPF e sua condição na lista "Lista" e exclusão dos dados armazenados no dicionário:

    lista.append(dicionario.copy())
    tabela_cpf.clear()
    CPF = ""
    soma = 0
    print(200 * '-')

    # Pergunta ao usuário se ele quer ou não continuar o programa:
    r=input("\033[35;40mDeseja continuar o programa de validação de CPF's?Digite 'sim' ou 'não':\033[m")
    while r != 'sim' and r != 'não':
        r = input("Resposta inválida, tente novamente (sim ou não): ")
print(200*'-')


# Atribuindo valor a porcent_validos e porcent_invalidos:

if qnt_cpf_validos != 0:
    porcent_validos = (qnt_cpf_validos/qnt_cpf_testados ) * 100
if qnt_cpf_invalidos != 0:
    porcent_invalidos = (qnt_cpf_invalidos/qnt_cpf_testados) * 100


# Porcentagens e estatísticas geradas ao decorrer do programa:

print(f"""- A Lista gerada com os CPF's foi: {lista}
- Quantos cpfs foram testados: {qnt_cpf_testados}
- Quantidade de CPFS VÁLIDOS: {qnt_cpf_validos}
- Quantidade de CPFS INVÁLIDOS: {qnt_cpf_invalidos}
- Porcentagem de cpfs válidos e inválidos em relação a quantidade total de testes realizados:
\033[4;42m|{porcent_validos}% Válidos|\033[m \033[4;41m|{porcent_invalidos}% Inválidos|\033[m """)