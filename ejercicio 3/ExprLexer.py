# Generated from Expr.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,5,35,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,
        0,1,1,1,1,5,1,17,8,1,10,1,12,1,20,9,1,1,2,1,2,1,3,4,3,25,8,3,11,
        3,12,3,26,1,4,4,4,30,8,4,11,4,12,4,31,1,4,1,4,0,0,5,1,1,3,2,5,3,
        7,4,9,5,1,0,4,3,0,65,90,95,95,97,122,4,0,48,57,65,90,95,95,97,122,
        1,0,48,57,3,0,9,10,13,13,32,32,37,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,
        0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,1,11,1,0,0,0,3,14,1,0,0,0,5,21,1,0,
        0,0,7,24,1,0,0,0,9,29,1,0,0,0,11,12,5,105,0,0,12,13,5,102,0,0,13,
        2,1,0,0,0,14,18,7,0,0,0,15,17,7,1,0,0,16,15,1,0,0,0,17,20,1,0,0,
        0,18,16,1,0,0,0,18,19,1,0,0,0,19,4,1,0,0,0,20,18,1,0,0,0,21,22,5,
        62,0,0,22,6,1,0,0,0,23,25,7,2,0,0,24,23,1,0,0,0,25,26,1,0,0,0,26,
        24,1,0,0,0,26,27,1,0,0,0,27,8,1,0,0,0,28,30,7,3,0,0,29,28,1,0,0,
        0,30,31,1,0,0,0,31,29,1,0,0,0,31,32,1,0,0,0,32,33,1,0,0,0,33,34,
        6,4,0,0,34,10,1,0,0,0,4,0,18,26,31,1,6,0,0
    ]

class ExprLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    IF = 1
    ID = 2
    MAYORQUE = 3
    NUM = 4
    WS = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'>'" ]

    symbolicNames = [ "<INVALID>",
            "IF", "ID", "MAYORQUE", "NUM", "WS" ]

    ruleNames = [ "IF", "ID", "MAYORQUE", "NUM", "WS" ]

    grammarFileName = "Expr.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


