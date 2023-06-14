def glc_para_fng(producoes):
    fng_producoes = []
    variaveis = set(producoes.keys())

    for variavel, producao in producoes.items():
        for p in producao:
            if len(p) <= 2:
                fng_producoes.append((variavel, p))
            else:
                novas_variaveis = []
                for i in range(len(p) - 1):
                    nova_variavel = obter_nova_variavel(variaveis)
                    variaveis.add(nova_variavel)
                    novas_variaveis.append(nova_variavel)
                    fng_producoes.append((variavel, p[i] + nova_variavel))
                fng_producoes.append((novas_variaveis[-1], p[-1]))
                for i in range(len(novas_variaveis) - 1):
                    fng_producoes.append((novas_variaveis[i], p[i + 1] + novas_variaveis[i + 1]))


    return fng_producoes

def obter_nova_variavel(variaveis):
    for letra in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        nova_variavel = letra
        if nova_variavel not in variaveis:
            return nova_variavel

# Exemplo de uso
producoes = {
    'S': ['aAd', 'A'],
    'A': ['Bc'],
    'B': ['Ac','a']
}

fng_producoes = glc_para_fng(producoes)

# Imprime as produções na FNG
for variavel, producao in fng_producoes:
    print(variavel + ' -> ' + producao)



