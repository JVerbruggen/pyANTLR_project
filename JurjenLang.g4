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

e : e OPERATOR e |
    INT |
    variable
    ;

variable : IDENTIFIER ;

FUNC_KW : 'func' ;
FUNC_RET : 'return' ;

INT : DIGIT+ ;
IDENTIFIER : ('a' .. 'z' | 'A' .. 'Z') ('a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_')* ;
OPERATOR : '+' | '-' | '*' | '/' ;
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

fragment DIGIT : '0' .. '9' ;
fragment BIT : '0' .. '1' ;