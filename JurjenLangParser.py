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
        buf.write("C\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\4\3\4\3\4\3\5\3\5\3\5\3\6\7\6%\n\6\f\6\16\6(\13\6")
        buf.write("\3\7\3\7\3\b\3\b\5\b.\n\b\3\t\3\t\3\t\3\t\3\t\3\t\5\t")
        buf.write("\66\n\t\3\n\3\n\3\n\3\n\3\n\3\n\7\n>\n\n\f\n\16\nA\13")
        buf.write("\n\3\n\2\3\22\13\2\4\6\b\n\f\16\20\22\2\2\2=\2\24\3\2")
        buf.write("\2\2\4\27\3\2\2\2\6\35\3\2\2\2\b \3\2\2\2\n&\3\2\2\2\f")
        buf.write(")\3\2\2\2\16-\3\2\2\2\20\65\3\2\2\2\22\67\3\2\2\2\24\25")
        buf.write("\5\4\3\2\25\26\7\2\2\3\26\3\3\2\2\2\27\30\5\6\4\2\30\31")
        buf.write("\7\3\2\2\31\32\5\n\6\2\32\33\5\b\5\2\33\34\7\4\2\2\34")
        buf.write("\5\3\2\2\2\35\36\7\6\2\2\36\37\7\t\2\2\37\7\3\2\2\2 !")
        buf.write("\7\7\2\2!\"\5\16\b\2\"\t\3\2\2\2#%\5\f\7\2$#\3\2\2\2%")
        buf.write("(\3\2\2\2&$\3\2\2\2&\'\3\2\2\2\'\13\3\2\2\2(&\3\2\2\2")
        buf.write(")*\5\20\t\2*\r\3\2\2\2+.\5\22\n\2,.\7\t\2\2-+\3\2\2\2")
        buf.write("-,\3\2\2\2.\17\3\2\2\2/\60\7\t\2\2\60\61\7\5\2\2\61\66")
        buf.write("\5\22\n\2\62\63\7\t\2\2\63\64\7\5\2\2\64\66\7\t\2\2\65")
        buf.write("/\3\2\2\2\65\62\3\2\2\2\66\21\3\2\2\2\678\b\n\1\289\7")
        buf.write("\b\2\29?\3\2\2\2:;\f\4\2\2;<\7\n\2\2<>\5\22\n\5=:\3\2")
        buf.write("\2\2>A\3\2\2\2?=\3\2\2\2?@\3\2\2\2@\23\3\2\2\2A?\3\2\2")
        buf.write("\2\6&-\65?")
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
    RULE_stats = 4
    RULE_stat = 5
    RULE_retstat = 6
    RULE_ass = 7
    RULE_e = 8

    ruleNames =  [ "startRule", "func", "func_def", "func_return", "stats", 
                   "stat", "retstat", "ass", "e" ]

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
            self.state = 18
            self.func()
            self.state = 19
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


        def stats(self):
            return self.getTypedRuleContext(JurjenLangParser.StatsContext,0)


        def func_return(self):
            return self.getTypedRuleContext(JurjenLangParser.Func_returnContext,0)


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
            self.state = 21
            self.func_def()
            self.state = 22
            self.match(JurjenLangParser.T__0)
            self.state = 23
            self.stats()
            self.state = 24
            self.func_return()
            self.state = 25
            self.match(JurjenLangParser.T__1)
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
            self.state = 27
            self.match(JurjenLangParser.FUNC_KW)
            self.state = 28
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
            self.state = 30
            self.match(JurjenLangParser.FUNC_RET)
            self.state = 31
            self.retstat()
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
        self.enterRule(localctx, 8, self.RULE_stats)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==JurjenLangParser.IDENTIFIER:
                self.state = 33
                self.stat()
                self.state = 38
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
        self.enterRule(localctx, 10, self.RULE_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
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


        def IDENTIFIER(self):
            return self.getToken(JurjenLangParser.IDENTIFIER, 0)

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
        self.enterRule(localctx, 12, self.RULE_retstat)
        try:
            self.state = 43
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JurjenLangParser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                self.e(0)
                pass
            elif token in [JurjenLangParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 42
                self.match(JurjenLangParser.IDENTIFIER)
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


    class AssContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(JurjenLangParser.IDENTIFIER)
            else:
                return self.getToken(JurjenLangParser.IDENTIFIER, i)

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
        self.enterRule(localctx, 14, self.RULE_ass)
        try:
            self.state = 51
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 45
                self.match(JurjenLangParser.IDENTIFIER)
                self.state = 46
                self.match(JurjenLangParser.T__2)
                self.state = 47
                self.e(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 48
                self.match(JurjenLangParser.IDENTIFIER)
                self.state = 49
                self.match(JurjenLangParser.T__2)
                self.state = 50
                self.match(JurjenLangParser.IDENTIFIER)
                pass


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
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_e, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(JurjenLangParser.INT)
            self._ctx.stop = self._input.LT(-1)
            self.state = 61
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = JurjenLangParser.EContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_e)
                    self.state = 56
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 57
                    self.match(JurjenLangParser.OPERATOR)
                    self.state = 58
                    self.e(3) 
                self.state = 63
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[8] = self.e_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def e_sempred(self, localctx:EContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




