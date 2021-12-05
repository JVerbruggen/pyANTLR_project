grammar JurjenLang ;
startRule: func EOF ;

func        : func_def '{' stats func_return '}' ;
func_def    : FUNC_KW IDENTIFIER ;
func_return : FUNC_RET retstat ;

stats   : stat* ;
stat    : ass ;

retstat : e | IDENTIFIER ;

ass : IDENTIFIER '=' e
    | IDENTIFIER '=' IDENTIFIER
    ;

e : e OPERATOR e |
    INT
    ;

FUNC_KW : 'func' ;
FUNC_RET : 'return' ;

INT : DIGIT+ ;
IDENTIFIER : ('a' .. 'z' | 'A' .. 'Z') ('a' .. 'z' | 'A' .. 'Z' | '0' .. '9' | '_')* ;
OPERATOR : '+' | '-' | '*' | '/' ;
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

fragment DIGIT : '0' .. '9' ;
fragment BIT : '0' .. '1' ;