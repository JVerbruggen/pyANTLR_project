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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\16")
        buf.write("P\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3")
        buf.write("\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t")
        buf.write("\6\t\67\n\t\r\t\16\t8\3\n\3\n\7\n=\n\n\f\n\16\n@\13\n")
        buf.write("\3\13\3\13\3\f\3\f\3\r\6\rG\n\r\r\r\16\rH\3\r\3\r\3\16")
        buf.write("\3\16\3\17\3\17\2\2\20\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\31\16\33\2\35\2\3\2\7\4\2C\\c|\6\2")
        buf.write("\62;C\\aac|\4\2,,\61\61\4\2--//\5\2\13\f\17\17\"\"\2P")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\3\37\3\2")
        buf.write("\2\2\5!\3\2\2\2\7#\3\2\2\2\t%\3\2\2\2\13\'\3\2\2\2\r)")
        buf.write("\3\2\2\2\17.\3\2\2\2\21\66\3\2\2\2\23:\3\2\2\2\25A\3\2")
        buf.write("\2\2\27C\3\2\2\2\31F\3\2\2\2\33L\3\2\2\2\35N\3\2\2\2\37")
        buf.write(" \7}\2\2 \4\3\2\2\2!\"\7\177\2\2\"\6\3\2\2\2#$\7?\2\2")
        buf.write("$\b\3\2\2\2%&\7*\2\2&\n\3\2\2\2\'(\7+\2\2(\f\3\2\2\2)")
        buf.write("*\7h\2\2*+\7w\2\2+,\7p\2\2,-\7e\2\2-\16\3\2\2\2./\7t\2")
        buf.write("\2/\60\7g\2\2\60\61\7v\2\2\61\62\7w\2\2\62\63\7t\2\2\63")
        buf.write("\64\7p\2\2\64\20\3\2\2\2\65\67\5\33\16\2\66\65\3\2\2\2")
        buf.write("\678\3\2\2\28\66\3\2\2\289\3\2\2\29\22\3\2\2\2:>\t\2\2")
        buf.write("\2;=\t\3\2\2<;\3\2\2\2=@\3\2\2\2><\3\2\2\2>?\3\2\2\2?")
        buf.write("\24\3\2\2\2@>\3\2\2\2AB\t\4\2\2B\26\3\2\2\2CD\t\5\2\2")
        buf.write("D\30\3\2\2\2EG\t\6\2\2FE\3\2\2\2GH\3\2\2\2HF\3\2\2\2H")
        buf.write("I\3\2\2\2IJ\3\2\2\2JK\b\r\2\2K\32\3\2\2\2LM\4\62;\2M\34")
        buf.write("\3\2\2\2NO\4\62\63\2O\36\3\2\2\2\6\28>H\3\b\2\2")
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
    NUMBERS = 8
    IDENTIFIER = 9
    OPERATOR_MD = 10
    OPERATOR_AS = 11
    WS = 12

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'{'", "'}'", "'='", "'('", "')'", "'func'", "'return'" ]

    symbolicNames = [ "<INVALID>",
            "FUNC_KW", "FUNC_RET", "NUMBERS", "IDENTIFIER", "OPERATOR_MD", 
            "OPERATOR_AS", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "FUNC_KW", "FUNC_RET", 
                  "NUMBERS", "IDENTIFIER", "OPERATOR_MD", "OPERATOR_AS", 
                  "WS", "DIGIT", "BIT" ]

    grammarFileName = "JurjenLang.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


