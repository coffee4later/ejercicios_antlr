from antlr4 import *
from ExprLexer import ExprLexer
import sys 

# Leer archivos
# input_stream = FileStream(sys.argv[1])
# lexer = ExprLexer(input_stream)

# Por terminal
lexer = ExprLexer(InputStream(input("> ")))


tokens = CommonTokenStream(lexer)
tokens.fill()

print(tokens)

for token in tokens.tokens:
    print("texto: ", token.text)
    print("Linea: ", token.line)
    print("columna: ", token.column)
    print("nombre:", lexer.symbolicNames[token.type])
    print("tipo: ", token.type)
    print("----------------------------------------------")