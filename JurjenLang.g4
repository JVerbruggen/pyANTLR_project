grammar JurjenLang;
startRule: func;

func        : func_def '{' stats func_return '}' ;
func_def    : FUNC NAME ;
func_return : FUNC_RET retstat ;

stats   : stat* ;
stat    : ass ;

retstat : e | VAR ;

ass : VAR '=' e
    | VAR '=' VAR
    ;

e : e '+' e |
    e '*' e |
    e '/' e |
    e '-' e |
    INT
    ;

INT : [0-9]+ ;
VAR : [a-zA-Z]+ ;
NAME : [a-zA-Z]+ ;
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

FUNC : 'func' ;
FUNC_RET : 'return' ;