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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\13")
        buf.write("I\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2\3\2\3\3")
        buf.write("\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\5\6(\n\6")
        buf.write("\3\6\3\6\3\7\7\7-\n\7\f\7\16\7\60\13\7\3\b\3\b\3\t\3\t")
        buf.write("\3\n\3\n\3\n\3\n\3\13\3\13\3\13\5\13=\n\13\3\13\3\13\3")
        buf.write("\13\7\13B\n\13\f\13\16\13E\13\13\3\f\3\f\3\f\2\3\24\r")
        buf.write("\2\4\6\b\n\f\16\20\22\24\26\2\2\2A\2\30\3\2\2\2\4\33\3")
        buf.write("\2\2\2\6\36\3\2\2\2\b!\3\2\2\2\n$\3\2\2\2\f.\3\2\2\2\16")
        buf.write("\61\3\2\2\2\20\63\3\2\2\2\22\65\3\2\2\2\24<\3\2\2\2\26")
        buf.write("F\3\2\2\2\30\31\5\4\3\2\31\32\7\2\2\3\32\3\3\2\2\2\33")
        buf.write("\34\5\6\4\2\34\35\5\n\6\2\35\5\3\2\2\2\36\37\7\6\2\2\37")
        buf.write(" \7\t\2\2 \7\3\2\2\2!\"\7\7\2\2\"#\5\20\t\2#\t\3\2\2\2")
        buf.write("$%\7\3\2\2%\'\5\f\7\2&(\5\b\5\2\'&\3\2\2\2\'(\3\2\2\2")
        buf.write("()\3\2\2\2)*\7\4\2\2*\13\3\2\2\2+-\5\16\b\2,+\3\2\2\2")
        buf.write("-\60\3\2\2\2.,\3\2\2\2./\3\2\2\2/\r\3\2\2\2\60.\3\2\2")
        buf.write("\2\61\62\5\22\n\2\62\17\3\2\2\2\63\64\5\24\13\2\64\21")
        buf.write("\3\2\2\2\65\66\5\26\f\2\66\67\7\5\2\2\678\5\24\13\28\23")
        buf.write("\3\2\2\29:\b\13\1\2:=\7\b\2\2;=\5\26\f\2<9\3\2\2\2<;\3")
        buf.write("\2\2\2=C\3\2\2\2>?\f\5\2\2?@\7\n\2\2@B\5\24\13\6A>\3\2")
        buf.write("\2\2BE\3\2\2\2CA\3\2\2\2CD\3\2\2\2D\25\3\2\2\2EC\3\2\2")
        buf.write("\2FG\7\t\2\2G\27\3\2\2\2\6\'.<C")
        return buf.getvalue()


class JurjenLangParser ( Parser ):

    grammarFileName = "JurjenLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'}'", "'='", "'func'", "'return'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "FUNC_KW", "FUNC_RET", "INT", "IDENTIFIER", "OPERATOR", 
                      "WS" ]

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
    RULE_variable = 10

    ruleNames =  [ "startRule", "func", "func_def", "func_return", "scope", 
                   "stats", "stat", "retstat", "ass", "e", "variable" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    FUNC_KW=4
    FUNC_RET=5
    INT=6
    IDENTIFIER=7
    OPERATOR=8
    WS=9

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
            self.state = 22
            self.func()
            self.state = 23
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
            self.state = 25
            self.func_def()
            self.state = 26
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
            self.state = 28
            self.match(JurjenLangParser.FUNC_KW)
            self.state = 29
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
            self.state = 31
            self.match(JurjenLangParser.FUNC_RET)
            self.state = 32
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
            self.state = 34
            self.match(JurjenLangParser.T__0)
            self.state = 35
            self.stats()
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==JurjenLangParser.FUNC_RET:
                self.state = 36
                self.func_return()


            self.state = 39
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
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==JurjenLangParser.IDENTIFIER:
                self.state = 41
                self.stat()
                self.state = 46
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
            self.state = 47
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
            self.state = 49
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
            self.state = 51
            self.variable()
            self.state = 52
            self.match(JurjenLangParser.T__2)
            self.state = 53
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

        def INT(self):
            return self.getToken(JurjenLangParser.INT, 0)

        def variable(self):
            return self.getTypedRuleContext(JurjenLangParser.VariableContext,0)


        def e(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JurjenLangParser.EContext)
            else:
                return self.getTypedRuleContext(JurjenLangParser.EContext,i)


        def OPERATOR(self):
            return self.getToken(JurjenLangParser.OPERATOR, 0)

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
            self.state = 58
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JurjenLangParser.INT]:
                self.state = 56
                self.match(JurjenLangParser.INT)
                pass
            elif token in [JurjenLangParser.IDENTIFIER]:
                self.state = 57
                self.variable()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 65
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = JurjenLangParser.EContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_e)
                    self.state = 60
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 61
                    self.match(JurjenLangParser.OPERATOR)
                    self.state = 62
                    self.e(4) 
                self.state = 67
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
        self.enterRule(localctx, 20, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(JurjenLangParser.IDENTIFIER)
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
                return self.precpred(self._ctx, 3)
         




