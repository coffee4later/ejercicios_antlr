grammar Expr;

root: expr EOF;

expr: EOF;

PAR_A: '(';
PAR_C: ')';

STRING: '"' .*? '"';

ID: [a-zA-Z]+;
WS: [ \t\r\n]+ -> skip;
