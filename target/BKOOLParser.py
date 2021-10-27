# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3?")
        buf.write("\u01f9\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\3\2\3\2\3\2\3\3\3\3\5\3r\n\3\3\4")
        buf.write("\3\4\5\4v\n\4\3\5\3\5\3\5\3\5\5\5|\n\5\3\5\3\5\3\5\3\5")
        buf.write("\3\6\3\6\3\6\3\7\3\7\3\7\3\7\5\7\u0089\n\7\3\b\3\b\3\b")
        buf.write("\3\b\5\b\u008f\n\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\5\t\u009a\n\t\3\n\5\n\u009d\n\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\5\13\u00a4\n\13\3\f\3\f\3\f\5\f\u00a9\n\f\3\r\3\r\3\r")
        buf.write("\5\r\u00ae\n\r\3\16\3\16\3\16\5\16\u00b3\n\16\3\17\3\17")
        buf.write("\3\17\3\17\3\17\5\17\u00ba\n\17\3\17\3\17\3\17\3\17\5")
        buf.write("\17\u00c0\n\17\3\17\3\17\3\17\5\17\u00c5\n\17\3\17\3\17")
        buf.write("\5\17\u00c9\n\17\3\20\3\20\3\20\3\20\3\20\5\20\u00d0\n")
        buf.write("\20\3\21\3\21\3\21\3\22\3\22\3\22\3\22\5\22\u00d9\n\22")
        buf.write("\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\5\24\u00e3\n")
        buf.write("\24\3\25\3\25\3\25\5\25\u00e8\n\25\3\25\5\25\u00eb\n\25")
        buf.write("\3\26\3\26\3\26\5\26\u00f0\n\26\3\26\5\26\u00f3\n\26\3")
        buf.write("\27\3\27\3\27\5\27\u00f8\n\27\3\27\5\27\u00fb\n\27\3\30")
        buf.write("\3\30\3\30\5\30\u0100\n\30\3\30\5\30\u0103\n\30\3\31\3")
        buf.write("\31\3\32\3\32\5\32\u0109\n\32\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\5\34\u0121\n\34\3\35\3")
        buf.write("\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\5\35\u012c\n\35")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\7\36\u0137")
        buf.write("\n\36\f\36\16\36\u013a\13\36\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\7\37\u0145\n\37\f\37\16\37\u0148")
        buf.write("\13\37\3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \7")
        buf.write(" \u0159\n \f \16 \u015c\13 \3!\3!\3!\3!\3!\3!\7!\u0164")
        buf.write("\n!\f!\16!\u0167\13!\3\"\3\"\3\"\5\"\u016c\n\"\3#\3#\3")
        buf.write("#\3#\3#\5#\u0173\n#\3$\3$\3$\3$\3$\3$\3$\3$\7$\u017d\n")
        buf.write("$\f$\16$\u0180\13$\3%\3%\3%\3%\3%\3%\3%\5%\u0189\n%\7")
        buf.write("%\u018b\n%\f%\16%\u018e\13%\3&\3&\3&\3&\5&\u0194\n&\3")
        buf.write("\'\3\'\3\'\3\'\3\'\3\'\3\'\5\'\u019d\n\'\3(\3(\3(\3(\3")
        buf.write("(\5(\u01a4\n(\3)\3)\5)\u01a8\n)\3)\3)\3*\3*\3*\3*\3*\5")
        buf.write("*\u01b1\n*\3+\3+\3+\3+\3+\3+\3+\5+\u01ba\n+\3,\3,\3,\3")
        buf.write(",\5,\u01c0\n,\3-\3-\3-\3-\5-\u01c6\n-\3.\3.\3.\3.\3.\3")
        buf.write("/\3/\5/\u01cf\n/\3\60\3\60\3\60\3\60\3\60\3\60\3\61\3")
        buf.write("\61\3\61\3\61\3\61\3\61\5\61\u01dd\n\61\3\62\3\62\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\64")
        buf.write("\3\64\3\64\3\65\3\65\3\65\3\65\3\66\3\66\3\66\3\66\3\66")
        buf.write("\3\66\3\66\2\b:<>@FH\67\2\4\6\b\n\f\16\20\22\24\26\30")
        buf.write("\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`b")
        buf.write("dfhj\2\4\6\2\t\t\20\20\22\22\24\24\3\2\37 \2\u0209\2l")
        buf.write("\3\2\2\2\4o\3\2\2\2\6u\3\2\2\2\bw\3\2\2\2\n\u0081\3\2")
        buf.write("\2\2\f\u0088\3\2\2\2\16\u008e\3\2\2\2\20\u0099\3\2\2\2")
        buf.write("\22\u009c\3\2\2\2\24\u00a0\3\2\2\2\26\u00a5\3\2\2\2\30")
        buf.write("\u00aa\3\2\2\2\32\u00af\3\2\2\2\34\u00c8\3\2\2\2\36\u00cf")
        buf.write("\3\2\2\2 \u00d1\3\2\2\2\"\u00d8\3\2\2\2$\u00da\3\2\2\2")
        buf.write("&\u00e2\3\2\2\2(\u00ea\3\2\2\2*\u00f2\3\2\2\2,\u00fa\3")
        buf.write("\2\2\2.\u0102\3\2\2\2\60\u0104\3\2\2\2\62\u0108\3\2\2")
        buf.write("\2\64\u010a\3\2\2\2\66\u0120\3\2\2\28\u012b\3\2\2\2:\u012d")
        buf.write("\3\2\2\2<\u013b\3\2\2\2>\u0149\3\2\2\2@\u015d\3\2\2\2")
        buf.write("B\u016b\3\2\2\2D\u0172\3\2\2\2F\u0174\3\2\2\2H\u0181\3")
        buf.write("\2\2\2J\u0193\3\2\2\2L\u019c\3\2\2\2N\u01a3\3\2\2\2P\u01a5")
        buf.write("\3\2\2\2R\u01b0\3\2\2\2T\u01b9\3\2\2\2V\u01bf\3\2\2\2")
        buf.write("X\u01c5\3\2\2\2Z\u01c7\3\2\2\2\\\u01ce\3\2\2\2^\u01d0")
        buf.write("\3\2\2\2`\u01d6\3\2\2\2b\u01de\3\2\2\2d\u01e8\3\2\2\2")
        buf.write("f\u01eb\3\2\2\2h\u01ee\3\2\2\2j\u01f2\3\2\2\2lm\5\4\3")
        buf.write("\2mn\7\2\2\3n\3\3\2\2\2oq\5\b\5\2pr\5\4\3\2qp\3\2\2\2")
        buf.write("qr\3\2\2\2r\5\3\2\2\2sv\5\62\32\2tv\5\64\33\2us\3\2\2")
        buf.write("\2ut\3\2\2\2v\7\3\2\2\2wx\7\13\2\2x{\7;\2\2yz\7\17\2\2")
        buf.write("z|\7;\2\2{y\3\2\2\2{|\3\2\2\2|}\3\2\2\2}~\7:\2\2~\177")
        buf.write("\5\n\6\2\177\u0080\79\2\2\u0080\t\3\2\2\2\u0081\u0082")
        buf.write("\5\f\7\2\u0082\u0083\5\16\b\2\u0083\13\3\2\2\2\u0084\u0085")
        buf.write("\5\22\n\2\u0085\u0086\5\f\7\2\u0086\u0089\3\2\2\2\u0087")
        buf.write("\u0089\3\2\2\2\u0088\u0084\3\2\2\2\u0088\u0087\3\2\2\2")
        buf.write("\u0089\r\3\2\2\2\u008a\u008b\5\34\17\2\u008b\u008c\5\16")
        buf.write("\b\2\u008c\u008f\3\2\2\2\u008d\u008f\3\2\2\2\u008e\u008a")
        buf.write("\3\2\2\2\u008e\u008d\3\2\2\2\u008f\17\3\2\2\2\u0090\u0091")
        buf.write("\7\35\2\2\u0091\u0092\5\6\4\2\u0092\u0093\5\24\13\2\u0093")
        buf.write("\u0094\7\66\2\2\u0094\u009a\3\2\2\2\u0095\u0096\5\6\4")
        buf.write("\2\u0096\u0097\5\26\f\2\u0097\u0098\7\66\2\2\u0098\u009a")
        buf.write("\3\2\2\2\u0099\u0090\3\2\2\2\u0099\u0095\3\2\2\2\u009a")
        buf.write("\21\3\2\2\2\u009b\u009d\7\36\2\2\u009c\u009b\3\2\2\2\u009c")
        buf.write("\u009d\3\2\2\2\u009d\u009e\3\2\2\2\u009e\u009f\5\20\t")
        buf.write("\2\u009f\23\3\2\2\2\u00a0\u00a3\5\30\r\2\u00a1\u00a2\7")
        buf.write("8\2\2\u00a2\u00a4\5\24\13\2\u00a3\u00a1\3\2\2\2\u00a3")
        buf.write("\u00a4\3\2\2\2\u00a4\25\3\2\2\2\u00a5\u00a8\5\32\16\2")
        buf.write("\u00a6\u00a7\78\2\2\u00a7\u00a9\5\26\f\2\u00a8\u00a6\3")
        buf.write("\2\2\2\u00a8\u00a9\3\2\2\2\u00a9\27\3\2\2\2\u00aa\u00ad")
        buf.write("\7;\2\2\u00ab\u00ac\7\3\2\2\u00ac\u00ae\5\66\34\2\u00ad")
        buf.write("\u00ab\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae\31\3\2\2\2\u00af")
        buf.write("\u00b2\7;\2\2\u00b0\u00b1\7\3\2\2\u00b1\u00b3\5\66\34")
        buf.write("\2\u00b2\u00b0\3\2\2\2\u00b2\u00b3\3\2\2\2\u00b3\33\3")
        buf.write("\2\2\2\u00b4\u00b5\7\36\2\2\u00b5\u00b6\5\6\4\2\u00b6")
        buf.write("\u00b7\7;\2\2\u00b7\u00b9\7\64\2\2\u00b8\u00ba\5\36\20")
        buf.write("\2\u00b9\u00b8\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba\u00bb")
        buf.write("\3\2\2\2\u00bb\u00bc\7\65\2\2\u00bc\u00bd\5Z.\2\u00bd")
        buf.write("\u00c9\3\2\2\2\u00be\u00c0\5\6\4\2\u00bf\u00be\3\2\2\2")
        buf.write("\u00bf\u00c0\3\2\2\2\u00c0\u00c1\3\2\2\2\u00c1\u00c2\7")
        buf.write(";\2\2\u00c2\u00c4\7\64\2\2\u00c3\u00c5\5\36\20\2\u00c4")
        buf.write("\u00c3\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5\u00c6\3\2\2\2")
        buf.write("\u00c6\u00c7\7\65\2\2\u00c7\u00c9\5Z.\2\u00c8\u00b4\3")
        buf.write("\2\2\2\u00c8\u00bf\3\2\2\2\u00c9\35\3\2\2\2\u00ca\u00cb")
        buf.write("\5 \21\2\u00cb\u00cc\7\66\2\2\u00cc\u00cd\5\36\20\2\u00cd")
        buf.write("\u00d0\3\2\2\2\u00ce\u00d0\5 \21\2\u00cf\u00ca\3\2\2\2")
        buf.write("\u00cf\u00ce\3\2\2\2\u00d0\37\3\2\2\2\u00d1\u00d2\5\6")
        buf.write("\4\2\u00d2\u00d3\5\"\22\2\u00d3!\3\2\2\2\u00d4\u00d5\7")
        buf.write(";\2\2\u00d5\u00d6\78\2\2\u00d6\u00d9\5\"\22\2\u00d7\u00d9")
        buf.write("\7;\2\2\u00d8\u00d4\3\2\2\2\u00d8\u00d7\3\2\2\2\u00d9")
        buf.write("#\3\2\2\2\u00da\u00db\7:\2\2\u00db\u00dc\5&\24\2\u00dc")
        buf.write("\u00dd\79\2\2\u00dd%\3\2\2\2\u00de\u00e3\5(\25\2\u00df")
        buf.write("\u00e3\5*\26\2\u00e0\u00e3\5,\27\2\u00e1\u00e3\5.\30\2")
        buf.write("\u00e2\u00de\3\2\2\2\u00e2\u00df\3\2\2\2\u00e2\u00e0\3")
        buf.write("\2\2\2\u00e2\u00e1\3\2\2\2\u00e3\'\3\2\2\2\u00e4\u00e7")
        buf.write("\7\5\2\2\u00e5\u00e6\78\2\2\u00e6\u00e8\5(\25\2\u00e7")
        buf.write("\u00e5\3\2\2\2\u00e7\u00e8\3\2\2\2\u00e8\u00eb\3\2\2\2")
        buf.write("\u00e9\u00eb\7\5\2\2\u00ea\u00e4\3\2\2\2\u00ea\u00e9\3")
        buf.write("\2\2\2\u00eb)\3\2\2\2\u00ec\u00ef\7\6\2\2\u00ed\u00ee")
        buf.write("\78\2\2\u00ee\u00f0\5*\26\2\u00ef\u00ed\3\2\2\2\u00ef")
        buf.write("\u00f0\3\2\2\2\u00f0\u00f3\3\2\2\2\u00f1\u00f3\7\6\2\2")
        buf.write("\u00f2\u00ec\3\2\2\2\u00f2\u00f1\3\2\2\2\u00f3+\3\2\2")
        buf.write("\2\u00f4\u00f7\7\7\2\2\u00f5\u00f6\78\2\2\u00f6\u00f8")
        buf.write("\5,\27\2\u00f7\u00f5\3\2\2\2\u00f7\u00f8\3\2\2\2\u00f8")
        buf.write("\u00fb\3\2\2\2\u00f9\u00fb\7\7\2\2\u00fa\u00f4\3\2\2\2")
        buf.write("\u00fa\u00f9\3\2\2\2\u00fb-\3\2\2\2\u00fc\u00ff\7\b\2")
        buf.write("\2\u00fd\u00fe\78\2\2\u00fe\u0100\5.\30\2\u00ff\u00fd")
        buf.write("\3\2\2\2\u00ff\u0100\3\2\2\2\u0100\u0103\3\2\2\2\u0101")
        buf.write("\u0103\7\b\2\2\u0102\u00fc\3\2\2\2\u0102\u0101\3\2\2\2")
        buf.write("\u0103/\3\2\2\2\u0104\u0105\t\2\2\2\u0105\61\3\2\2\2\u0106")
        buf.write("\u0109\5\60\31\2\u0107\u0109\7\32\2\2\u0108\u0106\3\2")
        buf.write("\2\2\u0108\u0107\3\2\2\2\u0109\63\3\2\2\2\u010a\u010b")
        buf.write("\5\60\31\2\u010b\u010c\7\61\2\2\u010c\u010d\7\5\2\2\u010d")
        buf.write("\u010e\7\62\2\2\u010e\65\3\2\2\2\u010f\u0110\58\35\2\u0110")
        buf.write("\u0111\7)\2\2\u0111\u0112\58\35\2\u0112\u0121\3\2\2\2")
        buf.write("\u0113\u0114\58\35\2\u0114\u0115\7*\2\2\u0115\u0116\5")
        buf.write("8\35\2\u0116\u0121\3\2\2\2\u0117\u0118\58\35\2\u0118\u0119")
        buf.write("\7+\2\2\u0119\u011a\58\35\2\u011a\u0121\3\2\2\2\u011b")
        buf.write("\u011c\58\35\2\u011c\u011d\7,\2\2\u011d\u011e\58\35\2")
        buf.write("\u011e\u0121\3\2\2\2\u011f\u0121\58\35\2\u0120\u010f\3")
        buf.write("\2\2\2\u0120\u0113\3\2\2\2\u0120\u0117\3\2\2\2\u0120\u011b")
        buf.write("\3\2\2\2\u0120\u011f\3\2\2\2\u0121\67\3\2\2\2\u0122\u0123")
        buf.write("\5:\36\2\u0123\u0124\7(\2\2\u0124\u0125\5:\36\2\u0125")
        buf.write("\u012c\3\2\2\2\u0126\u0127\5:\36\2\u0127\u0128\7\'\2\2")
        buf.write("\u0128\u0129\5:\36\2\u0129\u012c\3\2\2\2\u012a\u012c\5")
        buf.write(":\36\2\u012b\u0122\3\2\2\2\u012b\u0126\3\2\2\2\u012b\u012a")
        buf.write("\3\2\2\2\u012c9\3\2\2\2\u012d\u012e\b\36\1\2\u012e\u012f")
        buf.write("\5<\37\2\u012f\u0138\3\2\2\2\u0130\u0131\f\5\2\2\u0131")
        buf.write("\u0132\7.\2\2\u0132\u0137\5<\37\2\u0133\u0134\f\4\2\2")
        buf.write("\u0134\u0135\7-\2\2\u0135\u0137\5<\37\2\u0136\u0130\3")
        buf.write("\2\2\2\u0136\u0133\3\2\2\2\u0137\u013a\3\2\2\2\u0138\u0136")
        buf.write("\3\2\2\2\u0138\u0139\3\2\2\2\u0139;\3\2\2\2\u013a\u0138")
        buf.write("\3\2\2\2\u013b\u013c\b\37\1\2\u013c\u013d\5> \2\u013d")
        buf.write("\u0146\3\2\2\2\u013e\u013f\f\5\2\2\u013f\u0140\7!\2\2")
        buf.write("\u0140\u0145\5> \2\u0141\u0142\f\4\2\2\u0142\u0143\7\"")
        buf.write("\2\2\u0143\u0145\5> \2\u0144\u013e\3\2\2\2\u0144\u0141")
        buf.write("\3\2\2\2\u0145\u0148\3\2\2\2\u0146\u0144\3\2\2\2\u0146")
        buf.write("\u0147\3\2\2\2\u0147=\3\2\2\2\u0148\u0146\3\2\2\2\u0149")
        buf.write("\u014a\b \1\2\u014a\u014b\5@!\2\u014b\u015a\3\2\2\2\u014c")
        buf.write("\u014d\f\7\2\2\u014d\u014e\7#\2\2\u014e\u0159\5@!\2\u014f")
        buf.write("\u0150\f\6\2\2\u0150\u0151\7$\2\2\u0151\u0159\5@!\2\u0152")
        buf.write("\u0153\f\5\2\2\u0153\u0154\7%\2\2\u0154\u0159\5@!\2\u0155")
        buf.write("\u0156\f\4\2\2\u0156\u0157\7&\2\2\u0157\u0159\5@!\2\u0158")
        buf.write("\u014c\3\2\2\2\u0158\u014f\3\2\2\2\u0158\u0152\3\2\2\2")
        buf.write("\u0158\u0155\3\2\2\2\u0159\u015c\3\2\2\2\u015a\u0158\3")
        buf.write("\2\2\2\u015a\u015b\3\2\2\2\u015b?\3\2\2\2\u015c\u015a")
        buf.write("\3\2\2\2\u015d\u015e\b!\1\2\u015e\u015f\5B\"\2\u015f\u0165")
        buf.write("\3\2\2\2\u0160\u0161\f\4\2\2\u0161\u0162\7\60\2\2\u0162")
        buf.write("\u0164\5B\"\2\u0163\u0160\3\2\2\2\u0164\u0167\3\2\2\2")
        buf.write("\u0165\u0163\3\2\2\2\u0165\u0166\3\2\2\2\u0166A\3\2\2")
        buf.write("\2\u0167\u0165\3\2\2\2\u0168\u0169\7/\2\2\u0169\u016c")
        buf.write("\5B\"\2\u016a\u016c\5D#\2\u016b\u0168\3\2\2\2\u016b\u016a")
        buf.write("\3\2\2\2\u016cC\3\2\2\2\u016d\u016e\7\"\2\2\u016e\u0173")
        buf.write("\5D#\2\u016f\u0170\7!\2\2\u0170\u0173\5D#\2\u0171\u0173")
        buf.write("\5F$\2\u0172\u016d\3\2\2\2\u0172\u016f\3\2\2\2\u0172\u0171")
        buf.write("\3\2\2\2\u0173E\3\2\2\2\u0174\u0175\b$\1\2\u0175\u0176")
        buf.write("\5H%\2\u0176\u017e\3\2\2\2\u0177\u0178\f\4\2\2\u0178\u0179")
        buf.write("\7\61\2\2\u0179\u017a\5\66\34\2\u017a\u017b\7\62\2\2\u017b")
        buf.write("\u017d\3\2\2\2\u017c\u0177\3\2\2\2\u017d\u0180\3\2\2\2")
        buf.write("\u017e\u017c\3\2\2\2\u017e\u017f\3\2\2\2\u017fG\3\2\2")
        buf.write("\2\u0180\u017e\3\2\2\2\u0181\u0182\b%\1\2\u0182\u0183")
        buf.write("\5J&\2\u0183\u018c\3\2\2\2\u0184\u0185\f\4\2\2\u0185\u0186")
        buf.write("\7\67\2\2\u0186\u0188\7;\2\2\u0187\u0189\5P)\2\u0188\u0187")
        buf.write("\3\2\2\2\u0188\u0189\3\2\2\2\u0189\u018b\3\2\2\2\u018a")
        buf.write("\u0184\3\2\2\2\u018b\u018e\3\2\2\2\u018c\u018a\3\2\2\2")
        buf.write("\u018c\u018d\3\2\2\2\u018dI\3\2\2\2\u018e\u018c\3\2\2")
        buf.write("\2\u018f\u0190\7\23\2\2\u0190\u0191\7;\2\2\u0191\u0194")
        buf.write("\5P)\2\u0192\u0194\5L\'\2\u0193\u018f\3\2\2\2\u0193\u0192")
        buf.write("\3\2\2\2\u0194K\3\2\2\2\u0195\u0196\7\64\2\2\u0196\u0197")
        buf.write("\5\66\34\2\u0197\u0198\7\65\2\2\u0198\u019d\3\2\2\2\u0199")
        buf.write("\u019d\7;\2\2\u019a\u019d\5N(\2\u019b\u019d\7\34\2\2\u019c")
        buf.write("\u0195\3\2\2\2\u019c\u0199\3\2\2\2\u019c\u019a\3\2\2\2")
        buf.write("\u019c\u019b\3\2\2\2\u019dM\3\2\2\2\u019e\u01a4\7\5\2")
        buf.write("\2\u019f\u01a4\7\6\2\2\u01a0\u01a4\7\7\2\2\u01a1\u01a4")
        buf.write("\7\b\2\2\u01a2\u01a4\5$\23\2\u01a3\u019e\3\2\2\2\u01a3")
        buf.write("\u019f\3\2\2\2\u01a3\u01a0\3\2\2\2\u01a3\u01a1\3\2\2\2")
        buf.write("\u01a3\u01a2\3\2\2\2\u01a4O\3\2\2\2\u01a5\u01a7\7\64\2")
        buf.write("\2\u01a6\u01a8\5R*\2\u01a7\u01a6\3\2\2\2\u01a7\u01a8\3")
        buf.write("\2\2\2\u01a8\u01a9\3\2\2\2\u01a9\u01aa\7\65\2\2\u01aa")
        buf.write("Q\3\2\2\2\u01ab\u01ac\5\66\34\2\u01ac\u01ad\78\2\2\u01ad")
        buf.write("\u01ae\5R*\2\u01ae\u01b1\3\2\2\2\u01af\u01b1\5\66\34\2")
        buf.write("\u01b0\u01ab\3\2\2\2\u01b0\u01af\3\2\2\2\u01b1S\3\2\2")
        buf.write("\2\u01b2\u01ba\5^\60\2\u01b3\u01ba\5`\61\2\u01b4\u01ba")
        buf.write("\5b\62\2\u01b5\u01ba\5d\63\2\u01b6\u01ba\5f\64\2\u01b7")
        buf.write("\u01ba\5h\65\2\u01b8\u01ba\5j\66\2\u01b9\u01b2\3\2\2\2")
        buf.write("\u01b9\u01b3\3\2\2\2\u01b9\u01b4\3\2\2\2\u01b9\u01b5\3")
        buf.write("\2\2\2\u01b9\u01b6\3\2\2\2\u01b9\u01b7\3\2\2\2\u01b9\u01b8")
        buf.write("\3\2\2\2\u01baU\3\2\2\2\u01bb\u01bc\5T+\2\u01bc\u01bd")
        buf.write("\5V,\2\u01bd\u01c0\3\2\2\2\u01be\u01c0\3\2\2\2\u01bf\u01bb")
        buf.write("\3\2\2\2\u01bf\u01be\3\2\2\2\u01c0W\3\2\2\2\u01c1\u01c2")
        buf.write("\5\20\t\2\u01c2\u01c3\5X-\2\u01c3\u01c6\3\2\2\2\u01c4")
        buf.write("\u01c6\3\2\2\2\u01c5\u01c1\3\2\2\2\u01c5\u01c4\3\2\2\2")
        buf.write("\u01c6Y\3\2\2\2\u01c7\u01c8\7:\2\2\u01c8\u01c9\5X-\2\u01c9")
        buf.write("\u01ca\5V,\2\u01ca\u01cb\79\2\2\u01cb[\3\2\2\2\u01cc\u01cf")
        buf.write("\5T+\2\u01cd\u01cf\5Z.\2\u01ce\u01cc\3\2\2\2\u01ce\u01cd")
        buf.write("\3\2\2\2\u01cf]\3\2\2\2\u01d0\u01d1\5\66\34\2\u01d1\u01d2")
        buf.write("\7\63\2\2\u01d2\u01d3\7\3\2\2\u01d3\u01d4\5\66\34\2\u01d4")
        buf.write("\u01d5\7\66\2\2\u01d5_\3\2\2\2\u01d6\u01d7\7\21\2\2\u01d7")
        buf.write("\u01d8\5\66\34\2\u01d8\u01d9\7\25\2\2\u01d9\u01dc\5\\")
        buf.write("/\2\u01da\u01db\7\16\2\2\u01db\u01dd\5\\/\2\u01dc\u01da")
        buf.write("\3\2\2\2\u01dc\u01dd\3\2\2\2\u01dda\3\2\2\2\u01de\u01df")
        buf.write("\7\26\2\2\u01df\u01e0\7;\2\2\u01e0\u01e1\7\63\2\2\u01e1")
        buf.write("\u01e2\7\3\2\2\u01e2\u01e3\5\66\34\2\u01e3\u01e4\t\3\2")
        buf.write("\2\u01e4\u01e5\5\66\34\2\u01e5\u01e6\7\r\2\2\u01e6\u01e7")
        buf.write("\5\\/\2\u01e7c\3\2\2\2\u01e8\u01e9\7\n\2\2\u01e9\u01ea")
        buf.write("\7\66\2\2\u01eae\3\2\2\2\u01eb\u01ec\7\f\2\2\u01ec\u01ed")
        buf.write("\7\66\2\2\u01edg\3\2\2\2\u01ee\u01ef\7\27\2\2\u01ef\u01f0")
        buf.write("\5\66\34\2\u01f0\u01f1\7\66\2\2\u01f1i\3\2\2\2\u01f2\u01f3")
        buf.write("\5\66\34\2\u01f3\u01f4\7\67\2\2\u01f4\u01f5\7;\2\2\u01f5")
        buf.write("\u01f6\5P)\2\u01f6\u01f7\7\66\2\2\u01f7k\3\2\2\2\65qu")
        buf.write("{\u0088\u008e\u0099\u009c\u00a3\u00a8\u00ad\u00b2\u00b9")
        buf.write("\u00bf\u00c4\u00c8\u00cf\u00d8\u00e2\u00e7\u00ea\u00ef")
        buf.write("\u00f2\u00f7\u00fa\u00ff\u0102\u0108\u0120\u012b\u0136")
        buf.write("\u0138\u0144\u0146\u0158\u015a\u0165\u016b\u0172\u017e")
        buf.write("\u0188\u018c\u0193\u019c\u01a3\u01a7\u01b0\u01b9\u01bf")
        buf.write("\u01c5\u01ce\u01dc")
        return buf.getvalue()


class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'boolean'", "'break'", "'class'", 
                     "'continue'", "'do'", "'else'", "'extends'", "'float'", 
                     "'if'", "'int'", "'new'", "'string'", "'then'", "'for'", 
                     "'return'", "'true'", "'false'", "'void'", "'nil'", 
                     "'this'", "'final'", "'static'", "'to'", "'downto'", 
                     "'+'", "'-'", "'*'", "'/'", "'\\'", "'%'", "'!='", 
                     "'=='", "'<'", "'>'", "'<='", "'>='", "'||'", "'&&'", 
                     "'!'", "'^'", "'['", "']'", "':'", "'('", "')'", "';'", 
                     "'.'", "','", "'}'", "'{'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "COMMENT", "INT_LIT", "FLOAT_LIT", 
                      "BOOL_LIT", "STRING_LIT", "BOOLEAN", "BREAK", "CLASS", 
                      "CONTINUE", "DO", "ELSE", "EXTENDS", "FLOAT", "IF", 
                      "INT", "NEW", "STRING", "THEN", "FOR", "RETURN", "TRUE", 
                      "FALSE", "VOID", "NIL", "THIS", "FINAL", "STATIC", 
                      "TO", "DOWNTO", "ADD", "SUB", "MUL", "FDIV", "IDIV", 
                      "MOD", "NOT_EQUAL", "EQUAL", "LTHAN", "GTHAN", "LEQUAL", 
                      "GEQUAL", "OR", "AND", "NOT", "CONCATE", "LSB", "RSB", 
                      "COLON", "LB", "RB", "SEMI", "DOT", "COMMA", "RP", 
                      "LP", "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_list_class_dec = 1
    RULE_mptype = 2
    RULE_class_dec = 3
    RULE_list_member = 4
    RULE_list_attrib_dec = 5
    RULE_list_method_dec = 6
    RULE_decl_var = 7
    RULE_attrib_dec = 8
    RULE_list_attrib_const = 9
    RULE_list_attrib_var = 10
    RULE_attrib_const = 11
    RULE_attrib_var = 12
    RULE_method_dec = 13
    RULE_list_para = 14
    RULE_para_dec = 15
    RULE_list_id = 16
    RULE_array_lit = 17
    RULE_list_lit = 18
    RULE_list_int = 19
    RULE_list_float = 20
    RULE_list_bool = 21
    RULE_list_string = 22
    RULE_common_type = 23
    RULE_primitive_type = 24
    RULE_array_type = 25
    RULE_exp = 26
    RULE_exp1 = 27
    RULE_exp2 = 28
    RULE_exp3 = 29
    RULE_exp4 = 30
    RULE_exp5 = 31
    RULE_exp6 = 32
    RULE_exp7 = 33
    RULE_exp8 = 34
    RULE_exp9 = 35
    RULE_exp10 = 36
    RULE_exp11 = 37
    RULE_literals = 38
    RULE_list_arg = 39
    RULE_listexp = 40
    RULE_all_state = 41
    RULE_list_state = 42
    RULE_list_decl_var = 43
    RULE_block_state = 44
    RULE_exp_state = 45
    RULE_assign_state = 46
    RULE_if_state = 47
    RULE_for_state = 48
    RULE_break_state = 49
    RULE_continue_state = 50
    RULE_return_state = 51
    RULE_invocation_state = 52

    ruleNames =  [ "program", "list_class_dec", "mptype", "class_dec", "list_member", 
                   "list_attrib_dec", "list_method_dec", "decl_var", "attrib_dec", 
                   "list_attrib_const", "list_attrib_var", "attrib_const", 
                   "attrib_var", "method_dec", "list_para", "para_dec", 
                   "list_id", "array_lit", "list_lit", "list_int", "list_float", 
                   "list_bool", "list_string", "common_type", "primitive_type", 
                   "array_type", "exp", "exp1", "exp2", "exp3", "exp4", 
                   "exp5", "exp6", "exp7", "exp8", "exp9", "exp10", "exp11", 
                   "literals", "list_arg", "listexp", "all_state", "list_state", 
                   "list_decl_var", "block_state", "exp_state", "assign_state", 
                   "if_state", "for_state", "break_state", "continue_state", 
                   "return_state", "invocation_state" ]

    EOF = Token.EOF
    T__0=1
    COMMENT=2
    INT_LIT=3
    FLOAT_LIT=4
    BOOL_LIT=5
    STRING_LIT=6
    BOOLEAN=7
    BREAK=8
    CLASS=9
    CONTINUE=10
    DO=11
    ELSE=12
    EXTENDS=13
    FLOAT=14
    IF=15
    INT=16
    NEW=17
    STRING=18
    THEN=19
    FOR=20
    RETURN=21
    TRUE=22
    FALSE=23
    VOID=24
    NIL=25
    THIS=26
    FINAL=27
    STATIC=28
    TO=29
    DOWNTO=30
    ADD=31
    SUB=32
    MUL=33
    FDIV=34
    IDIV=35
    MOD=36
    NOT_EQUAL=37
    EQUAL=38
    LTHAN=39
    GTHAN=40
    LEQUAL=41
    GEQUAL=42
    OR=43
    AND=44
    NOT=45
    CONCATE=46
    LSB=47
    RSB=48
    COLON=49
    LB=50
    RB=51
    SEMI=52
    DOT=53
    COMMA=54
    RP=55
    LP=56
    ID=57
    WS=58
    ERROR_CHAR=59
    UNCLOSE_STRING=60
    ILLEGAL_ESCAPE=61

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_class_dec(self):
            return self.getTypedRuleContext(BKOOLParser.List_class_decContext,0)


        def EOF(self):
            return self.getToken(BKOOLParser.EOF, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKOOLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.list_class_dec()
            self.state = 107
            self.match(BKOOLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_class_decContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_dec(self):
            return self.getTypedRuleContext(BKOOLParser.Class_decContext,0)


        def list_class_dec(self):
            return self.getTypedRuleContext(BKOOLParser.List_class_decContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_list_class_dec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_class_dec" ):
                return visitor.visitList_class_dec(self)
            else:
                return visitor.visitChildren(self)




    def list_class_dec(self):

        localctx = BKOOLParser.List_class_decContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_list_class_dec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.class_dec()
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.CLASS:
                self.state = 110
                self.list_class_dec()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MptypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(BKOOLParser.Primitive_typeContext,0)


        def array_type(self):
            return self.getTypedRuleContext(BKOOLParser.Array_typeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_mptype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMptype" ):
                return visitor.visitMptype(self)
            else:
                return visitor.visitChildren(self)




    def mptype(self):

        localctx = BKOOLParser.MptypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_mptype)
        try:
            self.state = 115
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 113
                self.primitive_type()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 114
                self.array_type()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_decContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(BKOOLParser.CLASS, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def list_member(self):
            return self.getTypedRuleContext(BKOOLParser.List_memberContext,0)


        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def EXTENDS(self):
            return self.getToken(BKOOLParser.EXTENDS, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_class_dec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_dec" ):
                return visitor.visitClass_dec(self)
            else:
                return visitor.visitChildren(self)




    def class_dec(self):

        localctx = BKOOLParser.Class_decContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_class_dec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(BKOOLParser.CLASS)
            self.state = 118
            self.match(BKOOLParser.ID)
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.EXTENDS:
                self.state = 119
                self.match(BKOOLParser.EXTENDS)
                self.state = 120
                self.match(BKOOLParser.ID)


            self.state = 123
            self.match(BKOOLParser.LP)
            self.state = 124
            self.list_member()
            self.state = 125
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_memberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_attrib_dec(self):
            return self.getTypedRuleContext(BKOOLParser.List_attrib_decContext,0)


        def list_method_dec(self):
            return self.getTypedRuleContext(BKOOLParser.List_method_decContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_list_member

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_member" ):
                return visitor.visitList_member(self)
            else:
                return visitor.visitChildren(self)




    def list_member(self):

        localctx = BKOOLParser.List_memberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_list_member)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.list_attrib_dec()
            self.state = 128
            self.list_method_dec()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_attrib_decContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attrib_dec(self):
            return self.getTypedRuleContext(BKOOLParser.Attrib_decContext,0)


        def list_attrib_dec(self):
            return self.getTypedRuleContext(BKOOLParser.List_attrib_decContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_list_attrib_dec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_attrib_dec" ):
                return visitor.visitList_attrib_dec(self)
            else:
                return visitor.visitChildren(self)




    def list_attrib_dec(self):

        localctx = BKOOLParser.List_attrib_decContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_list_attrib_dec)
        try:
            self.state = 134
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 130
                self.attrib_dec()
                self.state = 131
                self.list_attrib_dec()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_method_decContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def method_dec(self):
            return self.getTypedRuleContext(BKOOLParser.Method_decContext,0)


        def list_method_dec(self):
            return self.getTypedRuleContext(BKOOLParser.List_method_decContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_list_method_dec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_method_dec" ):
                return visitor.visitList_method_dec(self)
            else:
                return visitor.visitChildren(self)




    def list_method_dec(self):

        localctx = BKOOLParser.List_method_decContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_list_method_dec)
        try:
            self.state = 140
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.BOOLEAN, BKOOLParser.FLOAT, BKOOLParser.INT, BKOOLParser.STRING, BKOOLParser.VOID, BKOOLParser.STATIC, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 136
                self.method_dec()
                self.state = 137
                self.list_method_dec()
                pass
            elif token in [BKOOLParser.RP]:
                self.enterOuterAlt(localctx, 2)

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


    class Decl_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FINAL(self):
            return self.getToken(BKOOLParser.FINAL, 0)

        def mptype(self):
            return self.getTypedRuleContext(BKOOLParser.MptypeContext,0)


        def list_attrib_const(self):
            return self.getTypedRuleContext(BKOOLParser.List_attrib_constContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def list_attrib_var(self):
            return self.getTypedRuleContext(BKOOLParser.List_attrib_varContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_decl_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl_var" ):
                return visitor.visitDecl_var(self)
            else:
                return visitor.visitChildren(self)




    def decl_var(self):

        localctx = BKOOLParser.Decl_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_decl_var)
        try:
            self.state = 151
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.FINAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 142
                self.match(BKOOLParser.FINAL)
                self.state = 143
                self.mptype()
                self.state = 144
                self.list_attrib_const()
                self.state = 145
                self.match(BKOOLParser.SEMI)
                pass
            elif token in [BKOOLParser.BOOLEAN, BKOOLParser.FLOAT, BKOOLParser.INT, BKOOLParser.STRING, BKOOLParser.VOID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 147
                self.mptype()
                self.state = 148
                self.list_attrib_var()
                self.state = 149
                self.match(BKOOLParser.SEMI)
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


    class Attrib_decContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl_var(self):
            return self.getTypedRuleContext(BKOOLParser.Decl_varContext,0)


        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_attrib_dec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttrib_dec" ):
                return visitor.visitAttrib_dec(self)
            else:
                return visitor.visitChildren(self)




    def attrib_dec(self):

        localctx = BKOOLParser.Attrib_decContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_attrib_dec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.STATIC:
                self.state = 153
                self.match(BKOOLParser.STATIC)


            self.state = 156
            self.decl_var()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_attrib_constContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attrib_const(self):
            return self.getTypedRuleContext(BKOOLParser.Attrib_constContext,0)


        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def list_attrib_const(self):
            return self.getTypedRuleContext(BKOOLParser.List_attrib_constContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_list_attrib_const

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_attrib_const" ):
                return visitor.visitList_attrib_const(self)
            else:
                return visitor.visitChildren(self)




    def list_attrib_const(self):

        localctx = BKOOLParser.List_attrib_constContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_list_attrib_const)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.attrib_const()
            self.state = 161
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.COMMA:
                self.state = 159
                self.match(BKOOLParser.COMMA)
                self.state = 160
                self.list_attrib_const()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_attrib_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attrib_var(self):
            return self.getTypedRuleContext(BKOOLParser.Attrib_varContext,0)


        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def list_attrib_var(self):
            return self.getTypedRuleContext(BKOOLParser.List_attrib_varContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_list_attrib_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_attrib_var" ):
                return visitor.visitList_attrib_var(self)
            else:
                return visitor.visitChildren(self)




    def list_attrib_var(self):

        localctx = BKOOLParser.List_attrib_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_list_attrib_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.attrib_var()
            self.state = 166
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.COMMA:
                self.state = 164
                self.match(BKOOLParser.COMMA)
                self.state = 165
                self.list_attrib_var()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attrib_constContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_attrib_const

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttrib_const" ):
                return visitor.visitAttrib_const(self)
            else:
                return visitor.visitChildren(self)




    def attrib_const(self):

        localctx = BKOOLParser.Attrib_constContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_attrib_const)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.match(BKOOLParser.ID)
            self.state = 171
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.T__0:
                self.state = 169
                self.match(BKOOLParser.T__0)
                self.state = 170
                self.exp()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attrib_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_attrib_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttrib_var" ):
                return visitor.visitAttrib_var(self)
            else:
                return visitor.visitChildren(self)




    def attrib_var(self):

        localctx = BKOOLParser.Attrib_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_attrib_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.match(BKOOLParser.ID)
            self.state = 176
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.T__0:
                self.state = 174
                self.match(BKOOLParser.T__0)
                self.state = 175
                self.exp()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_decContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def mptype(self):
            return self.getTypedRuleContext(BKOOLParser.MptypeContext,0)


        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def block_state(self):
            return self.getTypedRuleContext(BKOOLParser.Block_stateContext,0)


        def list_para(self):
            return self.getTypedRuleContext(BKOOLParser.List_paraContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_method_dec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_dec" ):
                return visitor.visitMethod_dec(self)
            else:
                return visitor.visitChildren(self)




    def method_dec(self):

        localctx = BKOOLParser.Method_decContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_method_dec)
        self._la = 0 # Token type
        try:
            self.state = 198
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.STATIC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 178
                self.match(BKOOLParser.STATIC)
                self.state = 179
                self.mptype()
                self.state = 180
                self.match(BKOOLParser.ID)
                self.state = 181
                self.match(BKOOLParser.LB)
                self.state = 183
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.VOID))) != 0):
                    self.state = 182
                    self.list_para()


                self.state = 185
                self.match(BKOOLParser.RB)
                self.state = 186
                self.block_state()
                pass
            elif token in [BKOOLParser.BOOLEAN, BKOOLParser.FLOAT, BKOOLParser.INT, BKOOLParser.STRING, BKOOLParser.VOID, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 189
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.VOID))) != 0):
                    self.state = 188
                    self.mptype()


                self.state = 191
                self.match(BKOOLParser.ID)
                self.state = 192
                self.match(BKOOLParser.LB)
                self.state = 194
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.VOID))) != 0):
                    self.state = 193
                    self.list_para()


                self.state = 196
                self.match(BKOOLParser.RB)
                self.state = 197
                self.block_state()
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


    class List_paraContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def para_dec(self):
            return self.getTypedRuleContext(BKOOLParser.Para_decContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def list_para(self):
            return self.getTypedRuleContext(BKOOLParser.List_paraContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_list_para

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_para" ):
                return visitor.visitList_para(self)
            else:
                return visitor.visitChildren(self)




    def list_para(self):

        localctx = BKOOLParser.List_paraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_list_para)
        try:
            self.state = 205
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 200
                self.para_dec()
                self.state = 201
                self.match(BKOOLParser.SEMI)
                self.state = 202
                self.list_para()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 204
                self.para_dec()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Para_decContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mptype(self):
            return self.getTypedRuleContext(BKOOLParser.MptypeContext,0)


        def list_id(self):
            return self.getTypedRuleContext(BKOOLParser.List_idContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_para_dec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara_dec" ):
                return visitor.visitPara_dec(self)
            else:
                return visitor.visitChildren(self)




    def para_dec(self):

        localctx = BKOOLParser.Para_decContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_para_dec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.mptype()
            self.state = 208
            self.list_id()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_idContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def list_id(self):
            return self.getTypedRuleContext(BKOOLParser.List_idContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_list_id

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_id" ):
                return visitor.visitList_id(self)
            else:
                return visitor.visitChildren(self)




    def list_id(self):

        localctx = BKOOLParser.List_idContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_list_id)
        try:
            self.state = 214
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 210
                self.match(BKOOLParser.ID)
                self.state = 211
                self.match(BKOOLParser.COMMA)
                self.state = 212
                self.list_id()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 213
                self.match(BKOOLParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def list_lit(self):
            return self.getTypedRuleContext(BKOOLParser.List_litContext,0)


        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_array_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_lit" ):
                return visitor.visitArray_lit(self)
            else:
                return visitor.visitChildren(self)




    def array_lit(self):

        localctx = BKOOLParser.Array_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_array_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.match(BKOOLParser.LP)
            self.state = 217
            self.list_lit()
            self.state = 218
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_int(self):
            return self.getTypedRuleContext(BKOOLParser.List_intContext,0)


        def list_float(self):
            return self.getTypedRuleContext(BKOOLParser.List_floatContext,0)


        def list_bool(self):
            return self.getTypedRuleContext(BKOOLParser.List_boolContext,0)


        def list_string(self):
            return self.getTypedRuleContext(BKOOLParser.List_stringContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_list_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_lit" ):
                return visitor.visitList_lit(self)
            else:
                return visitor.visitChildren(self)




    def list_lit(self):

        localctx = BKOOLParser.List_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_list_lit)
        try:
            self.state = 224
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INT_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 220
                self.list_int()
                pass
            elif token in [BKOOLParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 221
                self.list_float()
                pass
            elif token in [BKOOLParser.BOOL_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 222
                self.list_bool()
                pass
            elif token in [BKOOLParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 223
                self.list_string()
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


    class List_intContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(BKOOLParser.INT_LIT, 0)

        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def list_int(self):
            return self.getTypedRuleContext(BKOOLParser.List_intContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_list_int

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_int" ):
                return visitor.visitList_int(self)
            else:
                return visitor.visitChildren(self)




    def list_int(self):

        localctx = BKOOLParser.List_intContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_list_int)
        self._la = 0 # Token type
        try:
            self.state = 232
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 226
                self.match(BKOOLParser.INT_LIT)
                self.state = 229
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKOOLParser.COMMA:
                    self.state = 227
                    self.match(BKOOLParser.COMMA)
                    self.state = 228
                    self.list_int()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 231
                self.match(BKOOLParser.INT_LIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_floatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOAT_LIT(self):
            return self.getToken(BKOOLParser.FLOAT_LIT, 0)

        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def list_float(self):
            return self.getTypedRuleContext(BKOOLParser.List_floatContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_list_float

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_float" ):
                return visitor.visitList_float(self)
            else:
                return visitor.visitChildren(self)




    def list_float(self):

        localctx = BKOOLParser.List_floatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_list_float)
        self._la = 0 # Token type
        try:
            self.state = 240
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 234
                self.match(BKOOLParser.FLOAT_LIT)
                self.state = 237
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKOOLParser.COMMA:
                    self.state = 235
                    self.match(BKOOLParser.COMMA)
                    self.state = 236
                    self.list_float()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 239
                self.match(BKOOLParser.FLOAT_LIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_boolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOL_LIT(self):
            return self.getToken(BKOOLParser.BOOL_LIT, 0)

        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def list_bool(self):
            return self.getTypedRuleContext(BKOOLParser.List_boolContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_list_bool

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_bool" ):
                return visitor.visitList_bool(self)
            else:
                return visitor.visitChildren(self)




    def list_bool(self):

        localctx = BKOOLParser.List_boolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_list_bool)
        self._la = 0 # Token type
        try:
            self.state = 248
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 242
                self.match(BKOOLParser.BOOL_LIT)
                self.state = 245
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKOOLParser.COMMA:
                    self.state = 243
                    self.match(BKOOLParser.COMMA)
                    self.state = 244
                    self.list_bool()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 247
                self.match(BKOOLParser.BOOL_LIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_stringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_LIT(self):
            return self.getToken(BKOOLParser.STRING_LIT, 0)

        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def list_string(self):
            return self.getTypedRuleContext(BKOOLParser.List_stringContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_list_string

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_string" ):
                return visitor.visitList_string(self)
            else:
                return visitor.visitChildren(self)




    def list_string(self):

        localctx = BKOOLParser.List_stringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_list_string)
        self._la = 0 # Token type
        try:
            self.state = 256
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 250
                self.match(BKOOLParser.STRING_LIT)
                self.state = 253
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKOOLParser.COMMA:
                    self.state = 251
                    self.match(BKOOLParser.COMMA)
                    self.state = 252
                    self.list_string()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 255
                self.match(BKOOLParser.STRING_LIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Common_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(BKOOLParser.INT, 0)

        def FLOAT(self):
            return self.getToken(BKOOLParser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(BKOOLParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(BKOOLParser.STRING, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_common_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommon_type" ):
                return visitor.visitCommon_type(self)
            else:
                return visitor.visitChildren(self)




    def common_type(self):

        localctx = BKOOLParser.Common_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_common_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def common_type(self):
            return self.getTypedRuleContext(BKOOLParser.Common_typeContext,0)


        def VOID(self):
            return self.getToken(BKOOLParser.VOID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_primitive_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_type" ):
                return visitor.visitPrimitive_type(self)
            else:
                return visitor.visitChildren(self)




    def primitive_type(self):

        localctx = BKOOLParser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_primitive_type)
        try:
            self.state = 262
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.BOOLEAN, BKOOLParser.FLOAT, BKOOLParser.INT, BKOOLParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 260
                self.common_type()
                pass
            elif token in [BKOOLParser.VOID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 261
                self.match(BKOOLParser.VOID)
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


    class Array_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def common_type(self):
            return self.getTypedRuleContext(BKOOLParser.Common_typeContext,0)


        def LSB(self):
            return self.getToken(BKOOLParser.LSB, 0)

        def INT_LIT(self):
            return self.getToken(BKOOLParser.INT_LIT, 0)

        def RSB(self):
            return self.getToken(BKOOLParser.RSB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_array_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = BKOOLParser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.common_type()
            self.state = 265
            self.match(BKOOLParser.LSB)
            self.state = 266
            self.match(BKOOLParser.INT_LIT)
            self.state = 267
            self.match(BKOOLParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Exp1Context)
            else:
                return self.getTypedRuleContext(BKOOLParser.Exp1Context,i)


        def LTHAN(self):
            return self.getToken(BKOOLParser.LTHAN, 0)

        def GTHAN(self):
            return self.getToken(BKOOLParser.GTHAN, 0)

        def LEQUAL(self):
            return self.getToken(BKOOLParser.LEQUAL, 0)

        def GEQUAL(self):
            return self.getToken(BKOOLParser.GEQUAL, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = BKOOLParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_exp)
        try:
            self.state = 286
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 269
                self.exp1()
                self.state = 270
                self.match(BKOOLParser.LTHAN)
                self.state = 271
                self.exp1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 273
                self.exp1()
                self.state = 274
                self.match(BKOOLParser.GTHAN)
                self.state = 275
                self.exp1()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 277
                self.exp1()
                self.state = 278
                self.match(BKOOLParser.LEQUAL)
                self.state = 279
                self.exp1()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 281
                self.exp1()
                self.state = 282
                self.match(BKOOLParser.GEQUAL)
                self.state = 283
                self.exp1()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 285
                self.exp1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Exp2Context)
            else:
                return self.getTypedRuleContext(BKOOLParser.Exp2Context,i)


        def EQUAL(self):
            return self.getToken(BKOOLParser.EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(BKOOLParser.NOT_EQUAL, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp1" ):
                return visitor.visitExp1(self)
            else:
                return visitor.visitChildren(self)




    def exp1(self):

        localctx = BKOOLParser.Exp1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_exp1)
        try:
            self.state = 297
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 288
                self.exp2(0)
                self.state = 289
                self.match(BKOOLParser.EQUAL)
                self.state = 290
                self.exp2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 292
                self.exp2(0)
                self.state = 293
                self.match(BKOOLParser.NOT_EQUAL)
                self.state = 294
                self.exp2(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 296
                self.exp2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp3(self):
            return self.getTypedRuleContext(BKOOLParser.Exp3Context,0)


        def exp2(self):
            return self.getTypedRuleContext(BKOOLParser.Exp2Context,0)


        def AND(self):
            return self.getToken(BKOOLParser.AND, 0)

        def OR(self):
            return self.getToken(BKOOLParser.OR, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp2" ):
                return visitor.visitExp2(self)
            else:
                return visitor.visitChildren(self)



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_exp2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 310
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 308
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
                    if la_ == 1:
                        localctx = BKOOLParser.Exp2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                        self.state = 302
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 303
                        self.match(BKOOLParser.AND)
                        self.state = 304
                        self.exp3(0)
                        pass

                    elif la_ == 2:
                        localctx = BKOOLParser.Exp2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                        self.state = 305
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 306
                        self.match(BKOOLParser.OR)
                        self.state = 307
                        self.exp3(0)
                        pass

             
                self.state = 312
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp4(self):
            return self.getTypedRuleContext(BKOOLParser.Exp4Context,0)


        def exp3(self):
            return self.getTypedRuleContext(BKOOLParser.Exp3Context,0)


        def ADD(self):
            return self.getToken(BKOOLParser.ADD, 0)

        def SUB(self):
            return self.getToken(BKOOLParser.SUB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp3" ):
                return visitor.visitExp3(self)
            else:
                return visitor.visitChildren(self)



    def exp3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Exp3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_exp3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 314
            self.exp4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 324
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 322
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
                    if la_ == 1:
                        localctx = BKOOLParser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 316
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 317
                        self.match(BKOOLParser.ADD)
                        self.state = 318
                        self.exp4(0)
                        pass

                    elif la_ == 2:
                        localctx = BKOOLParser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 319
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 320
                        self.match(BKOOLParser.SUB)
                        self.state = 321
                        self.exp4(0)
                        pass

             
                self.state = 326
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp5(self):
            return self.getTypedRuleContext(BKOOLParser.Exp5Context,0)


        def exp4(self):
            return self.getTypedRuleContext(BKOOLParser.Exp4Context,0)


        def MUL(self):
            return self.getToken(BKOOLParser.MUL, 0)

        def FDIV(self):
            return self.getToken(BKOOLParser.FDIV, 0)

        def IDIV(self):
            return self.getToken(BKOOLParser.IDIV, 0)

        def MOD(self):
            return self.getToken(BKOOLParser.MOD, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp4" ):
                return visitor.visitExp4(self)
            else:
                return visitor.visitChildren(self)



    def exp4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Exp4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_exp4, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            self.exp5(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 344
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 342
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
                    if la_ == 1:
                        localctx = BKOOLParser.Exp4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                        self.state = 330
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 331
                        self.match(BKOOLParser.MUL)
                        self.state = 332
                        self.exp5(0)
                        pass

                    elif la_ == 2:
                        localctx = BKOOLParser.Exp4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                        self.state = 333
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 334
                        self.match(BKOOLParser.FDIV)
                        self.state = 335
                        self.exp5(0)
                        pass

                    elif la_ == 3:
                        localctx = BKOOLParser.Exp4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                        self.state = 336
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 337
                        self.match(BKOOLParser.IDIV)
                        self.state = 338
                        self.exp5(0)
                        pass

                    elif la_ == 4:
                        localctx = BKOOLParser.Exp4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                        self.state = 339
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 340
                        self.match(BKOOLParser.MOD)
                        self.state = 341
                        self.exp5(0)
                        pass

             
                self.state = 346
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp6(self):
            return self.getTypedRuleContext(BKOOLParser.Exp6Context,0)


        def exp5(self):
            return self.getTypedRuleContext(BKOOLParser.Exp5Context,0)


        def CONCATE(self):
            return self.getToken(BKOOLParser.CONCATE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp5" ):
                return visitor.visitExp5(self)
            else:
                return visitor.visitChildren(self)



    def exp5(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Exp5Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_exp5, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
            self.exp6()
            self._ctx.stop = self._input.LT(-1)
            self.state = 355
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp5Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp5)
                    self.state = 350
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 351
                    self.match(BKOOLParser.CONCATE)
                    self.state = 352
                    self.exp6() 
                self.state = 357
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(BKOOLParser.NOT, 0)

        def exp6(self):
            return self.getTypedRuleContext(BKOOLParser.Exp6Context,0)


        def exp7(self):
            return self.getTypedRuleContext(BKOOLParser.Exp7Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp6" ):
                return visitor.visitExp6(self)
            else:
                return visitor.visitChildren(self)




    def exp6(self):

        localctx = BKOOLParser.Exp6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_exp6)
        try:
            self.state = 361
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 358
                self.match(BKOOLParser.NOT)
                self.state = 359
                self.exp6()
                pass
            elif token in [BKOOLParser.INT_LIT, BKOOLParser.FLOAT_LIT, BKOOLParser.BOOL_LIT, BKOOLParser.STRING_LIT, BKOOLParser.NEW, BKOOLParser.THIS, BKOOLParser.ADD, BKOOLParser.SUB, BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 360
                self.exp7()
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


    class Exp7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB(self):
            return self.getToken(BKOOLParser.SUB, 0)

        def exp7(self):
            return self.getTypedRuleContext(BKOOLParser.Exp7Context,0)


        def ADD(self):
            return self.getToken(BKOOLParser.ADD, 0)

        def exp8(self):
            return self.getTypedRuleContext(BKOOLParser.Exp8Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp7" ):
                return visitor.visitExp7(self)
            else:
                return visitor.visitChildren(self)




    def exp7(self):

        localctx = BKOOLParser.Exp7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_exp7)
        try:
            self.state = 368
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 363
                self.match(BKOOLParser.SUB)
                self.state = 364
                self.exp7()
                pass
            elif token in [BKOOLParser.ADD]:
                self.enterOuterAlt(localctx, 2)
                self.state = 365
                self.match(BKOOLParser.ADD)
                self.state = 366
                self.exp7()
                pass
            elif token in [BKOOLParser.INT_LIT, BKOOLParser.FLOAT_LIT, BKOOLParser.BOOL_LIT, BKOOLParser.STRING_LIT, BKOOLParser.NEW, BKOOLParser.THIS, BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 367
                self.exp8(0)
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


    class Exp8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp9(self):
            return self.getTypedRuleContext(BKOOLParser.Exp9Context,0)


        def exp8(self):
            return self.getTypedRuleContext(BKOOLParser.Exp8Context,0)


        def LSB(self):
            return self.getToken(BKOOLParser.LSB, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def RSB(self):
            return self.getToken(BKOOLParser.RSB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp8" ):
                return visitor.visitExp8(self)
            else:
                return visitor.visitChildren(self)



    def exp8(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Exp8Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_exp8, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 371
            self.exp9(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 380
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp8)
                    self.state = 373
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 374
                    self.match(BKOOLParser.LSB)
                    self.state = 375
                    self.exp()
                    self.state = 376
                    self.match(BKOOLParser.RSB) 
                self.state = 382
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp9Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp10(self):
            return self.getTypedRuleContext(BKOOLParser.Exp10Context,0)


        def exp9(self):
            return self.getTypedRuleContext(BKOOLParser.Exp9Context,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def list_arg(self):
            return self.getTypedRuleContext(BKOOLParser.List_argContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp9

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp9" ):
                return visitor.visitExp9(self)
            else:
                return visitor.visitChildren(self)



    def exp9(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Exp9Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_exp9, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384
            self.exp10()
            self._ctx.stop = self._input.LT(-1)
            self.state = 394
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp9Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp9)
                    self.state = 386
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 387
                    self.match(BKOOLParser.DOT)
                    self.state = 388
                    self.match(BKOOLParser.ID)
                    self.state = 390
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
                    if la_ == 1:
                        self.state = 389
                        self.list_arg()

             
                self.state = 396
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp10Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(BKOOLParser.NEW, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def list_arg(self):
            return self.getTypedRuleContext(BKOOLParser.List_argContext,0)


        def exp11(self):
            return self.getTypedRuleContext(BKOOLParser.Exp11Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp10

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp10" ):
                return visitor.visitExp10(self)
            else:
                return visitor.visitChildren(self)




    def exp10(self):

        localctx = BKOOLParser.Exp10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_exp10)
        try:
            self.state = 401
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 397
                self.match(BKOOLParser.NEW)
                self.state = 398
                self.match(BKOOLParser.ID)
                self.state = 399
                self.list_arg()
                pass
            elif token in [BKOOLParser.INT_LIT, BKOOLParser.FLOAT_LIT, BKOOLParser.BOOL_LIT, BKOOLParser.STRING_LIT, BKOOLParser.THIS, BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 400
                self.exp11()
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


    class Exp11Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def literals(self):
            return self.getTypedRuleContext(BKOOLParser.LiteralsContext,0)


        def THIS(self):
            return self.getToken(BKOOLParser.THIS, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp11

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp11" ):
                return visitor.visitExp11(self)
            else:
                return visitor.visitChildren(self)




    def exp11(self):

        localctx = BKOOLParser.Exp11Context(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_exp11)
        try:
            self.state = 410
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.LB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 403
                self.match(BKOOLParser.LB)
                self.state = 404
                self.exp()
                self.state = 405
                self.match(BKOOLParser.RB)
                pass
            elif token in [BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 407
                self.match(BKOOLParser.ID)
                pass
            elif token in [BKOOLParser.INT_LIT, BKOOLParser.FLOAT_LIT, BKOOLParser.BOOL_LIT, BKOOLParser.STRING_LIT, BKOOLParser.LP]:
                self.enterOuterAlt(localctx, 3)
                self.state = 408
                self.literals()
                pass
            elif token in [BKOOLParser.THIS]:
                self.enterOuterAlt(localctx, 4)
                self.state = 409
                self.match(BKOOLParser.THIS)
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


    class LiteralsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(BKOOLParser.INT_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(BKOOLParser.FLOAT_LIT, 0)

        def BOOL_LIT(self):
            return self.getToken(BKOOLParser.BOOL_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(BKOOLParser.STRING_LIT, 0)

        def array_lit(self):
            return self.getTypedRuleContext(BKOOLParser.Array_litContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_literals

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiterals" ):
                return visitor.visitLiterals(self)
            else:
                return visitor.visitChildren(self)




    def literals(self):

        localctx = BKOOLParser.LiteralsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_literals)
        try:
            self.state = 417
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INT_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 412
                self.match(BKOOLParser.INT_LIT)
                pass
            elif token in [BKOOLParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 413
                self.match(BKOOLParser.FLOAT_LIT)
                pass
            elif token in [BKOOLParser.BOOL_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 414
                self.match(BKOOLParser.BOOL_LIT)
                pass
            elif token in [BKOOLParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 415
                self.match(BKOOLParser.STRING_LIT)
                pass
            elif token in [BKOOLParser.LP]:
                self.enterOuterAlt(localctx, 5)
                self.state = 416
                self.array_lit()
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


    class List_argContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def listexp(self):
            return self.getTypedRuleContext(BKOOLParser.ListexpContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_list_arg

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_arg" ):
                return visitor.visitList_arg(self)
            else:
                return visitor.visitChildren(self)




    def list_arg(self):

        localctx = BKOOLParser.List_argContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_list_arg)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 419
            self.match(BKOOLParser.LB)
            self.state = 421
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.INT_LIT) | (1 << BKOOLParser.FLOAT_LIT) | (1 << BKOOLParser.BOOL_LIT) | (1 << BKOOLParser.STRING_LIT) | (1 << BKOOLParser.NEW) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.ADD) | (1 << BKOOLParser.SUB) | (1 << BKOOLParser.NOT) | (1 << BKOOLParser.LB) | (1 << BKOOLParser.LP) | (1 << BKOOLParser.ID))) != 0):
                self.state = 420
                self.listexp()


            self.state = 423
            self.match(BKOOLParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListexpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def listexp(self):
            return self.getTypedRuleContext(BKOOLParser.ListexpContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_listexp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListexp" ):
                return visitor.visitListexp(self)
            else:
                return visitor.visitChildren(self)




    def listexp(self):

        localctx = BKOOLParser.ListexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_listexp)
        try:
            self.state = 430
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 425
                self.exp()
                self.state = 426
                self.match(BKOOLParser.COMMA)
                self.state = 427
                self.listexp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 429
                self.exp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class All_stateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_state(self):
            return self.getTypedRuleContext(BKOOLParser.Assign_stateContext,0)


        def if_state(self):
            return self.getTypedRuleContext(BKOOLParser.If_stateContext,0)


        def for_state(self):
            return self.getTypedRuleContext(BKOOLParser.For_stateContext,0)


        def break_state(self):
            return self.getTypedRuleContext(BKOOLParser.Break_stateContext,0)


        def continue_state(self):
            return self.getTypedRuleContext(BKOOLParser.Continue_stateContext,0)


        def return_state(self):
            return self.getTypedRuleContext(BKOOLParser.Return_stateContext,0)


        def invocation_state(self):
            return self.getTypedRuleContext(BKOOLParser.Invocation_stateContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_all_state

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAll_state" ):
                return visitor.visitAll_state(self)
            else:
                return visitor.visitChildren(self)




    def all_state(self):

        localctx = BKOOLParser.All_stateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_all_state)
        try:
            self.state = 439
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 432
                self.assign_state()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 433
                self.if_state()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 434
                self.for_state()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 435
                self.break_state()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 436
                self.continue_state()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 437
                self.return_state()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 438
                self.invocation_state()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_stateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def all_state(self):
            return self.getTypedRuleContext(BKOOLParser.All_stateContext,0)


        def list_state(self):
            return self.getTypedRuleContext(BKOOLParser.List_stateContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_list_state

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_state" ):
                return visitor.visitList_state(self)
            else:
                return visitor.visitChildren(self)




    def list_state(self):

        localctx = BKOOLParser.List_stateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_list_state)
        try:
            self.state = 445
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INT_LIT, BKOOLParser.FLOAT_LIT, BKOOLParser.BOOL_LIT, BKOOLParser.STRING_LIT, BKOOLParser.BREAK, BKOOLParser.CONTINUE, BKOOLParser.IF, BKOOLParser.NEW, BKOOLParser.FOR, BKOOLParser.RETURN, BKOOLParser.THIS, BKOOLParser.ADD, BKOOLParser.SUB, BKOOLParser.NOT, BKOOLParser.LB, BKOOLParser.LP, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 441
                self.all_state()
                self.state = 442
                self.list_state()
                pass
            elif token in [BKOOLParser.RP]:
                self.enterOuterAlt(localctx, 2)

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


    class List_decl_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl_var(self):
            return self.getTypedRuleContext(BKOOLParser.Decl_varContext,0)


        def list_decl_var(self):
            return self.getTypedRuleContext(BKOOLParser.List_decl_varContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_list_decl_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_decl_var" ):
                return visitor.visitList_decl_var(self)
            else:
                return visitor.visitChildren(self)




    def list_decl_var(self):

        localctx = BKOOLParser.List_decl_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_list_decl_var)
        try:
            self.state = 451
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.BOOLEAN, BKOOLParser.FLOAT, BKOOLParser.INT, BKOOLParser.STRING, BKOOLParser.VOID, BKOOLParser.FINAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 447
                self.decl_var()
                self.state = 448
                self.list_decl_var()
                pass
            elif token in [BKOOLParser.INT_LIT, BKOOLParser.FLOAT_LIT, BKOOLParser.BOOL_LIT, BKOOLParser.STRING_LIT, BKOOLParser.BREAK, BKOOLParser.CONTINUE, BKOOLParser.IF, BKOOLParser.NEW, BKOOLParser.FOR, BKOOLParser.RETURN, BKOOLParser.THIS, BKOOLParser.ADD, BKOOLParser.SUB, BKOOLParser.NOT, BKOOLParser.LB, BKOOLParser.RP, BKOOLParser.LP, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)

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


    class Block_stateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def list_decl_var(self):
            return self.getTypedRuleContext(BKOOLParser.List_decl_varContext,0)


        def list_state(self):
            return self.getTypedRuleContext(BKOOLParser.List_stateContext,0)


        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_block_state

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_state" ):
                return visitor.visitBlock_state(self)
            else:
                return visitor.visitChildren(self)




    def block_state(self):

        localctx = BKOOLParser.Block_stateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_block_state)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 453
            self.match(BKOOLParser.LP)
            self.state = 454
            self.list_decl_var()
            self.state = 455
            self.list_state()
            self.state = 456
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp_stateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def all_state(self):
            return self.getTypedRuleContext(BKOOLParser.All_stateContext,0)


        def block_state(self):
            return self.getTypedRuleContext(BKOOLParser.Block_stateContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp_state

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp_state" ):
                return visitor.visitExp_state(self)
            else:
                return visitor.visitChildren(self)




    def exp_state(self):

        localctx = BKOOLParser.Exp_stateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_exp_state)
        try:
            self.state = 460
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 458
                self.all_state()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 459
                self.block_state()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ExpContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ExpContext,i)


        def COLON(self):
            return self.getToken(BKOOLParser.COLON, 0)

        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_assign_state

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_state" ):
                return visitor.visitAssign_state(self)
            else:
                return visitor.visitChildren(self)




    def assign_state(self):

        localctx = BKOOLParser.Assign_stateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_assign_state)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 462
            self.exp()
            self.state = 463
            self.match(BKOOLParser.COLON)
            self.state = 464
            self.match(BKOOLParser.T__0)
            self.state = 465
            self.exp()
            self.state = 466
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(BKOOLParser.IF, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def THEN(self):
            return self.getToken(BKOOLParser.THEN, 0)

        def exp_state(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Exp_stateContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Exp_stateContext,i)


        def ELSE(self):
            return self.getToken(BKOOLParser.ELSE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_if_state

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_state" ):
                return visitor.visitIf_state(self)
            else:
                return visitor.visitChildren(self)




    def if_state(self):

        localctx = BKOOLParser.If_stateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_if_state)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 468
            self.match(BKOOLParser.IF)
            self.state = 469
            self.exp()
            self.state = 470
            self.match(BKOOLParser.THEN)
            self.state = 471
            self.exp_state()
            self.state = 474
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.state = 472
                self.match(BKOOLParser.ELSE)
                self.state = 473
                self.exp_state()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(BKOOLParser.FOR, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def COLON(self):
            return self.getToken(BKOOLParser.COLON, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ExpContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ExpContext,i)


        def DO(self):
            return self.getToken(BKOOLParser.DO, 0)

        def exp_state(self):
            return self.getTypedRuleContext(BKOOLParser.Exp_stateContext,0)


        def TO(self):
            return self.getToken(BKOOLParser.TO, 0)

        def DOWNTO(self):
            return self.getToken(BKOOLParser.DOWNTO, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_for_state

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_state" ):
                return visitor.visitFor_state(self)
            else:
                return visitor.visitChildren(self)




    def for_state(self):

        localctx = BKOOLParser.For_stateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_for_state)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 476
            self.match(BKOOLParser.FOR)
            self.state = 477
            self.match(BKOOLParser.ID)
            self.state = 478
            self.match(BKOOLParser.COLON)
            self.state = 479
            self.match(BKOOLParser.T__0)
            self.state = 480
            self.exp()
            self.state = 481
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.TO or _la==BKOOLParser.DOWNTO):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 482
            self.exp()
            self.state = 483
            self.match(BKOOLParser.DO)
            self.state = 484
            self.exp_state()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(BKOOLParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_break_state

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_state" ):
                return visitor.visitBreak_state(self)
            else:
                return visitor.visitChildren(self)




    def break_state(self):

        localctx = BKOOLParser.Break_stateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_break_state)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 486
            self.match(BKOOLParser.BREAK)
            self.state = 487
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(BKOOLParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_continue_state

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_state" ):
                return visitor.visitContinue_state(self)
            else:
                return visitor.visitChildren(self)




    def continue_state(self):

        localctx = BKOOLParser.Continue_stateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_continue_state)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 489
            self.match(BKOOLParser.CONTINUE)
            self.state = 490
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(BKOOLParser.RETURN, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_return_state

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_state" ):
                return visitor.visitReturn_state(self)
            else:
                return visitor.visitChildren(self)




    def return_state(self):

        localctx = BKOOLParser.Return_stateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_return_state)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 492
            self.match(BKOOLParser.RETURN)
            self.state = 493
            self.exp()
            self.state = 494
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Invocation_stateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def list_arg(self):
            return self.getTypedRuleContext(BKOOLParser.List_argContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_invocation_state

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInvocation_state" ):
                return visitor.visitInvocation_state(self)
            else:
                return visitor.visitChildren(self)




    def invocation_state(self):

        localctx = BKOOLParser.Invocation_stateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_invocation_state)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 496
            self.exp()
            self.state = 497
            self.match(BKOOLParser.DOT)
            self.state = 498
            self.match(BKOOLParser.ID)
            self.state = 499
            self.list_arg()
            self.state = 500
            self.match(BKOOLParser.SEMI)
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
        self._predicates[28] = self.exp2_sempred
        self._predicates[29] = self.exp3_sempred
        self._predicates[30] = self.exp4_sempred
        self._predicates[31] = self.exp5_sempred
        self._predicates[34] = self.exp8_sempred
        self._predicates[35] = self.exp9_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp2_sempred(self, localctx:Exp2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def exp3_sempred(self, localctx:Exp3Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def exp4_sempred(self, localctx:Exp4Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 2)
         

    def exp5_sempred(self, localctx:Exp5Context, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 2)
         

    def exp8_sempred(self, localctx:Exp8Context, predIndex:int):
            if predIndex == 9:
                return self.precpred(self._ctx, 2)
         

    def exp9_sempred(self, localctx:Exp9Context, predIndex:int):
            if predIndex == 10:
                return self.precpred(self._ctx, 2)
         




