import sys
from antlr4 import *
from JurjenLangLexer import JurjenLangLexer
from JurjenLangParser import JurjenLangParser
 
def main(argv):
    input_stream = FileStream(argv[1])
    lexer = JurjenLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = JurjenLangParser(stream)
    tree = parser.startRule()
 
if __name__ == '__main__':
    main(sys.argv)