def glc_para_fng(producoes):
    fng_producoes = [] # Lista para armazenar as produções na FNG
    variaveis = set(producoes.keys()) # Conjunto de variáveis presentes nas produções

    # Itera sobre cada variável e suas produções na GLC
    for variavel, producao in producoes.items():
        for p in producao:
            if len(p) <= 2: # Verifica se a produção tem no máximo 2 símbolos
                fng_producoes.append((variavel, p))  # Se a produção tiver no máximo 2 símbolos, adiciona diretamente à FNG
            else:
                novas_variaveis = []  # Lista para armazenar as novas variáveis geradas
                # Gera novas variáveis para substituir os símbolos intermediários na produção
                for i in range(len(p) - 1):
                    nova_variavel = obter_nova_variavel(variaveis)
                    variaveis.add(nova_variavel)
                    novas_variaveis.append(nova_variavel)
                    fng_producoes.append((variavel, p[i] + nova_variavel))
                # Adiciona uma produção final para substituir os últimos símbolos da produção original
                fng_producoes.append((novas_variaveis[-1], p[-1]))
                # Gera as produções intermediárias entre as novas variáveis
                for i in range(len(novas_variaveis) - 1):
                    fng_producoes.append((novas_variaveis[i], p[i + 1] + novas_variaveis[i + 1]))


    return fng_producoes

def obter_nova_variavel(variaveis):
    # Função para obter uma nova variável não utilizada
    for letra in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        nova_variavel = letra
        if nova_variavel not in variaveis:
            return nova_variavel

# Regras de produção GLC
producoes = {
    'S': ['aAd', 'A'],
    'A': ['Bc'],
    'B': ['Ac','a']
}

fng_producoes = glc_para_fng(producoes)

# Imprime as produções na FNG
for variavel, producao in fng_producoes:
    print(variavel + ' -> ' + producao)