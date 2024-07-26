import ply.yacc as yacc
from lexer import tokens, lexer

# Parsing rules


# This rule parses the overall structure of the password
def p_password(p):
    """password : characters"""
    p[0] = p[1]
    # Check if the password meets the criteria for a strong password
    if (
        len(p[1]["all"]) >= 13
        and p[1]["uppercase"]
        and p[1]["lowercase"]
        and p[1]["digit"]
        and p[1]["special"]
    ):
        print("Strong password")
    else:
        print("Weak password")


# This rule parses the characters in the password
def p_characters(p):
    """characters : character characters
    | character"""
    if len(p) == 3:
        p[0] = p[2]
    else:
        p[0] = {
            "all": "",
            "uppercase": False,
            "lowercase": False,
            "digit": False,
            "special": False,
        }

    # Add the parsed character to the overall string
    p[0]["all"] += p[1]["char"]
    # Mark the type of character (uppercase, lowercase, digit, special)
    if p[1]["type"] == "UPPERCASE":
        p[0]["uppercase"] = True
    elif p[1]["type"] == "LOWERCASE":
        p[0]["lowercase"] = True
    elif p[1]["type"] == "DIGIT":
        p[0]["digit"] = True
    elif p[1]["type"] == "SPECIAL":
        p[0]["special"] = True


# This rule identifies an individual character and its type
def p_character(p):
    """character : UPPERCASE
    | LOWERCASE
    | DIGIT
    | SPECIAL"""
    p[0] = {"char": p[1], "type": p.slice[1].type}


# Error handling function
def p_error(p):
    print("Syntax error in input!")


# Construct the parser
parser = yacc.yacc()


# Function to check the password
def check_password(password):
    parser.parse(password, lexer=lexer)


if __name__ == "__main__":
    while True:
        password = input("Enter a password to check (enter 'exit' to quit): ")
        if password == "exit":
            break
        check_password(password)
