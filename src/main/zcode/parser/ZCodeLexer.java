// Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class ZCodeLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		NUM_KEYWORD=1, BOOL_KEYWORD=2, STRING_KEYWORD=3, RETURN_KEYWORD=4, VAR_KEYWORD=5, 
		DYNAMIC_KEYWORD=6, FUNC_KEYWORD=7, FOR_KEYWORD=8, UNTIL_KEYWORD=9, BY_KEYWORD=10, 
		BREAK_KEYWORD=11, CONTINUE_KEYWORD=12, IF_KEYWORD=13, ELSE_KEYWORD=14, 
		ELIF_KEYWORD=15, BEGIN_KEYWORD=16, END_KEYWORD=17, ASSIGN_OP=18, ADD_OP=19, 
		SUB_OP=20, MUL_OP=21, DIV_OP=22, MOD_OP=23, NOT_OP=24, AND_OP=25, OR_OP=26, 
		EQUAL_OP=27, INEQUAL_OP=28, LESS_OP=29, LESSEQUAL_OP=30, LARGE_OP=31, 
		LARGEEQUAL_OP=32, CONCAT_OP=33, EQUAL_STR_OP=34, ID=35, LEFT_PARENTHESIS=36, 
		RIGHT_PARENTHESIS=37, LEFT_BRACKET=38, RIGHT_BRACKET=39, SEPARATOR_KEYWORD=40, 
		BOOL_LIT=41, REAL_LIT=42, NL1=43, NL2=44, NL3=45, NL4=46, WS=47, COMMENT_LINE=48, 
		UNCLOSE_STRING=49, STRING_LIT=50, NEWLINE_STRING=51, ILLEGAL_ESCAPE=52, 
		ERROR_TOKEN=53;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"NUM_KEYWORD", "BOOL_KEYWORD", "STRING_KEYWORD", "RETURN_KEYWORD", "VAR_KEYWORD", 
			"DYNAMIC_KEYWORD", "FUNC_KEYWORD", "FOR_KEYWORD", "UNTIL_KEYWORD", "BY_KEYWORD", 
			"BREAK_KEYWORD", "CONTINUE_KEYWORD", "IF_KEYWORD", "ELSE_KEYWORD", "ELIF_KEYWORD", 
			"BEGIN_KEYWORD", "END_KEYWORD", "ASSIGN_OP", "ADD_OP", "SUB_OP", "MUL_OP", 
			"DIV_OP", "MOD_OP", "NOT_OP", "AND_OP", "OR_OP", "EQUAL_OP", "INEQUAL_OP", 
			"LESS_OP", "LESSEQUAL_OP", "LARGE_OP", "LARGEEQUAL_OP", "CONCAT_OP", 
			"EQUAL_STR_OP", "ID", "LEFT_PARENTHESIS", "RIGHT_PARENTHESIS", "LEFT_BRACKET", 
			"RIGHT_BRACKET", "SEPARATOR_KEYWORD", "BOOL_LIT", "REAL_LIT", "INTPART", 
			"DECPART", "EXPPART", "NL1", "NL2", "NL3", "NL4", "WS", "COMMENT_LINE", 
			"UNCLOSE_STRING", "STRING_LIT", "NEWLINE_STRING", "ILLEGAL_ESCAPE", "ERROR_TOKEN"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'number'", "'bool'", "'string'", "'return'", "'var'", "'dynamic'", 
			"'func'", "'for'", "'until'", "'by'", "'break'", "'continue'", "'if'", 
			"'else'", "'elif'", "'begin'", "'end'", "'<-'", "'+'", "'-'", "'*'", 
			"'/'", "'%'", "'not'", "'and'", "'or'", "'='", "'!='", "'<'", "'<='", 
			"'>'", "'>='", "'...'", "'=='", null, "'('", "')'", "'['", "']'", "','", 
			null, null, "'\r\r\n'", "'\r'", "'\r\n'", "'\n'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "NUM_KEYWORD", "BOOL_KEYWORD", "STRING_KEYWORD", "RETURN_KEYWORD", 
			"VAR_KEYWORD", "DYNAMIC_KEYWORD", "FUNC_KEYWORD", "FOR_KEYWORD", "UNTIL_KEYWORD", 
			"BY_KEYWORD", "BREAK_KEYWORD", "CONTINUE_KEYWORD", "IF_KEYWORD", "ELSE_KEYWORD", 
			"ELIF_KEYWORD", "BEGIN_KEYWORD", "END_KEYWORD", "ASSIGN_OP", "ADD_OP", 
			"SUB_OP", "MUL_OP", "DIV_OP", "MOD_OP", "NOT_OP", "AND_OP", "OR_OP", 
			"EQUAL_OP", "INEQUAL_OP", "LESS_OP", "LESSEQUAL_OP", "LARGE_OP", "LARGEEQUAL_OP", 
			"CONCAT_OP", "EQUAL_STR_OP", "ID", "LEFT_PARENTHESIS", "RIGHT_PARENTHESIS", 
			"LEFT_BRACKET", "RIGHT_BRACKET", "SEPARATOR_KEYWORD", "BOOL_LIT", "REAL_LIT", 
			"NL1", "NL2", "NL3", "NL4", "WS", "COMMENT_LINE", "UNCLOSE_STRING", "STRING_LIT", 
			"NEWLINE_STRING", "ILLEGAL_ESCAPE", "ERROR_TOKEN"
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


	public ZCodeLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "ZCode.g4"; }

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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\67\u019d\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22"+
		"\t\22\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31"+
		"\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t"+
		" \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t"+
		"+\4,\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64"+
		"\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\3\2\3\2\3\2\3\2\3\2\3"+
		"\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5"+
		"\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3"+
		"\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\f"+
		"\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16"+
		"\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21"+
		"\3\21\3\21\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\25\3\25\3\26"+
		"\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\33"+
		"\3\33\3\33\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\37\3\37\3\37\3 \3 \3!"+
		"\3!\3!\3\"\3\"\3\"\3\"\3#\3#\3#\3$\6$\u0101\n$\r$\16$\u0102\3$\7$\u0106"+
		"\n$\f$\16$\u0109\13$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3*\3*\3*\3"+
		"*\3*\3*\3*\5*\u011e\n*\3+\3+\3+\3+\3+\3+\5+\u0126\n+\3+\3+\5+\u012a\n"+
		"+\3,\6,\u012d\n,\r,\16,\u012e\3-\3-\7-\u0133\n-\f-\16-\u0136\13-\3.\3"+
		".\5.\u013a\n.\3.\6.\u013d\n.\r.\16.\u013e\3/\3/\3/\3/\3\60\3\60\3\61\3"+
		"\61\3\61\3\62\3\62\3\63\6\63\u014d\n\63\r\63\16\63\u014e\3\63\3\63\3\64"+
		"\3\64\3\64\3\64\7\64\u0157\n\64\f\64\16\64\u015a\13\64\3\64\3\64\3\65"+
		"\3\65\3\65\3\65\3\65\3\65\5\65\u0164\n\65\7\65\u0166\n\65\f\65\16\65\u0169"+
		"\13\65\3\66\3\66\3\66\3\66\3\66\3\66\5\66\u0171\n\66\7\66\u0173\n\66\f"+
		"\66\16\66\u0176\13\66\3\66\3\66\3\67\3\67\3\67\3\67\3\67\3\67\5\67\u0180"+
		"\n\67\7\67\u0182\n\67\f\67\16\67\u0185\13\67\3\67\3\67\3\67\5\67\u018a"+
		"\n\67\38\38\38\38\58\u0190\n8\38\38\78\u0194\n8\f8\168\u0197\138\38\3"+
		"8\38\39\39\4\u0183\u0195\2:\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25"+
		"\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32"+
		"\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W\2Y\2[\2]-_.a/"+
		"c\60e\61g\62i\63k\64m\65o\66q\67\3\2\r\5\2C\\aac|\6\2\62;C\\aac|\3\2\62"+
		";\3\2\60\60\4\2GGgg\4\2--//\5\2\n\13\16\16\"\"\4\2\f\f\17\17\7\2\f\f\17"+
		"\17$$))^^\t\2))^^ddhhppttvv\3\2$$\2\u01b6\2\3\3\2\2\2\2\5\3\2\2\2\2\7"+
		"\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2"+
		"\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2"+
		"\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2"+
		"\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2"+
		"\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2"+
		"\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M"+
		"\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2]\3\2\2\2\2_\3\2"+
		"\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2"+
		"\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\3s\3\2\2\2\5z\3\2\2\2\7\177\3\2\2\2"+
		"\t\u0086\3\2\2\2\13\u008d\3\2\2\2\r\u0091\3\2\2\2\17\u0099\3\2\2\2\21"+
		"\u009e\3\2\2\2\23\u00a2\3\2\2\2\25\u00a8\3\2\2\2\27\u00ab\3\2\2\2\31\u00b1"+
		"\3\2\2\2\33\u00ba\3\2\2\2\35\u00bd\3\2\2\2\37\u00c2\3\2\2\2!\u00c7\3\2"+
		"\2\2#\u00cd\3\2\2\2%\u00d1\3\2\2\2\'\u00d4\3\2\2\2)\u00d6\3\2\2\2+\u00d8"+
		"\3\2\2\2-\u00da\3\2\2\2/\u00dc\3\2\2\2\61\u00de\3\2\2\2\63\u00e2\3\2\2"+
		"\2\65\u00e6\3\2\2\2\67\u00e9\3\2\2\29\u00eb\3\2\2\2;\u00ee\3\2\2\2=\u00f0"+
		"\3\2\2\2?\u00f3\3\2\2\2A\u00f5\3\2\2\2C\u00f8\3\2\2\2E\u00fc\3\2\2\2G"+
		"\u0100\3\2\2\2I\u010a\3\2\2\2K\u010c\3\2\2\2M\u010e\3\2\2\2O\u0110\3\2"+
		"\2\2Q\u0112\3\2\2\2S\u011d\3\2\2\2U\u0129\3\2\2\2W\u012c\3\2\2\2Y\u0130"+
		"\3\2\2\2[\u0137\3\2\2\2]\u0140\3\2\2\2_\u0144\3\2\2\2a\u0146\3\2\2\2c"+
		"\u0149\3\2\2\2e\u014c\3\2\2\2g\u0152\3\2\2\2i\u015d\3\2\2\2k\u016a\3\2"+
		"\2\2m\u0179\3\2\2\2o\u018b\3\2\2\2q\u019b\3\2\2\2st\7p\2\2tu\7w\2\2uv"+
		"\7o\2\2vw\7d\2\2wx\7g\2\2xy\7t\2\2y\4\3\2\2\2z{\7d\2\2{|\7q\2\2|}\7q\2"+
		"\2}~\7n\2\2~\6\3\2\2\2\177\u0080\7u\2\2\u0080\u0081\7v\2\2\u0081\u0082"+
		"\7t\2\2\u0082\u0083\7k\2\2\u0083\u0084\7p\2\2\u0084\u0085\7i\2\2\u0085"+
		"\b\3\2\2\2\u0086\u0087\7t\2\2\u0087\u0088\7g\2\2\u0088\u0089\7v\2\2\u0089"+
		"\u008a\7w\2\2\u008a\u008b\7t\2\2\u008b\u008c\7p\2\2\u008c\n\3\2\2\2\u008d"+
		"\u008e\7x\2\2\u008e\u008f\7c\2\2\u008f\u0090\7t\2\2\u0090\f\3\2\2\2\u0091"+
		"\u0092\7f\2\2\u0092\u0093\7{\2\2\u0093\u0094\7p\2\2\u0094\u0095\7c\2\2"+
		"\u0095\u0096\7o\2\2\u0096\u0097\7k\2\2\u0097\u0098\7e\2\2\u0098\16\3\2"+
		"\2\2\u0099\u009a\7h\2\2\u009a\u009b\7w\2\2\u009b\u009c\7p\2\2\u009c\u009d"+
		"\7e\2\2\u009d\20\3\2\2\2\u009e\u009f\7h\2\2\u009f\u00a0\7q\2\2\u00a0\u00a1"+
		"\7t\2\2\u00a1\22\3\2\2\2\u00a2\u00a3\7w\2\2\u00a3\u00a4\7p\2\2\u00a4\u00a5"+
		"\7v\2\2\u00a5\u00a6\7k\2\2\u00a6\u00a7\7n\2\2\u00a7\24\3\2\2\2\u00a8\u00a9"+
		"\7d\2\2\u00a9\u00aa\7{\2\2\u00aa\26\3\2\2\2\u00ab\u00ac\7d\2\2\u00ac\u00ad"+
		"\7t\2\2\u00ad\u00ae\7g\2\2\u00ae\u00af\7c\2\2\u00af\u00b0\7m\2\2\u00b0"+
		"\30\3\2\2\2\u00b1\u00b2\7e\2\2\u00b2\u00b3\7q\2\2\u00b3\u00b4\7p\2\2\u00b4"+
		"\u00b5\7v\2\2\u00b5\u00b6\7k\2\2\u00b6\u00b7\7p\2\2\u00b7\u00b8\7w\2\2"+
		"\u00b8\u00b9\7g\2\2\u00b9\32\3\2\2\2\u00ba\u00bb\7k\2\2\u00bb\u00bc\7"+
		"h\2\2\u00bc\34\3\2\2\2\u00bd\u00be\7g\2\2\u00be\u00bf\7n\2\2\u00bf\u00c0"+
		"\7u\2\2\u00c0\u00c1\7g\2\2\u00c1\36\3\2\2\2\u00c2\u00c3\7g\2\2\u00c3\u00c4"+
		"\7n\2\2\u00c4\u00c5\7k\2\2\u00c5\u00c6\7h\2\2\u00c6 \3\2\2\2\u00c7\u00c8"+
		"\7d\2\2\u00c8\u00c9\7g\2\2\u00c9\u00ca\7i\2\2\u00ca\u00cb\7k\2\2\u00cb"+
		"\u00cc\7p\2\2\u00cc\"\3\2\2\2\u00cd\u00ce\7g\2\2\u00ce\u00cf\7p\2\2\u00cf"+
		"\u00d0\7f\2\2\u00d0$\3\2\2\2\u00d1\u00d2\7>\2\2\u00d2\u00d3\7/\2\2\u00d3"+
		"&\3\2\2\2\u00d4\u00d5\7-\2\2\u00d5(\3\2\2\2\u00d6\u00d7\7/\2\2\u00d7*"+
		"\3\2\2\2\u00d8\u00d9\7,\2\2\u00d9,\3\2\2\2\u00da\u00db\7\61\2\2\u00db"+
		".\3\2\2\2\u00dc\u00dd\7\'\2\2\u00dd\60\3\2\2\2\u00de\u00df\7p\2\2\u00df"+
		"\u00e0\7q\2\2\u00e0\u00e1\7v\2\2\u00e1\62\3\2\2\2\u00e2\u00e3\7c\2\2\u00e3"+
		"\u00e4\7p\2\2\u00e4\u00e5\7f\2\2\u00e5\64\3\2\2\2\u00e6\u00e7\7q\2\2\u00e7"+
		"\u00e8\7t\2\2\u00e8\66\3\2\2\2\u00e9\u00ea\7?\2\2\u00ea8\3\2\2\2\u00eb"+
		"\u00ec\7#\2\2\u00ec\u00ed\7?\2\2\u00ed:\3\2\2\2\u00ee\u00ef\7>\2\2\u00ef"+
		"<\3\2\2\2\u00f0\u00f1\7>\2\2\u00f1\u00f2\7?\2\2\u00f2>\3\2\2\2\u00f3\u00f4"+
		"\7@\2\2\u00f4@\3\2\2\2\u00f5\u00f6\7@\2\2\u00f6\u00f7\7?\2\2\u00f7B\3"+
		"\2\2\2\u00f8\u00f9\7\60\2\2\u00f9\u00fa\7\60\2\2\u00fa\u00fb\7\60\2\2"+
		"\u00fbD\3\2\2\2\u00fc\u00fd\7?\2\2\u00fd\u00fe\7?\2\2\u00feF\3\2\2\2\u00ff"+
		"\u0101\t\2\2\2\u0100\u00ff\3\2\2\2\u0101\u0102\3\2\2\2\u0102\u0100\3\2"+
		"\2\2\u0102\u0103\3\2\2\2\u0103\u0107\3\2\2\2\u0104\u0106\t\3\2\2\u0105"+
		"\u0104\3\2\2\2\u0106\u0109\3\2\2\2\u0107\u0105\3\2\2\2\u0107\u0108\3\2"+
		"\2\2\u0108H\3\2\2\2\u0109\u0107\3\2\2\2\u010a\u010b\7*\2\2\u010bJ\3\2"+
		"\2\2\u010c\u010d\7+\2\2\u010dL\3\2\2\2\u010e\u010f\7]\2\2\u010fN\3\2\2"+
		"\2\u0110\u0111\7_\2\2\u0111P\3\2\2\2\u0112\u0113\7.\2\2\u0113R\3\2\2\2"+
		"\u0114\u0115\7v\2\2\u0115\u0116\7t\2\2\u0116\u0117\7w\2\2\u0117\u011e"+
		"\7g\2\2\u0118\u0119\7h\2\2\u0119\u011a\7c\2\2\u011a\u011b\7n\2\2\u011b"+
		"\u011c\7u\2\2\u011c\u011e\7g\2\2\u011d\u0114\3\2\2\2\u011d\u0118\3\2\2"+
		"\2\u011eT\3\2\2\2\u011f\u012a\5W,\2\u0120\u0121\5W,\2\u0121\u0122\5Y-"+
		"\2\u0122\u012a\3\2\2\2\u0123\u0125\5W,\2\u0124\u0126\5Y-\2\u0125\u0124"+
		"\3\2\2\2\u0125\u0126\3\2\2\2\u0126\u0127\3\2\2\2\u0127\u0128\5[.\2\u0128"+
		"\u012a\3\2\2\2\u0129\u011f\3\2\2\2\u0129\u0120\3\2\2\2\u0129\u0123\3\2"+
		"\2\2\u012aV\3\2\2\2\u012b\u012d\t\4\2\2\u012c\u012b\3\2\2\2\u012d\u012e"+
		"\3\2\2\2\u012e\u012c\3\2\2\2\u012e\u012f\3\2\2\2\u012fX\3\2\2\2\u0130"+
		"\u0134\t\5\2\2\u0131\u0133\t\4\2\2\u0132\u0131\3\2\2\2\u0133\u0136\3\2"+
		"\2\2\u0134\u0132\3\2\2\2\u0134\u0135\3\2\2\2\u0135Z\3\2\2\2\u0136\u0134"+
		"\3\2\2\2\u0137\u0139\t\6\2\2\u0138\u013a\t\7\2\2\u0139\u0138\3\2\2\2\u0139"+
		"\u013a\3\2\2\2\u013a\u013c\3\2\2\2\u013b\u013d\t\4\2\2\u013c\u013b\3\2"+
		"\2\2\u013d\u013e\3\2\2\2\u013e\u013c\3\2\2\2\u013e\u013f\3\2\2\2\u013f"+
		"\\\3\2\2\2\u0140\u0141\7\17\2\2\u0141\u0142\7\17\2\2\u0142\u0143\7\f\2"+
		"\2\u0143^\3\2\2\2\u0144\u0145\7\17\2\2\u0145`\3\2\2\2\u0146\u0147\7\17"+
		"\2\2\u0147\u0148\7\f\2\2\u0148b\3\2\2\2\u0149\u014a\7\f\2\2\u014ad\3\2"+
		"\2\2\u014b\u014d\t\b\2\2\u014c\u014b\3\2\2\2\u014d\u014e\3\2\2\2\u014e"+
		"\u014c\3\2\2\2\u014e\u014f\3\2\2\2\u014f\u0150\3\2\2\2\u0150\u0151\b\63"+
		"\2\2\u0151f\3\2\2\2\u0152\u0153\7%\2\2\u0153\u0154\7%\2\2\u0154\u0158"+
		"\3\2\2\2\u0155\u0157\n\t\2\2\u0156\u0155\3\2\2\2\u0157\u015a\3\2\2\2\u0158"+
		"\u0156\3\2\2\2\u0158\u0159\3\2\2\2\u0159\u015b\3\2\2\2\u015a\u0158\3\2"+
		"\2\2\u015b\u015c\b\64\2\2\u015ch\3\2\2\2\u015d\u0167\7$\2\2\u015e\u0166"+
		"\n\n\2\2\u015f\u0160\7^\2\2\u0160\u0166\t\13\2\2\u0161\u0163\7)\2\2\u0162"+
		"\u0164\t\f\2\2\u0163\u0162\3\2\2\2\u0163\u0164\3\2\2\2\u0164\u0166\3\2"+
		"\2\2\u0165\u015e\3\2\2\2\u0165\u015f\3\2\2\2\u0165\u0161\3\2\2\2\u0166"+
		"\u0169\3\2\2\2\u0167\u0165\3\2\2\2\u0167\u0168\3\2\2\2\u0168j\3\2\2\2"+
		"\u0169\u0167\3\2\2\2\u016a\u0174\7$\2\2\u016b\u0173\n\n\2\2\u016c\u016d"+
		"\7^\2\2\u016d\u0173\t\13\2\2\u016e\u0170\7)\2\2\u016f\u0171\t\f\2\2\u0170"+
		"\u016f\3\2\2\2\u0170\u0171\3\2\2\2\u0171\u0173\3\2\2\2\u0172\u016b\3\2"+
		"\2\2\u0172\u016c\3\2\2\2\u0172\u016e\3\2\2\2\u0173\u0176\3\2\2\2\u0174"+
		"\u0172\3\2\2\2\u0174\u0175\3\2\2\2\u0175\u0177\3\2\2\2\u0176\u0174\3\2"+
		"\2\2\u0177\u0178\7$\2\2\u0178l\3\2\2\2\u0179\u0183\7$\2\2\u017a\u0182"+
		"\n\n\2\2\u017b\u017c\7^\2\2\u017c\u0182\t\13\2\2\u017d\u017f\7)\2\2\u017e"+
		"\u0180\t\f\2\2\u017f\u017e\3\2\2\2\u017f\u0180\3\2\2\2\u0180\u0182\3\2"+
		"\2\2\u0181\u017a\3\2\2\2\u0181\u017b\3\2\2\2\u0181\u017d\3\2\2\2\u0182"+
		"\u0185\3\2\2\2\u0183\u0184\3\2\2\2\u0183\u0181\3\2\2\2\u0184\u0189\3\2"+
		"\2\2\u0185\u0183\3\2\2\2\u0186\u0187\7\17\2\2\u0187\u018a\7\f\2\2\u0188"+
		"\u018a\t\t\2\2\u0189\u0186\3\2\2\2\u0189\u0188\3\2\2\2\u018an\3\2\2\2"+
		"\u018b\u0195\7$\2\2\u018c\u0194\n\n\2\2\u018d\u018f\7)\2\2\u018e\u0190"+
		"\t\f\2\2\u018f\u018e\3\2\2\2\u018f\u0190\3\2\2\2\u0190\u0194\3\2\2\2\u0191"+
		"\u0192\7^\2\2\u0192\u0194\t\13\2\2\u0193\u018c\3\2\2\2\u0193\u018d\3\2"+
		"\2\2\u0193\u0191\3\2\2\2\u0194\u0197\3\2\2\2\u0195\u0196\3\2\2\2\u0195"+
		"\u0193\3\2\2\2\u0196\u0198\3\2\2\2\u0197\u0195\3\2\2\2\u0198\u0199\7^"+
		"\2\2\u0199\u019a\n\13\2\2\u019ap\3\2\2\2\u019b\u019c\13\2\2\2\u019cr\3"+
		"\2\2\2\33\2\u0102\u0107\u011d\u0125\u0129\u012e\u0134\u0139\u013e\u014e"+
		"\u0158\u0163\u0165\u0167\u0170\u0172\u0174\u017f\u0181\u0183\u0189\u018f"+
		"\u0193\u0195\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}