import sys
from antlr4 import *
from JurjenLangLexer import JurjenLangLexer
from JurjenLangParser import JurjenLangParser
from JurjenLangCustomListener import *
 
def main(argv):
    input_stream = FileStream(argv[1])
    lexer = JurjenLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = JurjenLangParser(stream)
    tree = parser.startRule()
    
    listener = JurjenLangCustomListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

if __name__ == '__main__':
    main(sys.argv)