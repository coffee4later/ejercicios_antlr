grammar Expr;

root: expr EOF;

expr: expr MAS term | expr POR term | term;
term: NUM;

NUM: [0-9]+;

MAS: '+';
POR: '*';

WS: [ \t\r\n]+ -> skip;