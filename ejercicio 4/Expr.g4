grammar Expr;

root : expr EOF;

expr : EOF;


ID : [a-zA-Z_][a-zA-Z0-9_]*;

IGUAL : '=';

NUM : [0-9]+;

WS : [ \t\r\n]+ -> skip;