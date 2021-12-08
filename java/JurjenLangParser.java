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
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, FUNC_KW=6, FUNC_RET=7, NUMBERS=8, 
		IDENTIFIER=9, OPERATOR_MD=10, OPERATOR_AS=11, WS=12;
	public static final int
		RULE_startRule = 0, RULE_func = 1, RULE_func_def = 2, RULE_func_return = 3, 
		RULE_scope = 4, RULE_stats = 5, RULE_stat = 6, RULE_retstat = 7, RULE_ass = 8, 
		RULE_e = 9, RULE_prio_e = 10, RULE_variable = 11, RULE_integer = 12;
	private static String[] makeRuleNames() {
		return new String[] {
			"startRule", "func", "func_def", "func_return", "scope", "stats", "stat", 
			"retstat", "ass", "e", "prio_e", "variable", "integer"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'{'", "'}'", "'='", "'('", "')'", "'func'", "'return'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, "FUNC_KW", "FUNC_RET", "NUMBERS", 
			"IDENTIFIER", "OPERATOR_MD", "OPERATOR_AS", "WS"
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
			setState(26);
			func();
			setState(27);
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
		public ScopeContext scope() {
			return getRuleContext(ScopeContext.class,0);
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
			setState(29);
			func_def();
			setState(30);
			scope();
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
			setState(32);
			match(FUNC_KW);
			setState(33);
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
			setState(35);
			match(FUNC_RET);
			setState(36);
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

	public static class ScopeContext extends ParserRuleContext {
		public StatsContext stats() {
			return getRuleContext(StatsContext.class,0);
		}
		public Func_returnContext func_return() {
			return getRuleContext(Func_returnContext.class,0);
		}
		public ScopeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_scope; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof JurjenLangListener ) ((JurjenLangListener)listener).enterScope(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof JurjenLangListener ) ((JurjenLangListener)listener).exitScope(this);
		}
	}

	public final ScopeContext scope() throws RecognitionException {
		ScopeContext _localctx = new ScopeContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_scope);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(38);
			match(T__0);
			setState(39);
			stats();
			setState(41);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==FUNC_RET) {
				{
				setState(40);
				func_return();
				}
			}

			setState(43);
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
		enterRule(_localctx, 10, RULE_stats);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(48);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==IDENTIFIER) {
				{
				{
				setState(45);
				stat();
				}
				}
				setState(50);
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
		enterRule(_localctx, 12, RULE_stat);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(51);
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
		enterRule(_localctx, 14, RULE_retstat);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(53);
			e(0);
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
		public VariableContext variable() {
			return getRuleContext(VariableContext.class,0);
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
		enterRule(_localctx, 16, RULE_ass);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(55);
			variable();
			setState(56);
			match(T__2);
			setState(57);
			e(0);
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
		public Prio_eContext prio_e() {
			return getRuleContext(Prio_eContext.class,0);
		}
		public IntegerContext integer() {
			return getRuleContext(IntegerContext.class,0);
		}
		public VariableContext variable() {
			return getRuleContext(VariableContext.class,0);
		}
		public List<EContext> e() {
			return getRuleContexts(EContext.class);
		}
		public EContext e(int i) {
			return getRuleContext(EContext.class,i);
		}
		public TerminalNode OPERATOR_MD() { return getToken(JurjenLangParser.OPERATOR_MD, 0); }
		public TerminalNode OPERATOR_AS() { return getToken(JurjenLangParser.OPERATOR_AS, 0); }
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
		int _startState = 18;
		enterRecursionRule(_localctx, 18, RULE_e, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(63);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__3:
				{
				setState(60);
				prio_e();
				}
				break;
			case NUMBERS:
				{
				setState(61);
				integer();
				}
				break;
			case IDENTIFIER:
				{
				setState(62);
				variable();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(73);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,4,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(71);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
					case 1:
						{
						_localctx = new EContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_e);
						setState(65);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(66);
						match(OPERATOR_MD);
						setState(67);
						e(5);
						}
						break;
					case 2:
						{
						_localctx = new EContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_e);
						setState(68);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(69);
						match(OPERATOR_AS);
						setState(70);
						e(4);
						}
						break;
					}
					} 
				}
				setState(75);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,4,_ctx);
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

	public static class Prio_eContext extends ParserRuleContext {
		public EContext e() {
			return getRuleContext(EContext.class,0);
		}
		public Prio_eContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_prio_e; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof JurjenLangListener ) ((JurjenLangListener)listener).enterPrio_e(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof JurjenLangListener ) ((JurjenLangListener)listener).exitPrio_e(this);
		}
	}

	public final Prio_eContext prio_e() throws RecognitionException {
		Prio_eContext _localctx = new Prio_eContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_prio_e);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(76);
			match(T__3);
			setState(77);
			e(0);
			setState(78);
			match(T__4);
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

	public static class VariableContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(JurjenLangParser.IDENTIFIER, 0); }
		public VariableContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variable; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof JurjenLangListener ) ((JurjenLangListener)listener).enterVariable(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof JurjenLangListener ) ((JurjenLangListener)listener).exitVariable(this);
		}
	}

	public final VariableContext variable() throws RecognitionException {
		VariableContext _localctx = new VariableContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_variable);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(80);
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

	public static class IntegerContext extends ParserRuleContext {
		public TerminalNode NUMBERS() { return getToken(JurjenLangParser.NUMBERS, 0); }
		public IntegerContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_integer; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof JurjenLangListener ) ((JurjenLangListener)listener).enterInteger(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof JurjenLangListener ) ((JurjenLangListener)listener).exitInteger(this);
		}
	}

	public final IntegerContext integer() throws RecognitionException {
		IntegerContext _localctx = new IntegerContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_integer);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(82);
			match(NUMBERS);
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

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 9:
			return e_sempred((EContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean e_sempred(EContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 4);
		case 1:
			return precpred(_ctx, 3);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\16W\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4"+
		"\f\t\f\4\r\t\r\4\16\t\16\3\2\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3"+
		"\5\3\6\3\6\3\6\5\6,\n\6\3\6\3\6\3\7\7\7\61\n\7\f\7\16\7\64\13\7\3\b\3"+
		"\b\3\t\3\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\5\13B\n\13\3\13\3\13\3"+
		"\13\3\13\3\13\3\13\7\13J\n\13\f\13\16\13M\13\13\3\f\3\f\3\f\3\f\3\r\3"+
		"\r\3\16\3\16\3\16\2\3\24\17\2\4\6\b\n\f\16\20\22\24\26\30\32\2\2\2O\2"+
		"\34\3\2\2\2\4\37\3\2\2\2\6\"\3\2\2\2\b%\3\2\2\2\n(\3\2\2\2\f\62\3\2\2"+
		"\2\16\65\3\2\2\2\20\67\3\2\2\2\229\3\2\2\2\24A\3\2\2\2\26N\3\2\2\2\30"+
		"R\3\2\2\2\32T\3\2\2\2\34\35\5\4\3\2\35\36\7\2\2\3\36\3\3\2\2\2\37 \5\6"+
		"\4\2 !\5\n\6\2!\5\3\2\2\2\"#\7\b\2\2#$\7\13\2\2$\7\3\2\2\2%&\7\t\2\2&"+
		"\'\5\20\t\2\'\t\3\2\2\2()\7\3\2\2)+\5\f\7\2*,\5\b\5\2+*\3\2\2\2+,\3\2"+
		"\2\2,-\3\2\2\2-.\7\4\2\2.\13\3\2\2\2/\61\5\16\b\2\60/\3\2\2\2\61\64\3"+
		"\2\2\2\62\60\3\2\2\2\62\63\3\2\2\2\63\r\3\2\2\2\64\62\3\2\2\2\65\66\5"+
		"\22\n\2\66\17\3\2\2\2\678\5\24\13\28\21\3\2\2\29:\5\30\r\2:;\7\5\2\2;"+
		"<\5\24\13\2<\23\3\2\2\2=>\b\13\1\2>B\5\26\f\2?B\5\32\16\2@B\5\30\r\2A"+
		"=\3\2\2\2A?\3\2\2\2A@\3\2\2\2BK\3\2\2\2CD\f\6\2\2DE\7\f\2\2EJ\5\24\13"+
		"\7FG\f\5\2\2GH\7\r\2\2HJ\5\24\13\6IC\3\2\2\2IF\3\2\2\2JM\3\2\2\2KI\3\2"+
		"\2\2KL\3\2\2\2L\25\3\2\2\2MK\3\2\2\2NO\7\6\2\2OP\5\24\13\2PQ\7\7\2\2Q"+
		"\27\3\2\2\2RS\7\13\2\2S\31\3\2\2\2TU\7\n\2\2U\33\3\2\2\2\7+\62AIK";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}