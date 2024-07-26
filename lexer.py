import ply.lex as lex

# The tokens that we will accept
tokens = (
    'UPPERCASE',
    'LOWERCASE',
    'DIGIT',
    'SPECIAL',
)

# Regexes for the tokens
t_UPPERCASE = r'[A-Z]' # All capital letters
t_LOWERCASE = r'[a-z]' # All lowercase letters
t_DIGIT = r'\d' # All digits
t_SPECIAL = r'[\!\@\#\$\%\^\&\*\(\)\_\+\=\[\]\{\}\;\:\,\.\<\>\?\/\\\|]' # All special characters (almost all of them)

# Ignore spaces
t_ignore = ' \t\n'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()
