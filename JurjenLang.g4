grammar JurjenLang;
startRule: e ;

e : e '+' e |
    e '*' e |
    e '/' e |
    e '-' e |
    INT ;

INT : [0-9][0-9]* ;
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines