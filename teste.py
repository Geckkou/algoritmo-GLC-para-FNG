def remove_empty_productions(productions):
    nullable = set()
    new_productions = []

    for production in productions:
        lhs, rhs = production.split(' → ')
        if rhs == 'λ':
            nullable.add(lhs)

    def generate_combinations(current_production, remaining_symbols):
        if len(remaining_symbols) == 0:
            new_productions.append(current_production)
        else:
            symbol = remaining_symbols[0]
            generate_combinations(current_production + symbol, remaining_symbols[1:])
            if symbol in nullable:
                generate_combinations(current_production, remaining_symbols[1:])

    for production in productions:
        lhs, rhs = production.split(' → ')
        generate_combinations('', rhs)

    return new_productions


def remove_unit_productions(productions):
    unit_productions = {}
    new_productions = []

    for production in productions:
        lhs, rhs = production.split(' → ')
        if len(rhs) == 1 and rhs.isupper():
            if lhs not in unit_productions:
                unit_productions[lhs] = []
            unit_productions[lhs].append(rhs)

    def expand_production(lhs, rhs):
        if rhs in unit_productions:
            for unit_rhs in unit_productions[rhs]:
                expand_production(lhs, unit_rhs)
        else:
            new_productions.append(lhs + ' → ' + rhs)

    for production in productions:
        lhs, rhs = production.split(' → ')
        if len(rhs) > 1 or not rhs.isupper():
            expand_production(lhs, rhs)

    return new_productions


def remove_unused_symbols(start_symbol, productions):
    reachable_symbols = {start_symbol}
    for production in productions:
        lhs, rhs = production.split(' → ')
        if all(symbol in reachable_symbols for symbol in rhs):
            reachable_symbols.add(lhs)

    new_productions = [production for production in productions if production.split(' → ')[0] in reachable_symbols
                       and all(symbol in reachable_symbols for symbol in production.split(' → ')[1])]

    return new_productions


def convert_to_binary_productions(productions):
    new_productions = []

    def split_production(lhs, rhs):
        if len(rhs) <= 2:
            new_productions.append(lhs + ' → ' + rhs)
        else:
            new_symbol = rhs[0] + rhs[1]
            new_productions.append(lhs + ' → ' + new_symbol)
            split_production(new_symbol, rhs[2:])

    for production in productions:
        lhs, rhs = production.split(' → ')
        split_production(lhs, rhs)

    return new_productions


def rename_nonterminals(productions):
    new_productions = []
    nonterminal_count = 0
    nonterminal_map = {}

    def rename_nonterminal(nonterminal):
        nonlocal nonterminal_count
        if nonterminal not in nonterminal_map:
            nonterminal_count += 1
            new_nonterminal = chr(65 + nonterminal_count)
            nonterminal_map[nonterminal] = new_nonterminal
        return nonterminal_map[nonterminal]

    for production in productions:
        lhs, rhs = production.split(' → ')
        new_lhs = rename_nonterminal(lhs)
        new_rhs = ''.join(rename_nonterminal(symbol) if symbol.isupper() else symbol for symbol in rhs)
        new_productions.append(new_lhs + ' → ' + new_rhs)

    return new_productions


def transform_to_greibach_form(start_symbol, productions):
    productions = remove_empty_productions(productions)
    productions = remove_unit_productions(productions)
    productions = remove_unused_symbols(start_symbol, productions)
    productions = convert_to_binary_productions(productions)
    productions = rename_nonterminals(productions)

    return productions


# Exemplo de uso
start_symbol = 'S'
productions = [
    'S → aAd | A',
    'A → Bc | λ',
    'B → Ac | a'
]

result = transform_to_greibach_form(start_symbol, productions)

# Imprimir as produções resultantes
for production in result:
    print(production)
