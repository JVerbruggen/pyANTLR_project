// Generated from JurjenLang.g4 by ANTLR 4.9.3
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class JurjenLangParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.9.3", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, FUNC_KW=4, FUNC_RET=5, INT=6, IDENTIFIER=7, OPERATOR=8, 
		WS=9;
	public static final int
		RULE_startRule = 0, RULE_func = 1, RULE_func_def = 2, RULE_func_return = 3, 
		RULE_stats = 4, RULE_stat = 5, RULE_retstat = 6, RULE_ass = 7, RULE_e = 8;
	private static String[] makeRuleNames() {
		return new String[] {
			"startRule", "func", "func_def", "func_return", "stats", "stat", "retstat", 
			"ass", "e"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'{'", "'}'", "'='", "'func'", "'return'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, "FUNC_KW", "FUNC_RET", "INT", "IDENTIFIER", "OPERATOR", 
			"WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "JurjenLang.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public JurjenLangParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class StartRuleContext extends ParserRuleContext {
		public FuncContext func() {
			return getRuleContext(FuncContext.class,0);
		}
		public TerminalNode EOF() { return getToken(JurjenLangParser.EOF, 0); }
		public StartRuleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_startRule; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof JurjenLangListener ) ((JurjenLangListener)listener).enterStartRule(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof JurjenLangListener ) ((JurjenLangListener)listener).exitStartRule(this);
		}
	}

	public final StartRuleContext startRule() throws RecognitionException {
		StartRuleContext _localctx = new StartRuleContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_startRule);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(18);
			func();
			setState(19);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FuncContext extends ParserRuleContext {
		public Func_defContext func_def() {
			return getRuleContext(Func_defContext.class,0);
		}
		public StatsContext stats() {
			return getRuleContext(StatsContext.class,0);
		}
		public Func_returnContext func_return() {
			return getRuleContext(Func_returnContext.class,0);
		}
		public FuncContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_func; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof JurjenLangListener ) ((JurjenLangListener)listener).enterFunc(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof JurjenLangListener ) ((JurjenLangListener)listener).exitFunc(this);
		}
	}

	public final FuncContext func() throws RecognitionException {
		FuncContext _localctx = new FuncContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_func);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(21);
			func_def();
			setState(22);
			match(T__0);
			setState(23);
			stats();
			setState(24);
			func_return();
			setState(25);
			match(T__1);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Func_defContext extends ParserRuleContext {
		public TerminalNode FUNC_KW() { return getToken(JurjenLangParser.FUNC_KW, 0); }
		public TerminalNode IDENTIFIER() { return getToken(JurjenLangParser.IDENTIFIER, 0); }
		public Func_defContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_func_def; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof JurjenLangListener ) ((JurjenLangListener)listener).enterFunc_def(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof JurjenLangListener ) ((JurjenLangListener)listener).exitFunc_def(this);
		}
	}

	public final Func_defContext func_def() throws RecognitionException {
		Func_defContext _localctx = new Func_defContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_func_def);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(27);
			match(FUNC_KW);
			setState(28);
			match(IDENTIFIER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Func_returnContext extends ParserRuleContext {
		public TerminalNode FUNC_RET() { return getToken(JurjenLangParser.FUNC_RET, 0); }
		public RetstatContext retstat() {
			return getRuleContext(RetstatContext.class,0);
		}
		public Func_returnContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_func_return; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof JurjenLangListener ) ((JurjenLangListener)listener).enterFunc_return(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof JurjenLangListener ) ((JurjenLangListener)listener).exitFunc_return(this);
		}
	}

	public final Func_returnContext func_return() throws RecognitionException {
		Func_returnContext _localctx = new Func_returnContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_func_return);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(30);
			match(FUNC_RET);
			setState(31);
			retstat();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StatsContext extends ParserRuleContext {
		public List<StatContext> stat() {
			return getRuleContexts(StatContext.class);
		}
		public StatContext stat(int i) {
			return getRuleContext(StatContext.class,i);
		}
		public StatsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stats; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof JurjenLangListener ) ((JurjenLangListener)listener).enterStats(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof JurjenLangListener ) ((JurjenLangListener)listener).exitStats(this);
		}
	}

	public final StatsContext stats() throws RecognitionException {
		StatsContext _localctx = new StatsContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_stats);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(36);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==IDENTIFIER) {
				{
				{
				setState(33);
				stat();
				}
				}
				setState(38);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StatContext extends ParserRuleContext {
		public AssContext ass() {
			return getRuleContext(AssContext.class,0);
		}
		public StatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stat; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof JurjenLangListener ) ((JurjenLangListener)listener).enterStat(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof JurjenLangListener ) ((JurjenLangListener)listener).exitStat(this);
		}
	}

	public final StatContext stat() throws RecognitionException {
		StatContext _localctx = new StatContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_stat);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(39);
			ass();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class RetstatContext extends ParserRuleContext {
		public EContext e() {
			return getRuleContext(EContext.class,0);
		}
		public TerminalNode IDENTIFIER() { return getToken(JurjenLangParser.IDENTIFIER, 0); }
		public RetstatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_retstat; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof JurjenLangListener ) ((JurjenLangListener)listener).enterRetstat(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof JurjenLangListener ) ((JurjenLangListener)listener).exitRetstat(this);
		}
	}

	public final RetstatContext retstat() throws RecognitionException {
		RetstatContext _localctx = new RetstatContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_retstat);
		try {
			setState(43);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT:
				enterOuterAlt(_localctx, 1);
				{
				setState(41);
				e(0);
				}
				break;
			case IDENTIFIER:
				enterOuterAlt(_localctx, 2);
				{
				setState(42);
				match(IDENTIFIER);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AssContext extends ParserRuleContext {
		public List<TerminalNode> IDENTIFIER() { return getTokens(JurjenLangParser.IDENTIFIER); }
		public TerminalNode IDENTIFIER(int i) {
			return getToken(JurjenLangParser.IDENTIFIER, i);
		}
		public EContext e() {
			return getRuleContext(EContext.class,0);
		}
		public AssContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ass; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof JurjenLangListener ) ((JurjenLangListener)listener).enterAss(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof JurjenLangListener ) ((JurjenLangListener)listener).exitAss(this);
		}
	}

	public final AssContext ass() throws RecognitionException {
		AssContext _localctx = new AssContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_ass);
		try {
			setState(51);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(45);
				match(IDENTIFIER);
				setState(46);
				match(T__2);
				setState(47);
				e(0);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(48);
				match(IDENTIFIER);
				setState(49);
				match(T__2);
				setState(50);
				match(IDENTIFIER);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class EContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(JurjenLangParser.INT, 0); }
		public List<EContext> e() {
			return getRuleContexts(EContext.class);
		}
		public EContext e(int i) {
			return getRuleContext(EContext.class,i);
		}
		public TerminalNode OPERATOR() { return getToken(JurjenLangParser.OPERATOR, 0); }
		public EContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_e; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof JurjenLangListener ) ((JurjenLangListener)listener).enterE(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof JurjenLangListener ) ((JurjenLangListener)listener).exitE(this);
		}
	}

	public final EContext e() throws RecognitionException {
		return e(0);
	}

	private EContext e(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		EContext _localctx = new EContext(_ctx, _parentState);
		EContext _prevctx = _localctx;
		int _startState = 16;
		enterRecursionRule(_localctx, 16, RULE_e, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(54);
			match(INT);
			}
			_ctx.stop = _input.LT(-1);
			setState(61);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,3,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new EContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_e);
					setState(56);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(57);
					match(OPERATOR);
					setState(58);
					e(3);
					}
					} 
				}
				setState(63);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,3,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 8:
			return e_sempred((EContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean e_sempred(EContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 2);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\13C\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\2"+
		"\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3\5\3\6\7\6%\n\6\f\6\16\6"+
		"(\13\6\3\7\3\7\3\b\3\b\5\b.\n\b\3\t\3\t\3\t\3\t\3\t\3\t\5\t\66\n\t\3\n"+
		"\3\n\3\n\3\n\3\n\3\n\7\n>\n\n\f\n\16\nA\13\n\3\n\2\3\22\13\2\4\6\b\n\f"+
		"\16\20\22\2\2\2=\2\24\3\2\2\2\4\27\3\2\2\2\6\35\3\2\2\2\b \3\2\2\2\n&"+
		"\3\2\2\2\f)\3\2\2\2\16-\3\2\2\2\20\65\3\2\2\2\22\67\3\2\2\2\24\25\5\4"+
		"\3\2\25\26\7\2\2\3\26\3\3\2\2\2\27\30\5\6\4\2\30\31\7\3\2\2\31\32\5\n"+
		"\6\2\32\33\5\b\5\2\33\34\7\4\2\2\34\5\3\2\2\2\35\36\7\6\2\2\36\37\7\t"+
		"\2\2\37\7\3\2\2\2 !\7\7\2\2!\"\5\16\b\2\"\t\3\2\2\2#%\5\f\7\2$#\3\2\2"+
		"\2%(\3\2\2\2&$\3\2\2\2&\'\3\2\2\2\'\13\3\2\2\2(&\3\2\2\2)*\5\20\t\2*\r"+
		"\3\2\2\2+.\5\22\n\2,.\7\t\2\2-+\3\2\2\2-,\3\2\2\2.\17\3\2\2\2/\60\7\t"+
		"\2\2\60\61\7\5\2\2\61\66\5\22\n\2\62\63\7\t\2\2\63\64\7\5\2\2\64\66\7"+
		"\t\2\2\65/\3\2\2\2\65\62\3\2\2\2\66\21\3\2\2\2\678\b\n\1\289\7\b\2\29"+
		"?\3\2\2\2:;\f\4\2\2;<\7\n\2\2<>\5\22\n\5=:\3\2\2\2>A\3\2\2\2?=\3\2\2\2"+
		"?@\3\2\2\2@\23\3\2\2\2A?\3\2\2\2\6&-\65?";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}