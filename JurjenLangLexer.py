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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\20")
        buf.write("\\\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\3\2\3\3\3\3\3")
        buf.write("\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n\6\nA\n\n")
        buf.write("\r\n\16\nB\3\13\3\13\7\13G\n\13\f\13\16\13J\13\13\3\f")
        buf.write("\3\f\3\r\3\r\3\16\3\16\3\17\6\17S\n\17\r\17\16\17T\3\17")
        buf.write("\3\17\3\20\3\20\3\21\3\21\2\2\22\3\3\5\4\7\5\t\6\13\7")
        buf.write("\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\2")
        buf.write("!\2\3\2\7\4\2C\\c|\6\2\62;C\\aac|\4\2,,\61\61\4\2--//")
        buf.write("\5\2\13\f\17\17\"\"\2\\\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3")
        buf.write("\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2")
        buf.write("\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2")
        buf.write("\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\3#\3\2\2\2\5%")
        buf.write("\3\2\2\2\7\'\3\2\2\2\t)\3\2\2\2\13+\3\2\2\2\r-\3\2\2\2")
        buf.write("\17\62\3\2\2\2\219\3\2\2\2\23@\3\2\2\2\25D\3\2\2\2\27")
        buf.write("K\3\2\2\2\31M\3\2\2\2\33O\3\2\2\2\35R\3\2\2\2\37X\3\2")
        buf.write("\2\2!Z\3\2\2\2#$\7}\2\2$\4\3\2\2\2%&\7\177\2\2&\6\3\2")
        buf.write("\2\2\'(\7?\2\2(\b\3\2\2\2)*\7*\2\2*\n\3\2\2\2+,\7+\2\2")
        buf.write(",\f\3\2\2\2-.\7h\2\2./\7w\2\2/\60\7p\2\2\60\61\7e\2\2")
        buf.write("\61\16\3\2\2\2\62\63\7t\2\2\63\64\7g\2\2\64\65\7v\2\2")
        buf.write("\65\66\7w\2\2\66\67\7t\2\2\678\7p\2\28\20\3\2\2\29:\7")
        buf.write("r\2\2:;\7t\2\2;<\7k\2\2<=\7p\2\2=>\7v\2\2>\22\3\2\2\2")
        buf.write("?A\5\37\20\2@?\3\2\2\2AB\3\2\2\2B@\3\2\2\2BC\3\2\2\2C")
        buf.write("\24\3\2\2\2DH\t\2\2\2EG\t\3\2\2FE\3\2\2\2GJ\3\2\2\2HF")
        buf.write("\3\2\2\2HI\3\2\2\2I\26\3\2\2\2JH\3\2\2\2KL\7#\2\2L\30")
        buf.write("\3\2\2\2MN\t\4\2\2N\32\3\2\2\2OP\t\5\2\2P\34\3\2\2\2Q")
        buf.write("S\t\6\2\2RQ\3\2\2\2ST\3\2\2\2TR\3\2\2\2TU\3\2\2\2UV\3")
        buf.write("\2\2\2VW\b\17\2\2W\36\3\2\2\2XY\4\62;\2Y \3\2\2\2Z[\4")
        buf.write("\62\63\2[\"\3\2\2\2\6\2BHT\3\b\2\2")
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
    OPERATOR_MD = 12
    OPERATOR_AS = 13
    WS = 14

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'{'", "'}'", "'='", "'('", "')'", "'func'", "'return'", "'print'", 
            "'!'" ]

    symbolicNames = [ "<INVALID>",
            "FUNC_KW", "FUNC_RET", "PRINT_KW", "NUMBERS", "IDENTIFIER", 
            "OPERATOR_FAC", "OPERATOR_MD", "OPERATOR_AS", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "FUNC_KW", "FUNC_RET", 
                  "PRINT_KW", "NUMBERS", "IDENTIFIER", "OPERATOR_FAC", "OPERATOR_MD", 
                  "OPERATOR_AS", "WS", "DIGIT", "BIT" ]

    grammarFileName = "JurjenLang.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


