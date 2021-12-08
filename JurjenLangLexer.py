# Generated from JurjenLang.g4 by ANTLR 4.9.3
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\21")
        buf.write("`\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\3\2\3\2")
        buf.write("\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n")
        buf.write("\6\nC\n\n\r\n\16\nD\3\13\3\13\7\13I\n\13\f\13\16\13L\13")
        buf.write("\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\6\20W\n\20")
        buf.write("\r\20\16\20X\3\20\3\20\3\21\3\21\3\22\3\22\2\2\23\3\3")
        buf.write("\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\2#\2\3\2\7\4\2C\\c|\6\2\62;C\\aac")
        buf.write("|\4\2,,\61\61\4\2--//\5\2\13\f\17\17\"\"\2`\2\3\3\2\2")
        buf.write("\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25")
        buf.write("\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3")
        buf.write("\2\2\2\2\37\3\2\2\2\3%\3\2\2\2\5\'\3\2\2\2\7)\3\2\2\2")
        buf.write("\t+\3\2\2\2\13-\3\2\2\2\r/\3\2\2\2\17\64\3\2\2\2\21;\3")
        buf.write("\2\2\2\23B\3\2\2\2\25F\3\2\2\2\27M\3\2\2\2\31O\3\2\2\2")
        buf.write("\33Q\3\2\2\2\35S\3\2\2\2\37V\3\2\2\2!\\\3\2\2\2#^\3\2")
        buf.write("\2\2%&\7}\2\2&\4\3\2\2\2\'(\7\177\2\2(\6\3\2\2\2)*\7?")
        buf.write("\2\2*\b\3\2\2\2+,\7*\2\2,\n\3\2\2\2-.\7+\2\2.\f\3\2\2")
        buf.write("\2/\60\7h\2\2\60\61\7w\2\2\61\62\7p\2\2\62\63\7e\2\2\63")
        buf.write("\16\3\2\2\2\64\65\7t\2\2\65\66\7g\2\2\66\67\7v\2\2\67")
        buf.write("8\7w\2\289\7t\2\29:\7p\2\2:\20\3\2\2\2;<\7r\2\2<=\7t\2")
        buf.write("\2=>\7k\2\2>?\7p\2\2?@\7v\2\2@\22\3\2\2\2AC\5!\21\2BA")
        buf.write("\3\2\2\2CD\3\2\2\2DB\3\2\2\2DE\3\2\2\2E\24\3\2\2\2FJ\t")
        buf.write("\2\2\2GI\t\3\2\2HG\3\2\2\2IL\3\2\2\2JH\3\2\2\2JK\3\2\2")
        buf.write("\2K\26\3\2\2\2LJ\3\2\2\2MN\7#\2\2N\30\3\2\2\2OP\7`\2\2")
        buf.write("P\32\3\2\2\2QR\t\4\2\2R\34\3\2\2\2ST\t\5\2\2T\36\3\2\2")
        buf.write("\2UW\t\6\2\2VU\3\2\2\2WX\3\2\2\2XV\3\2\2\2XY\3\2\2\2Y")
        buf.write("Z\3\2\2\2Z[\b\20\2\2[ \3\2\2\2\\]\4\62;\2]\"\3\2\2\2^")
        buf.write("_\4\62\63\2_$\3\2\2\2\6\2DJX\3\b\2\2")
        return buf.getvalue()


class JurjenLangLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    FUNC_KW = 6
    FUNC_RET = 7
    PRINT_KW = 8
    NUMBERS = 9
    IDENTIFIER = 10
    OPERATOR_FAC = 11
    OPERATOR_EXP = 12
    OPERATOR_MD = 13
    OPERATOR_AS = 14
    WS = 15

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'{'", "'}'", "'='", "'('", "')'", "'func'", "'return'", "'print'", 
            "'!'", "'^'" ]

    symbolicNames = [ "<INVALID>",
            "FUNC_KW", "FUNC_RET", "PRINT_KW", "NUMBERS", "IDENTIFIER", 
            "OPERATOR_FAC", "OPERATOR_EXP", "OPERATOR_MD", "OPERATOR_AS", 
            "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "FUNC_KW", "FUNC_RET", 
                  "PRINT_KW", "NUMBERS", "IDENTIFIER", "OPERATOR_FAC", "OPERATOR_EXP", 
                  "OPERATOR_MD", "OPERATOR_AS", "WS", "DIGIT", "BIT" ]

    grammarFileName = "JurjenLang.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


