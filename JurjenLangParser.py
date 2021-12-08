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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\16")
        buf.write("W\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\3\2\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3\5\3")
        buf.write("\6\3\6\3\6\5\6,\n\6\3\6\3\6\3\7\7\7\61\n\7\f\7\16\7\64")
        buf.write("\13\7\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3")
        buf.write("\13\5\13B\n\13\3\13\3\13\3\13\3\13\3\13\3\13\7\13J\n\13")
        buf.write("\f\13\16\13M\13\13\3\f\3\f\3\f\3\f\3\r\3\r\3\16\3\16\3")
        buf.write("\16\2\3\24\17\2\4\6\b\n\f\16\20\22\24\26\30\32\2\2\2O")
        buf.write("\2\34\3\2\2\2\4\37\3\2\2\2\6\"\3\2\2\2\b%\3\2\2\2\n(\3")
        buf.write("\2\2\2\f\62\3\2\2\2\16\65\3\2\2\2\20\67\3\2\2\2\229\3")
        buf.write("\2\2\2\24A\3\2\2\2\26N\3\2\2\2\30R\3\2\2\2\32T\3\2\2\2")
        buf.write("\34\35\5\4\3\2\35\36\7\2\2\3\36\3\3\2\2\2\37 \5\6\4\2")
        buf.write(" !\5\n\6\2!\5\3\2\2\2\"#\7\b\2\2#$\7\13\2\2$\7\3\2\2\2")
        buf.write("%&\7\t\2\2&\'\5\20\t\2\'\t\3\2\2\2()\7\3\2\2)+\5\f\7\2")
        buf.write("*,\5\b\5\2+*\3\2\2\2+,\3\2\2\2,-\3\2\2\2-.\7\4\2\2.\13")
        buf.write("\3\2\2\2/\61\5\16\b\2\60/\3\2\2\2\61\64\3\2\2\2\62\60")
        buf.write("\3\2\2\2\62\63\3\2\2\2\63\r\3\2\2\2\64\62\3\2\2\2\65\66")
        buf.write("\5\22\n\2\66\17\3\2\2\2\678\5\24\13\28\21\3\2\2\29:\5")
        buf.write("\30\r\2:;\7\5\2\2;<\5\24\13\2<\23\3\2\2\2=>\b\13\1\2>")
        buf.write("B\5\26\f\2?B\5\32\16\2@B\5\30\r\2A=\3\2\2\2A?\3\2\2\2")
        buf.write("A@\3\2\2\2BK\3\2\2\2CD\f\6\2\2DE\7\f\2\2EJ\5\24\13\7F")
        buf.write("G\f\5\2\2GH\7\r\2\2HJ\5\24\13\6IC\3\2\2\2IF\3\2\2\2JM")
        buf.write("\3\2\2\2KI\3\2\2\2KL\3\2\2\2L\25\3\2\2\2MK\3\2\2\2NO\7")
        buf.write("\6\2\2OP\5\24\13\2PQ\7\7\2\2Q\27\3\2\2\2RS\7\13\2\2S\31")
        buf.write("\3\2\2\2TU\7\n\2\2U\33\3\2\2\2\7+\62AIK")
        return buf.getvalue()


class JurjenLangParser ( Parser ):

    grammarFileName = "JurjenLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'}'", "'='", "'('", "')'", "'func'", 
                     "'return'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "FUNC_KW", "FUNC_RET", "NUMBERS", 
                      "IDENTIFIER", "OPERATOR_MD", "OPERATOR_AS", "WS" ]

    RULE_startRule = 0
    RULE_func = 1
    RULE_func_def = 2
    RULE_func_return = 3
    RULE_scope = 4
    RULE_stats = 5
    RULE_stat = 6
    RULE_retstat = 7
    RULE_ass = 8
    RULE_e = 9
    RULE_prio_e = 10
    RULE_variable = 11
    RULE_integer = 12

    ruleNames =  [ "startRule", "func", "func_def", "func_return", "scope", 
                   "stats", "stat", "retstat", "ass", "e", "prio_e", "variable", 
                   "integer" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    FUNC_KW=6
    FUNC_RET=7
    NUMBERS=8
    IDENTIFIER=9
    OPERATOR_MD=10
    OPERATOR_AS=11
    WS=12

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
            self.state = 26
            self.func()
            self.state = 27
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
            self.state = 29
            self.func_def()
            self.state = 30
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
            self.state = 32
            self.match(JurjenLangParser.FUNC_KW)
            self.state = 33
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
            self.state = 35
            self.match(JurjenLangParser.FUNC_RET)
            self.state = 36
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
            self.state = 38
            self.match(JurjenLangParser.T__0)
            self.state = 39
            self.stats()
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==JurjenLangParser.FUNC_RET:
                self.state = 40
                self.func_return()


            self.state = 43
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
            self.state = 48
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==JurjenLangParser.IDENTIFIER:
                self.state = 45
                self.stat()
                self.state = 50
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
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.ass()
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
        self.enterRule(localctx, 14, self.RULE_retstat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
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
        self.enterRule(localctx, 16, self.RULE_ass)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.variable()
            self.state = 56
            self.match(JurjenLangParser.T__2)
            self.state = 57
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
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_e, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JurjenLangParser.T__3]:
                self.state = 60
                self.prio_e()
                pass
            elif token in [JurjenLangParser.NUMBERS]:
                self.state = 61
                self.integer()
                pass
            elif token in [JurjenLangParser.IDENTIFIER]:
                self.state = 62
                self.variable()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 73
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 71
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = JurjenLangParser.EContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_e)
                        self.state = 65
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 66
                        self.match(JurjenLangParser.OPERATOR_MD)
                        self.state = 67
                        self.e(5)
                        pass

                    elif la_ == 2:
                        localctx = JurjenLangParser.EContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_e)
                        self.state = 68
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 69
                        self.match(JurjenLangParser.OPERATOR_AS)
                        self.state = 70
                        self.e(4)
                        pass

             
                self.state = 75
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

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
        self.enterRule(localctx, 20, self.RULE_prio_e)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(JurjenLangParser.T__3)
            self.state = 77
            self.e(0)
            self.state = 78
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
        self.enterRule(localctx, 22, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
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
        self.enterRule(localctx, 24, self.RULE_integer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
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
        self._predicates[9] = self.e_sempred
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
         




