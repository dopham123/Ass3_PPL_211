# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2?")
        buf.write("\u01c9\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\3\2\3\2\3\3\3\3\6\3\u008c\n\3\r\3\16\3\u008d\3\3\3\3")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\7\4\u0098\n\4\f\4\16\4\u009b")
        buf.write("\13\4\3\4\3\4\3\4\3\5\3\5\7\5\u00a2\n\5\f\5\16\5\u00a5")
        buf.write("\13\5\3\6\6\6\u00a8\n\6\r\6\16\6\u00a9\3\6\7\6\u00ad\n")
        buf.write("\6\f\6\16\6\u00b0\13\6\3\6\5\6\u00b3\n\6\3\7\3\7\5\7\u00b7")
        buf.write("\n\7\3\7\6\7\u00ba\n\7\r\7\16\7\u00bb\3\b\6\b\u00bf\n")
        buf.write("\b\r\b\16\b\u00c0\3\b\7\b\u00c4\n\b\f\b\16\b\u00c7\13")
        buf.write("\b\3\b\5\b\u00ca\n\b\3\t\3\t\3\t\3\t\3\t\3\t\7\t\u00d2")
        buf.write("\n\t\f\t\16\t\u00d5\13\t\3\t\5\t\u00d8\n\t\5\t\u00da\n")
        buf.write("\t\3\n\3\n\5\n\u00de\n\n\3\13\3\13\3\13\3\f\3\f\3\f\3")
        buf.write("\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3!\3!\3!\3!\3")
        buf.write("!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3$\3$\3$\3$")
        buf.write("\3$\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+")
        buf.write("\3+\3,\3,\3,\3-\3-\3.\3.\3/\3/\3/\3\60\3\60\3\60\3\61")
        buf.write("\3\61\3\61\3\62\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65")
        buf.write("\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:\3;\3;\3<\3<\3=")
        buf.write("\3=\3>\3>\3?\6?\u01a7\n?\r?\16?\u01a8\3?\7?\u01ac\n?\f")
        buf.write("?\16?\u01af\13?\3@\6@\u01b2\n@\r@\16@\u01b3\3@\3@\3A\3")
        buf.write("A\3A\3B\3B\3B\7B\u01be\nB\fB\16B\u01c1\13B\3B\3B\3C\3")
        buf.write("C\3C\3C\3C\2\2D\3\3\5\4\7\2\t\2\13\5\r\2\17\2\21\6\23")
        buf.write("\7\25\2\27\b\31\t\33\n\35\13\37\f!\r#\16%\17\'\20)\21")
        buf.write("+\22-\23/\24\61\25\63\26\65\27\67\309\31;\32=\33?\34A")
        buf.write("\35C\36E\37G I!K\"M#O$Q%S&U\'W(Y)[*]+_,a-c.e/g\60i\61")
        buf.write("k\62m\63o\64q\65s\66u\67w8y9{:};\177<\u0081=\u0083>\u0085")
        buf.write("?\3\2\16\3\2\61\61\3\2,,\4\2\f\f\17\17\3\2\63;\3\2\62")
        buf.write(";\4\2GGgg\4\2--//\t\2$$^^ddhhppttvv\5\2C\\aac|\6\2\62")
        buf.write(";C\\aac|\5\2\13\f\17\17\"\"\4\2$$^^\2\u01d9\2\3\3\2\2")
        buf.write("\2\2\5\3\2\2\2\2\13\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2")
        buf.write("\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2")
        buf.write("\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2")
        buf.write("\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3")
        buf.write("\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2")
        buf.write("\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2")
        buf.write("\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3")
        buf.write("\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W")
        buf.write("\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2")
        buf.write("a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2")
        buf.write("\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2")
        buf.write("\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2")
        buf.write("\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085")
        buf.write("\3\2\2\2\3\u0087\3\2\2\2\5\u008b\3\2\2\2\7\u0091\3\2\2")
        buf.write("\2\t\u009f\3\2\2\2\13\u00b2\3\2\2\2\r\u00b4\3\2\2\2\17")
        buf.write("\u00c9\3\2\2\2\21\u00d9\3\2\2\2\23\u00dd\3\2\2\2\25\u00df")
        buf.write("\3\2\2\2\27\u00e2\3\2\2\2\31\u00e6\3\2\2\2\33\u00ee\3")
        buf.write("\2\2\2\35\u00f4\3\2\2\2\37\u00fa\3\2\2\2!\u0103\3\2\2")
        buf.write("\2#\u0106\3\2\2\2%\u010b\3\2\2\2\'\u0113\3\2\2\2)\u0119")
        buf.write("\3\2\2\2+\u011c\3\2\2\2-\u0120\3\2\2\2/\u0124\3\2\2\2")
        buf.write("\61\u012b\3\2\2\2\63\u0130\3\2\2\2\65\u0134\3\2\2\2\67")
        buf.write("\u013b\3\2\2\29\u0140\3\2\2\2;\u0146\3\2\2\2=\u014b\3")
        buf.write("\2\2\2?\u014f\3\2\2\2A\u0154\3\2\2\2C\u015a\3\2\2\2E\u0161")
        buf.write("\3\2\2\2G\u0164\3\2\2\2I\u016b\3\2\2\2K\u016d\3\2\2\2")
        buf.write("M\u016f\3\2\2\2O\u0171\3\2\2\2Q\u0173\3\2\2\2S\u0175\3")
        buf.write("\2\2\2U\u0177\3\2\2\2W\u017a\3\2\2\2Y\u017d\3\2\2\2[\u017f")
        buf.write("\3\2\2\2]\u0181\3\2\2\2_\u0184\3\2\2\2a\u0187\3\2\2\2")
        buf.write("c\u018a\3\2\2\2e\u018d\3\2\2\2g\u018f\3\2\2\2i\u0191\3")
        buf.write("\2\2\2k\u0193\3\2\2\2m\u0195\3\2\2\2o\u0197\3\2\2\2q\u0199")
        buf.write("\3\2\2\2s\u019b\3\2\2\2u\u019d\3\2\2\2w\u019f\3\2\2\2")
        buf.write("y\u01a1\3\2\2\2{\u01a3\3\2\2\2}\u01a6\3\2\2\2\177\u01b1")
        buf.write("\3\2\2\2\u0081\u01b7\3\2\2\2\u0083\u01ba\3\2\2\2\u0085")
        buf.write("\u01c4\3\2\2\2\u0087\u0088\7?\2\2\u0088\4\3\2\2\2\u0089")
        buf.write("\u008c\5\7\4\2\u008a\u008c\5\t\5\2\u008b\u0089\3\2\2\2")
        buf.write("\u008b\u008a\3\2\2\2\u008c\u008d\3\2\2\2\u008d\u008b\3")
        buf.write("\2\2\2\u008d\u008e\3\2\2\2\u008e\u008f\3\2\2\2\u008f\u0090")
        buf.write("\b\3\2\2\u0090\6\3\2\2\2\u0091\u0092\7\61\2\2\u0092\u0093")
        buf.write("\7,\2\2\u0093\u0099\3\2\2\2\u0094\u0095\7,\2\2\u0095\u0098")
        buf.write("\n\2\2\2\u0096\u0098\n\3\2\2\u0097\u0094\3\2\2\2\u0097")
        buf.write("\u0096\3\2\2\2\u0098\u009b\3\2\2\2\u0099\u0097\3\2\2\2")
        buf.write("\u0099\u009a\3\2\2\2\u009a\u009c\3\2\2\2\u009b\u0099\3")
        buf.write("\2\2\2\u009c\u009d\7,\2\2\u009d\u009e\7\61\2\2\u009e\b")
        buf.write("\3\2\2\2\u009f\u00a3\7%\2\2\u00a0\u00a2\n\4\2\2\u00a1")
        buf.write("\u00a0\3\2\2\2\u00a2\u00a5\3\2\2\2\u00a3\u00a1\3\2\2\2")
        buf.write("\u00a3\u00a4\3\2\2\2\u00a4\n\3\2\2\2\u00a5\u00a3\3\2\2")
        buf.write("\2\u00a6\u00a8\t\5\2\2\u00a7\u00a6\3\2\2\2\u00a8\u00a9")
        buf.write("\3\2\2\2\u00a9\u00a7\3\2\2\2\u00a9\u00aa\3\2\2\2\u00aa")
        buf.write("\u00ae\3\2\2\2\u00ab\u00ad\t\6\2\2\u00ac\u00ab\3\2\2\2")
        buf.write("\u00ad\u00b0\3\2\2\2\u00ae\u00ac\3\2\2\2\u00ae\u00af\3")
        buf.write("\2\2\2\u00af\u00b3\3\2\2\2\u00b0\u00ae\3\2\2\2\u00b1\u00b3")
        buf.write("\7\62\2\2\u00b2\u00a7\3\2\2\2\u00b2\u00b1\3\2\2\2\u00b3")
        buf.write("\f\3\2\2\2\u00b4\u00b6\t\7\2\2\u00b5\u00b7\t\b\2\2\u00b6")
        buf.write("\u00b5\3\2\2\2\u00b6\u00b7\3\2\2\2\u00b7\u00b9\3\2\2\2")
        buf.write("\u00b8\u00ba\t\6\2\2\u00b9\u00b8\3\2\2\2\u00ba\u00bb\3")
        buf.write("\2\2\2\u00bb\u00b9\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc\16")
        buf.write("\3\2\2\2\u00bd\u00bf\t\5\2\2\u00be\u00bd\3\2\2\2\u00bf")
        buf.write("\u00c0\3\2\2\2\u00c0\u00be\3\2\2\2\u00c0\u00c1\3\2\2\2")
        buf.write("\u00c1\u00c5\3\2\2\2\u00c2\u00c4\t\6\2\2\u00c3\u00c2\3")
        buf.write("\2\2\2\u00c4\u00c7\3\2\2\2\u00c5\u00c3\3\2\2\2\u00c5\u00c6")
        buf.write("\3\2\2\2\u00c6\u00ca\3\2\2\2\u00c7\u00c5\3\2\2\2\u00c8")
        buf.write("\u00ca\7\62\2\2\u00c9\u00be\3\2\2\2\u00c9\u00c8\3\2\2")
        buf.write("\2\u00ca\20\3\2\2\2\u00cb\u00cc\5\17\b\2\u00cc\u00cd\5")
        buf.write("\r\7\2\u00cd\u00da\3\2\2\2\u00ce\u00cf\5\17\b\2\u00cf")
        buf.write("\u00d3\5u;\2\u00d0\u00d2\t\6\2\2\u00d1\u00d0\3\2\2\2\u00d2")
        buf.write("\u00d5\3\2\2\2\u00d3\u00d1\3\2\2\2\u00d3\u00d4\3\2\2\2")
        buf.write("\u00d4\u00d7\3\2\2\2\u00d5\u00d3\3\2\2\2\u00d6\u00d8\5")
        buf.write("\r\7\2\u00d7\u00d6\3\2\2\2\u00d7\u00d8\3\2\2\2\u00d8\u00da")
        buf.write("\3\2\2\2\u00d9\u00cb\3\2\2\2\u00d9\u00ce\3\2\2\2\u00da")
        buf.write("\22\3\2\2\2\u00db\u00de\5\67\34\2\u00dc\u00de\59\35\2")
        buf.write("\u00dd\u00db\3\2\2\2\u00dd\u00dc\3\2\2\2\u00de\24\3\2")
        buf.write("\2\2\u00df\u00e0\7^\2\2\u00e0\u00e1\t\t\2\2\u00e1\26\3")
        buf.write("\2\2\2\u00e2\u00e3\5\u0083B\2\u00e3\u00e4\7$\2\2\u00e4")
        buf.write("\u00e5\b\f\3\2\u00e5\30\3\2\2\2\u00e6\u00e7\7d\2\2\u00e7")
        buf.write("\u00e8\7q\2\2\u00e8\u00e9\7q\2\2\u00e9\u00ea\7n\2\2\u00ea")
        buf.write("\u00eb\7g\2\2\u00eb\u00ec\7c\2\2\u00ec\u00ed\7p\2\2\u00ed")
        buf.write("\32\3\2\2\2\u00ee\u00ef\7d\2\2\u00ef\u00f0\7t\2\2\u00f0")
        buf.write("\u00f1\7g\2\2\u00f1\u00f2\7c\2\2\u00f2\u00f3\7m\2\2\u00f3")
        buf.write("\34\3\2\2\2\u00f4\u00f5\7e\2\2\u00f5\u00f6\7n\2\2\u00f6")
        buf.write("\u00f7\7c\2\2\u00f7\u00f8\7u\2\2\u00f8\u00f9\7u\2\2\u00f9")
        buf.write("\36\3\2\2\2\u00fa\u00fb\7e\2\2\u00fb\u00fc\7q\2\2\u00fc")
        buf.write("\u00fd\7p\2\2\u00fd\u00fe\7v\2\2\u00fe\u00ff\7k\2\2\u00ff")
        buf.write("\u0100\7p\2\2\u0100\u0101\7w\2\2\u0101\u0102\7g\2\2\u0102")
        buf.write(" \3\2\2\2\u0103\u0104\7f\2\2\u0104\u0105\7q\2\2\u0105")
        buf.write("\"\3\2\2\2\u0106\u0107\7g\2\2\u0107\u0108\7n\2\2\u0108")
        buf.write("\u0109\7u\2\2\u0109\u010a\7g\2\2\u010a$\3\2\2\2\u010b")
        buf.write("\u010c\7g\2\2\u010c\u010d\7z\2\2\u010d\u010e\7v\2\2\u010e")
        buf.write("\u010f\7g\2\2\u010f\u0110\7p\2\2\u0110\u0111\7f\2\2\u0111")
        buf.write("\u0112\7u\2\2\u0112&\3\2\2\2\u0113\u0114\7h\2\2\u0114")
        buf.write("\u0115\7n\2\2\u0115\u0116\7q\2\2\u0116\u0117\7c\2\2\u0117")
        buf.write("\u0118\7v\2\2\u0118(\3\2\2\2\u0119\u011a\7k\2\2\u011a")
        buf.write("\u011b\7h\2\2\u011b*\3\2\2\2\u011c\u011d\7k\2\2\u011d")
        buf.write("\u011e\7p\2\2\u011e\u011f\7v\2\2\u011f,\3\2\2\2\u0120")
        buf.write("\u0121\7p\2\2\u0121\u0122\7g\2\2\u0122\u0123\7y\2\2\u0123")
        buf.write(".\3\2\2\2\u0124\u0125\7u\2\2\u0125\u0126\7v\2\2\u0126")
        buf.write("\u0127\7t\2\2\u0127\u0128\7k\2\2\u0128\u0129\7p\2\2\u0129")
        buf.write("\u012a\7i\2\2\u012a\60\3\2\2\2\u012b\u012c\7v\2\2\u012c")
        buf.write("\u012d\7j\2\2\u012d\u012e\7g\2\2\u012e\u012f\7p\2\2\u012f")
        buf.write("\62\3\2\2\2\u0130\u0131\7h\2\2\u0131\u0132\7q\2\2\u0132")
        buf.write("\u0133\7t\2\2\u0133\64\3\2\2\2\u0134\u0135\7t\2\2\u0135")
        buf.write("\u0136\7g\2\2\u0136\u0137\7v\2\2\u0137\u0138\7w\2\2\u0138")
        buf.write("\u0139\7t\2\2\u0139\u013a\7p\2\2\u013a\66\3\2\2\2\u013b")
        buf.write("\u013c\7v\2\2\u013c\u013d\7t\2\2\u013d\u013e\7w\2\2\u013e")
        buf.write("\u013f\7g\2\2\u013f8\3\2\2\2\u0140\u0141\7h\2\2\u0141")
        buf.write("\u0142\7c\2\2\u0142\u0143\7n\2\2\u0143\u0144\7u\2\2\u0144")
        buf.write("\u0145\7g\2\2\u0145:\3\2\2\2\u0146\u0147\7x\2\2\u0147")
        buf.write("\u0148\7q\2\2\u0148\u0149\7k\2\2\u0149\u014a\7f\2\2\u014a")
        buf.write("<\3\2\2\2\u014b\u014c\7p\2\2\u014c\u014d\7k\2\2\u014d")
        buf.write("\u014e\7n\2\2\u014e>\3\2\2\2\u014f\u0150\7v\2\2\u0150")
        buf.write("\u0151\7j\2\2\u0151\u0152\7k\2\2\u0152\u0153\7u\2\2\u0153")
        buf.write("@\3\2\2\2\u0154\u0155\7h\2\2\u0155\u0156\7k\2\2\u0156")
        buf.write("\u0157\7p\2\2\u0157\u0158\7c\2\2\u0158\u0159\7n\2\2\u0159")
        buf.write("B\3\2\2\2\u015a\u015b\7u\2\2\u015b\u015c\7v\2\2\u015c")
        buf.write("\u015d\7c\2\2\u015d\u015e\7v\2\2\u015e\u015f\7k\2\2\u015f")
        buf.write("\u0160\7e\2\2\u0160D\3\2\2\2\u0161\u0162\7v\2\2\u0162")
        buf.write("\u0163\7q\2\2\u0163F\3\2\2\2\u0164\u0165\7f\2\2\u0165")
        buf.write("\u0166\7q\2\2\u0166\u0167\7y\2\2\u0167\u0168\7p\2\2\u0168")
        buf.write("\u0169\7v\2\2\u0169\u016a\7q\2\2\u016aH\3\2\2\2\u016b")
        buf.write("\u016c\7-\2\2\u016cJ\3\2\2\2\u016d\u016e\7/\2\2\u016e")
        buf.write("L\3\2\2\2\u016f\u0170\7,\2\2\u0170N\3\2\2\2\u0171\u0172")
        buf.write("\7\61\2\2\u0172P\3\2\2\2\u0173\u0174\7^\2\2\u0174R\3\2")
        buf.write("\2\2\u0175\u0176\7\'\2\2\u0176T\3\2\2\2\u0177\u0178\7")
        buf.write("#\2\2\u0178\u0179\7?\2\2\u0179V\3\2\2\2\u017a\u017b\7")
        buf.write("?\2\2\u017b\u017c\7?\2\2\u017cX\3\2\2\2\u017d\u017e\7")
        buf.write(">\2\2\u017eZ\3\2\2\2\u017f\u0180\7@\2\2\u0180\\\3\2\2")
        buf.write("\2\u0181\u0182\7>\2\2\u0182\u0183\7?\2\2\u0183^\3\2\2")
        buf.write("\2\u0184\u0185\7@\2\2\u0185\u0186\7?\2\2\u0186`\3\2\2")
        buf.write("\2\u0187\u0188\7~\2\2\u0188\u0189\7~\2\2\u0189b\3\2\2")
        buf.write("\2\u018a\u018b\7(\2\2\u018b\u018c\7(\2\2\u018cd\3\2\2")
        buf.write("\2\u018d\u018e\7#\2\2\u018ef\3\2\2\2\u018f\u0190\7`\2")
        buf.write("\2\u0190h\3\2\2\2\u0191\u0192\7]\2\2\u0192j\3\2\2\2\u0193")
        buf.write("\u0194\7_\2\2\u0194l\3\2\2\2\u0195\u0196\7<\2\2\u0196")
        buf.write("n\3\2\2\2\u0197\u0198\7*\2\2\u0198p\3\2\2\2\u0199\u019a")
        buf.write("\7+\2\2\u019ar\3\2\2\2\u019b\u019c\7=\2\2\u019ct\3\2\2")
        buf.write("\2\u019d\u019e\7\60\2\2\u019ev\3\2\2\2\u019f\u01a0\7.")
        buf.write("\2\2\u01a0x\3\2\2\2\u01a1\u01a2\7\177\2\2\u01a2z\3\2\2")
        buf.write("\2\u01a3\u01a4\7}\2\2\u01a4|\3\2\2\2\u01a5\u01a7\t\n\2")
        buf.write("\2\u01a6\u01a5\3\2\2\2\u01a7\u01a8\3\2\2\2\u01a8\u01a6")
        buf.write("\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9\u01ad\3\2\2\2\u01aa")
        buf.write("\u01ac\t\13\2\2\u01ab\u01aa\3\2\2\2\u01ac\u01af\3\2\2")
        buf.write("\2\u01ad\u01ab\3\2\2\2\u01ad\u01ae\3\2\2\2\u01ae~\3\2")
        buf.write("\2\2\u01af\u01ad\3\2\2\2\u01b0\u01b2\t\f\2\2\u01b1\u01b0")
        buf.write("\3\2\2\2\u01b2\u01b3\3\2\2\2\u01b3\u01b1\3\2\2\2\u01b3")
        buf.write("\u01b4\3\2\2\2\u01b4\u01b5\3\2\2\2\u01b5\u01b6\b@\2\2")
        buf.write("\u01b6\u0080\3\2\2\2\u01b7\u01b8\13\2\2\2\u01b8\u01b9")
        buf.write("\bA\4\2\u01b9\u0082\3\2\2\2\u01ba\u01bf\7$\2\2\u01bb\u01be")
        buf.write("\n\r\2\2\u01bc\u01be\5\25\13\2\u01bd\u01bb\3\2\2\2\u01bd")
        buf.write("\u01bc\3\2\2\2\u01be\u01c1\3\2\2\2\u01bf\u01bd\3\2\2\2")
        buf.write("\u01bf\u01c0\3\2\2\2\u01c0\u01c2\3\2\2\2\u01c1\u01bf\3")
        buf.write("\2\2\2\u01c2\u01c3\bB\5\2\u01c3\u0084\3\2\2\2\u01c4\u01c5")
        buf.write("\5\u0083B\2\u01c5\u01c6\7^\2\2\u01c6\u01c7\n\t\2\2\u01c7")
        buf.write("\u01c8\bC\6\2\u01c8\u0086\3\2\2\2\31\2\u008b\u008d\u0097")
        buf.write("\u0099\u00a3\u00a9\u00ae\u00b2\u00b6\u00bb\u00c0\u00c5")
        buf.write("\u00c9\u00d3\u00d7\u00d9\u00dd\u01a8\u01ad\u01b3\u01bd")
        buf.write("\u01bf\7\b\2\2\3\f\2\3A\3\3B\4\3C\5")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    COMMENT = 2
    INT_LIT = 3
    FLOAT_LIT = 4
    BOOL_LIT = 5
    STRING_LIT = 6
    BOOLEAN = 7
    BREAK = 8
    CLASS = 9
    CONTINUE = 10
    DO = 11
    ELSE = 12
    EXTENDS = 13
    FLOAT = 14
    IF = 15
    INT = 16
    NEW = 17
    STRING = 18
    THEN = 19
    FOR = 20
    RETURN = 21
    TRUE = 22
    FALSE = 23
    VOID = 24
    NIL = 25
    THIS = 26
    FINAL = 27
    STATIC = 28
    TO = 29
    DOWNTO = 30
    ADD = 31
    SUB = 32
    MUL = 33
    FDIV = 34
    IDIV = 35
    MOD = 36
    NOT_EQUAL = 37
    EQUAL = 38
    LTHAN = 39
    GTHAN = 40
    LEQUAL = 41
    GEQUAL = 42
    OR = 43
    AND = 44
    NOT = 45
    CONCATE = 46
    LSB = 47
    RSB = 48
    COLON = 49
    LB = 50
    RB = 51
    SEMI = 52
    DOT = 53
    COMMA = 54
    RP = 55
    LP = 56
    ID = 57
    WS = 58
    ERROR_CHAR = 59
    UNCLOSE_STRING = 60
    ILLEGAL_ESCAPE = 61

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "'boolean'", "'break'", "'class'", "'continue'", "'do'", 
            "'else'", "'extends'", "'float'", "'if'", "'int'", "'new'", 
            "'string'", "'then'", "'for'", "'return'", "'true'", "'false'", 
            "'void'", "'nil'", "'this'", "'final'", "'static'", "'to'", 
            "'downto'", "'+'", "'-'", "'*'", "'/'", "'\\'", "'%'", "'!='", 
            "'=='", "'<'", "'>'", "'<='", "'>='", "'||'", "'&&'", "'!'", 
            "'^'", "'['", "']'", "':'", "'('", "')'", "';'", "'.'", "','", 
            "'}'", "'{'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "INT_LIT", "FLOAT_LIT", "BOOL_LIT", "STRING_LIT", 
            "BOOLEAN", "BREAK", "CLASS", "CONTINUE", "DO", "ELSE", "EXTENDS", 
            "FLOAT", "IF", "INT", "NEW", "STRING", "THEN", "FOR", "RETURN", 
            "TRUE", "FALSE", "VOID", "NIL", "THIS", "FINAL", "STATIC", "TO", 
            "DOWNTO", "ADD", "SUB", "MUL", "FDIV", "IDIV", "MOD", "NOT_EQUAL", 
            "EQUAL", "LTHAN", "GTHAN", "LEQUAL", "GEQUAL", "OR", "AND", 
            "NOT", "CONCATE", "LSB", "RSB", "COLON", "LB", "RB", "SEMI", 
            "DOT", "COMMA", "RP", "LP", "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "COMMENT", "BLOCK_COMMENT", "SINGLE_COMMENT", 
                  "INT_LIT", "EXPONENT", "INTEGER_PART", "FLOAT_LIT", "BOOL_LIT", 
                  "ESCAPE_SEQUENCES", "STRING_LIT", "BOOLEAN", "BREAK", 
                  "CLASS", "CONTINUE", "DO", "ELSE", "EXTENDS", "FLOAT", 
                  "IF", "INT", "NEW", "STRING", "THEN", "FOR", "RETURN", 
                  "TRUE", "FALSE", "VOID", "NIL", "THIS", "FINAL", "STATIC", 
                  "TO", "DOWNTO", "ADD", "SUB", "MUL", "FDIV", "IDIV", "MOD", 
                  "NOT_EQUAL", "EQUAL", "LTHAN", "GTHAN", "LEQUAL", "GEQUAL", 
                  "OR", "AND", "NOT", "CONCATE", "LSB", "RSB", "COLON", 
                  "LB", "RB", "SEMI", "DOT", "COMMA", "RP", "LP", "ID", 
                  "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[10] = self.STRING_LIT_action 
            actions[63] = self.ERROR_CHAR_action 
            actions[64] = self.UNCLOSE_STRING_action 
            actions[65] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1]
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                           raise ErrorToken(self.text)
                    
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise UncloseString(self.text[1:])
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise IllegalEscape(self.text[1:])
     


