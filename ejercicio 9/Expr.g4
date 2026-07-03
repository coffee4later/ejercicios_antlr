grammar Expr;

root: expr EOF;

expr: EOF;
IF: 'if';

MAYOR_QUE: '>';
PAR_A: '(';
PAR_C: ')';

NUM: [0-9]+;


ID: [a-zA-Z]+;
WS: [ \t\r\n]+ -> skip;