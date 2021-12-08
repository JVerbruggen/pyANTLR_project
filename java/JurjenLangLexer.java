// Generated from JurjenLang.g4 by ANTLR 4.9.3
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class JurjenLangLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.9.3", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, FUNC_KW=6, FUNC_RET=7, NUMBERS=8, 
		IDENTIFIER=9, OPERATOR_MD=10, OPERATOR_AS=11, WS=12;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "FUNC_KW", "FUNC_RET", "NUMBERS", 
			"IDENTIFIER", "OPERATOR_MD", "OPERATOR_AS", "WS", "DIGIT", "BIT"
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


	public JurjenLangLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "JurjenLang.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\16P\b\1\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3"+
		"\5\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\6\t\67"+
		"\n\t\r\t\16\t8\3\n\3\n\7\n=\n\n\f\n\16\n@\13\n\3\13\3\13\3\f\3\f\3\r\6"+
		"\rG\n\r\r\r\16\rH\3\r\3\r\3\16\3\16\3\17\3\17\2\2\20\3\3\5\4\7\5\t\6\13"+
		"\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\2\35\2\3\2\7\4\2C\\c|\6\2\62"+
		";C\\aac|\4\2,,\61\61\4\2--//\5\2\13\f\17\17\"\"\2P\2\3\3\2\2\2\2\5\3\2"+
		"\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21"+
		"\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\3\37\3\2"+
		"\2\2\5!\3\2\2\2\7#\3\2\2\2\t%\3\2\2\2\13\'\3\2\2\2\r)\3\2\2\2\17.\3\2"+
		"\2\2\21\66\3\2\2\2\23:\3\2\2\2\25A\3\2\2\2\27C\3\2\2\2\31F\3\2\2\2\33"+
		"L\3\2\2\2\35N\3\2\2\2\37 \7}\2\2 \4\3\2\2\2!\"\7\177\2\2\"\6\3\2\2\2#"+
		"$\7?\2\2$\b\3\2\2\2%&\7*\2\2&\n\3\2\2\2\'(\7+\2\2(\f\3\2\2\2)*\7h\2\2"+
		"*+\7w\2\2+,\7p\2\2,-\7e\2\2-\16\3\2\2\2./\7t\2\2/\60\7g\2\2\60\61\7v\2"+
		"\2\61\62\7w\2\2\62\63\7t\2\2\63\64\7p\2\2\64\20\3\2\2\2\65\67\5\33\16"+
		"\2\66\65\3\2\2\2\678\3\2\2\28\66\3\2\2\289\3\2\2\29\22\3\2\2\2:>\t\2\2"+
		"\2;=\t\3\2\2<;\3\2\2\2=@\3\2\2\2><\3\2\2\2>?\3\2\2\2?\24\3\2\2\2@>\3\2"+
		"\2\2AB\t\4\2\2B\26\3\2\2\2CD\t\5\2\2D\30\3\2\2\2EG\t\6\2\2FE\3\2\2\2G"+
		"H\3\2\2\2HF\3\2\2\2HI\3\2\2\2IJ\3\2\2\2JK\b\r\2\2K\32\3\2\2\2LM\4\62;"+
		"\2M\34\3\2\2\2NO\4\62\63\2O\36\3\2\2\2\6\28>H\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}