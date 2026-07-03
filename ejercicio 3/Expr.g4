grammar Expr;

root : expr EOF;

expr : EOF;

IF: 'if';

ID : [a-zA-Z_][a-zA-Z0-9_]*;

MAYORQUE : '>';

NUM : [0-9]+;

WS : [ \t\r\n]+ -> skip;