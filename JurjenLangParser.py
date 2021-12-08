# Generated from JurjenLang.g4 by ANTLR 4.9.3
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\20")
        buf.write("`\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\4\17\t\17\3\2\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3\4\3\5")
        buf.write("\3\5\3\5\3\6\3\6\3\6\5\6.\n\6\3\6\3\6\3\7\7\7\63\n\7\f")
        buf.write("\7\16\7\66\13\7\3\b\3\b\5\b:\n\b\3\t\3\t\3\t\3\n\3\n\3")
        buf.write("\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\5\fI\n\f\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\f\7\fS\n\f\f\f\16\fV\13\f\3\r\3\r")
        buf.write("\3\r\3\r\3\16\3\16\3\17\3\17\3\17\2\3\26\20\2\4\6\b\n")
        buf.write("\f\16\20\22\24\26\30\32\34\2\2\2Y\2\36\3\2\2\2\4!\3\2")
        buf.write("\2\2\6$\3\2\2\2\b\'\3\2\2\2\n*\3\2\2\2\f\64\3\2\2\2\16")
        buf.write("9\3\2\2\2\20;\3\2\2\2\22>\3\2\2\2\24@\3\2\2\2\26H\3\2")
        buf.write("\2\2\30W\3\2\2\2\32[\3\2\2\2\34]\3\2\2\2\36\37\5\4\3\2")
        buf.write("\37 \7\2\2\3 \3\3\2\2\2!\"\5\6\4\2\"#\5\n\6\2#\5\3\2\2")
        buf.write("\2$%\7\b\2\2%&\7\f\2\2&\7\3\2\2\2\'(\7\t\2\2()\5\22\n")
        buf.write("\2)\t\3\2\2\2*+\7\3\2\2+-\5\f\7\2,.\5\b\5\2-,\3\2\2\2")
        buf.write("-.\3\2\2\2./\3\2\2\2/\60\7\4\2\2\60\13\3\2\2\2\61\63\5")
        buf.write("\16\b\2\62\61\3\2\2\2\63\66\3\2\2\2\64\62\3\2\2\2\64\65")
        buf.write("\3\2\2\2\65\r\3\2\2\2\66\64\3\2\2\2\67:\5\24\13\28:\5")
        buf.write("\20\t\29\67\3\2\2\298\3\2\2\2:\17\3\2\2\2;<\7\n\2\2<=")
        buf.write("\5\26\f\2=\21\3\2\2\2>?\5\26\f\2?\23\3\2\2\2@A\5\32\16")
        buf.write("\2AB\7\5\2\2BC\5\26\f\2C\25\3\2\2\2DE\b\f\1\2EI\5\30\r")
        buf.write("\2FI\5\34\17\2GI\5\32\16\2HD\3\2\2\2HF\3\2\2\2HG\3\2\2")
        buf.write("\2IT\3\2\2\2JK\f\6\2\2KL\7\16\2\2LS\5\26\f\7MN\f\5\2\2")
        buf.write("NO\7\17\2\2OS\5\26\f\6PQ\f\7\2\2QS\7\r\2\2RJ\3\2\2\2R")
        buf.write("M\3\2\2\2RP\3\2\2\2SV\3\2\2\2TR\3\2\2\2TU\3\2\2\2U\27")
        buf.write("\3\2\2\2VT\3\2\2\2WX\7\6\2\2XY\5\26\f\2YZ\7\7\2\2Z\31")
        buf.write("\3\2\2\2[\\\7\f\2\2\\\33\3\2\2\2]^\7\13\2\2^\35\3\2\2")
        buf.write("\2\b-\649HRT")
        return buf.getvalue()


class JurjenLangParser ( Parser ):

    grammarFileName = "JurjenLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'}'", "'='", "'('", "')'", "'func'", 
                     "'return'", "'print'", "<INVALID>", "<INVALID>", "'!'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "FUNC_KW", "FUNC_RET", "PRINT_KW", 
                      "NUMBERS", "IDENTIFIER", "OPERATOR_FAC", "OPERATOR_MD", 
                      "OPERATOR_AS", "WS" ]

    RULE_startRule = 0
    RULE_func = 1
    RULE_func_def = 2
    RULE_func_return = 3
    RULE_scope = 4
    RULE_stats = 5
    RULE_stat = 6
    RULE_printstat = 7
    RULE_retstat = 8
    RULE_ass = 9
    RULE_e = 10
    RULE_prio_e = 11
    RULE_variable = 12
    RULE_integer = 13

    ruleNames =  [ "startRule", "func", "func_def", "func_return", "scope", 
                   "stats", "stat", "printstat", "retstat", "ass", "e", 
                   "prio_e", "variable", "integer" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    FUNC_KW=6
    FUNC_RET=7
    PRINT_KW=8
    NUMBERS=9
    IDENTIFIER=10
    OPERATOR_FAC=11
    OPERATOR_MD=12
    OPERATOR_AS=13
    WS=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartRuleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func(self):
            return self.getTypedRuleContext(JurjenLangParser.FuncContext,0)


        def EOF(self):
            return self.getToken(JurjenLangParser.EOF, 0)

        def getRuleIndex(self):
            return JurjenLangParser.RULE_startRule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStartRule" ):
                listener.enterStartRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStartRule" ):
                listener.exitStartRule(self)




    def startRule(self):

        localctx = JurjenLangParser.StartRuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_startRule)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.func()
            self.state = 29
            self.match(JurjenLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_def(self):
            return self.getTypedRuleContext(JurjenLangParser.Func_defContext,0)


        def scope(self):
            return self.getTypedRuleContext(JurjenLangParser.ScopeContext,0)


        def getRuleIndex(self):
            return JurjenLangParser.RULE_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc" ):
                listener.enterFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc" ):
                listener.exitFunc(self)




    def func(self):

        localctx = JurjenLangParser.FuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.func_def()
            self.state = 32
            self.scope()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC_KW(self):
            return self.getToken(JurjenLangParser.FUNC_KW, 0)

        def IDENTIFIER(self):
            return self.getToken(JurjenLangParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return JurjenLangParser.RULE_func_def

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_def" ):
                listener.enterFunc_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_def" ):
                listener.exitFunc_def(self)




    def func_def(self):

        localctx = JurjenLangParser.Func_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_func_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(JurjenLangParser.FUNC_KW)
            self.state = 35
            self.match(JurjenLangParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_returnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC_RET(self):
            return self.getToken(JurjenLangParser.FUNC_RET, 0)

        def retstat(self):
            return self.getTypedRuleContext(JurjenLangParser.RetstatContext,0)


        def getRuleIndex(self):
            return JurjenLangParser.RULE_func_return

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_return" ):
                listener.enterFunc_return(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_return" ):
                listener.exitFunc_return(self)




    def func_return(self):

        localctx = JurjenLangParser.Func_returnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_func_return)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(JurjenLangParser.FUNC_RET)
            self.state = 38
            self.retstat()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScopeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stats(self):
            return self.getTypedRuleContext(JurjenLangParser.StatsContext,0)


        def func_return(self):
            return self.getTypedRuleContext(JurjenLangParser.Func_returnContext,0)


        def getRuleIndex(self):
            return JurjenLangParser.RULE_scope

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScope" ):
                listener.enterScope(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScope" ):
                listener.exitScope(self)




    def scope(self):

        localctx = JurjenLangParser.ScopeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_scope)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(JurjenLangParser.T__0)
            self.state = 41
            self.stats()
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==JurjenLangParser.FUNC_RET:
                self.state = 42
                self.func_return()


            self.state = 45
            self.match(JurjenLangParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JurjenLangParser.StatContext)
            else:
                return self.getTypedRuleContext(JurjenLangParser.StatContext,i)


        def getRuleIndex(self):
            return JurjenLangParser.RULE_stats

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStats" ):
                listener.enterStats(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStats" ):
                listener.exitStats(self)




    def stats(self):

        localctx = JurjenLangParser.StatsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_stats)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==JurjenLangParser.PRINT_KW or _la==JurjenLangParser.IDENTIFIER:
                self.state = 47
                self.stat()
                self.state = 52
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ass(self):
            return self.getTypedRuleContext(JurjenLangParser.AssContext,0)


        def printstat(self):
            return self.getTypedRuleContext(JurjenLangParser.PrintstatContext,0)


        def getRuleIndex(self):
            return JurjenLangParser.RULE_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat" ):
                listener.enterStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat" ):
                listener.exitStat(self)




    def stat(self):

        localctx = JurjenLangParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_stat)
        try:
            self.state = 55
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JurjenLangParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 53
                self.ass()
                pass
            elif token in [JurjenLangParser.PRINT_KW]:
                self.enterOuterAlt(localctx, 2)
                self.state = 54
                self.printstat()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintstatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT_KW(self):
            return self.getToken(JurjenLangParser.PRINT_KW, 0)

        def e(self):
            return self.getTypedRuleContext(JurjenLangParser.EContext,0)


        def getRuleIndex(self):
            return JurjenLangParser.RULE_printstat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintstat" ):
                listener.enterPrintstat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintstat" ):
                listener.exitPrintstat(self)




    def printstat(self):

        localctx = JurjenLangParser.PrintstatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_printstat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(JurjenLangParser.PRINT_KW)
            self.state = 58
            self.e(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RetstatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def e(self):
            return self.getTypedRuleContext(JurjenLangParser.EContext,0)


        def getRuleIndex(self):
            return JurjenLangParser.RULE_retstat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRetstat" ):
                listener.enterRetstat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRetstat" ):
                listener.exitRetstat(self)




    def retstat(self):

        localctx = JurjenLangParser.RetstatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_retstat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.e(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(JurjenLangParser.VariableContext,0)


        def e(self):
            return self.getTypedRuleContext(JurjenLangParser.EContext,0)


        def getRuleIndex(self):
            return JurjenLangParser.RULE_ass

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAss" ):
                listener.enterAss(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAss" ):
                listener.exitAss(self)




    def ass(self):

        localctx = JurjenLangParser.AssContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_ass)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.variable()
            self.state = 63
            self.match(JurjenLangParser.T__2)
            self.state = 64
            self.e(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def prio_e(self):
            return self.getTypedRuleContext(JurjenLangParser.Prio_eContext,0)


        def integer(self):
            return self.getTypedRuleContext(JurjenLangParser.IntegerContext,0)


        def variable(self):
            return self.getTypedRuleContext(JurjenLangParser.VariableContext,0)


        def e(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JurjenLangParser.EContext)
            else:
                return self.getTypedRuleContext(JurjenLangParser.EContext,i)


        def OPERATOR_MD(self):
            return self.getToken(JurjenLangParser.OPERATOR_MD, 0)

        def OPERATOR_AS(self):
            return self.getToken(JurjenLangParser.OPERATOR_AS, 0)

        def OPERATOR_FAC(self):
            return self.getToken(JurjenLangParser.OPERATOR_FAC, 0)

        def getRuleIndex(self):
            return JurjenLangParser.RULE_e

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterE" ):
                listener.enterE(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitE" ):
                listener.exitE(self)



    def e(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = JurjenLangParser.EContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_e, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JurjenLangParser.T__3]:
                self.state = 67
                self.prio_e()
                pass
            elif token in [JurjenLangParser.NUMBERS]:
                self.state = 68
                self.integer()
                pass
            elif token in [JurjenLangParser.IDENTIFIER]:
                self.state = 69
                self.variable()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 82
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 80
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = JurjenLangParser.EContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_e)
                        self.state = 72
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 73
                        self.match(JurjenLangParser.OPERATOR_MD)
                        self.state = 74
                        self.e(5)
                        pass

                    elif la_ == 2:
                        localctx = JurjenLangParser.EContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_e)
                        self.state = 75
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 76
                        self.match(JurjenLangParser.OPERATOR_AS)
                        self.state = 77
                        self.e(4)
                        pass

                    elif la_ == 3:
                        localctx = JurjenLangParser.EContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_e)
                        self.state = 78
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 79
                        self.match(JurjenLangParser.OPERATOR_FAC)
                        pass

             
                self.state = 84
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Prio_eContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def e(self):
            return self.getTypedRuleContext(JurjenLangParser.EContext,0)


        def getRuleIndex(self):
            return JurjenLangParser.RULE_prio_e

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrio_e" ):
                listener.enterPrio_e(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrio_e" ):
                listener.exitPrio_e(self)




    def prio_e(self):

        localctx = JurjenLangParser.Prio_eContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_prio_e)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(JurjenLangParser.T__3)
            self.state = 86
            self.e(0)
            self.state = 87
            self.match(JurjenLangParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(JurjenLangParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return JurjenLangParser.RULE_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)




    def variable(self):

        localctx = JurjenLangParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(JurjenLangParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntegerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBERS(self):
            return self.getToken(JurjenLangParser.NUMBERS, 0)

        def getRuleIndex(self):
            return JurjenLangParser.RULE_integer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInteger" ):
                listener.enterInteger(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInteger" ):
                listener.exitInteger(self)




    def integer(self):

        localctx = JurjenLangParser.IntegerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_integer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(JurjenLangParser.NUMBERS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[10] = self.e_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def e_sempred(self, localctx:EContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         




