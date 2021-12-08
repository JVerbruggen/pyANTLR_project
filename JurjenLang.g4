grammar JurjenLang ;
startRule: func EOF ;

func        : func_def scope ;
func_def    : FUNC_KW IDENTIFIER ;
func_return : FUNC_RET retstat ;

scope   : '{' stats func_return? '}' ;

stats   : stat* ;
stat    : ass ;

retstat : e ;

ass : variable '=' e
    ;

e : prio_e |
    e OPERATOR_MD e |
    e OPERATOR_AS e |
    integer |
    variable
    ;

prio_e : '(' e ')' ;

variable    : IDENTIFIER ;
integer     : NUMBERS ;

FUNC_KW : 'func' ;
FUNC_RET : 'return' ;

NUMBERS : DIGIT+ ;
IDENTIFIER : ('a' .. 'z' | 'A' .. 'Z') ('a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_')* ;
OPERATOR_MD     : '*' | '/' ;
OPERATOR_AS     : '+' | '-' ;
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

fragment DIGIT : '0' .. '9' ;
fragment BIT : '0' .. '1' ;