def generate_strings(cfg, k):
    def expand(symbol, current_length):
        # If the symbol is a terminal, return it as is
        if symbol not in cfg:
            return [symbol] if current_length < k else []

        # Explore all production rules for the current non-terminal symbol
        result = []
        for production in cfg[symbol]:
            if current_length + len(production) - 1 < k:
                # Generate all combinations for the current production
                combinations = ['']
                for prod_symbol in production:
                    new_combinations = []
                    for string in combinations:
                        for expansion in expand(prod_symbol, current_length + len(string)):
                            new_combinations.append(string + expansion)
                    combinations = new_combinations
                result.extend(combinations)
        return result

    # Start the expansion from the start symbol
    start_symbol = list(cfg.keys())[0]  # Assuming the first key is the start symbol
    return expand(start_symbol, 0)

def convert_grammar(input_grammar):
    grammar = {}
    lines = input_grammar.strip().split('\n')

    for line in lines:
        # Split the line into the non-terminal and its productions
        non_terminal, productions = line.split('::=')
        non_terminal = non_terminal.strip()

        # Process each production, removing extra spaces and quotes
        productions = productions.strip().split('|')
        productions = [prod.strip().replace('"', '') for prod in productions]

        grammar[non_terminal] = productions

    return grammar

def stringsofLenk(input_grammar, k):
    grammar = convert_grammar(input_grammar)
    lstStrings = generate_strings(grammar, k)
    Stringdict = {}
    for i in lstStrings:
        Stringdict[i] = 0
    return Stringdict

# f = open('grammars/total.gbnf')
# s = f.read()
# f.close()
# print(stringsofLenk(s, 3))


# input_grammar_text = """
# root    ::= S
# S       ::= X | "1"S
# X       ::= "0"
# """

# grammar = convert_grammar(input_grammar_text)
# print(grammar)

# cfg_example = {
#     'S': ['AB', 'BC'],
#     'A': ['a', ''],
#     'B': ['b', ''],
#     'C': ['c']
# }

# binary = {
#     'S' : ['1S', '0S', 'T'],
#     'T' : ['0', '1']
# }

# partial1 = {
#    'S' : ['1S', 'T'],
#     'T' : ['0']
# }

# print(generate_strings(binary,3))

# print(generate_strings(grammar, 4))