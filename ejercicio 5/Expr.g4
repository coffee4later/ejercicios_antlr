grammar Expr;

root: expr EOF;

expr: EOF;
ID: [a-zA-Z]+;
STRING: '"' .*? '"';
WS: [ \t\r\n]+ -> skip;

