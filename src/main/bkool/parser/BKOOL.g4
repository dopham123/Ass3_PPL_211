grammar BKOOL;
//........................ID:1711035....................
@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: list_class_dec EOF ;

list_class_dec
    :   class_dec list_class_dec?
    ;

mptype
    :   primitive_type
    |   array_type
    ;

//=========================== 2: PROGRAM STRUCTURE ======================

//2.1 Class Declaration ######################################################################################
class_dec
    :   CLASS ID (EXTENDS ID)? LP list_member RP
    ;

list_member
    :   list_attrib_dec list_method_dec
    ;

//nullable list_attrib_dec
list_attrib_dec
    :   attrib_dec list_attrib_dec
    |
    ;

//nullable list_method_dec
list_method_dec
    :   method_dec list_method_dec
    |
    ;
//2.2 Attribute declaration ######################################################################################

decl_var
    :   FINAL mptype list_attrib_const SEMI
    |   mptype list_attrib_var SEMI
    ;

//attrib_dec
//    :   STATIC? FINAL mptype list_attrib_const SEMI
//    |   STATIC? mptype list_attrib_var SEMI
//    ;

attrib_dec
    :   STATIC? decl_var
    ;

list_attrib_const
    :   attrib_const (COMMA list_attrib_const)?
    ;

list_attrib_var
    :   attrib_var (COMMA list_attrib_var)?
    ;

attrib_const
    :   ID '=' exp
    ;

attrib_var
    :   ID ('=' exp)?
    ;
//2.3 Method declaration
method_dec
    :   STATIC mptype ID LB list_para? RB block_state
    |   mptype? ID LB list_para? RB block_state
    ;

list_para
    :   para_dec SEMI list_para
    |   para_dec
    ;

para_dec
    :   mptype list_id
    ;

list_id
    :   ID COMMA list_id
    |   ID
    ;
//
//constructer_method
//    :   ID LB list_para? RB block_state
//    ;

//=========================== 3: LEXICAL STRUCTURE ======================

//3.1 Character Set

//3.2 Comment
COMMENT: (BLOCK_COMMENT|SINGLE_COMMENT)+ -> skip ;

fragment BLOCK_COMMENT
        :   '/*' ('*' ~'/' | ~'*')* '*/'
        ;

fragment SINGLE_COMMENT
        :   '#' ~[\r\n]*
        ;

//3.7 Literal
//3.7.1 Integer Literal
INT_LIT
    :   [1-9]+ [0-9]*
    |   '0'
    ;

//3.7.2 Float Literal
fragment EXPONENT:  [eE] [-+]? [0-9]+ ;

fragment INTEGER_PART
             :  [1-9]+ [0-9]*
             |  '0'
             ;

FLOAT_LIT    :      INTEGER_PART EXPONENT
             |      INTEGER_PART DOT [0-9]* EXPONENT?
             ;

//3.7.3 Boolean Literal
BOOL_LIT    :       TRUE
            |       FALSE
            ;

//3.7.4 String Literals
fragment ESCAPE_SEQUENCES
            :       '\\' ('b'|'f'|'r'|'n'|'t'|'"'|'\\')
            ;

STRING_LIT  :       UNCLOSE_STRING '"' {self.text = self.text[1:-1]}
            ;

//3.7.5 Array Literals
array_lit   :       LP list_lit RP
            ;

list_lit    :       list_int
            |       list_float
            |       list_bool
            |       list_string
            ;

list_int    :       INT_LIT (COMMA list_int)?
            |       INT_LIT
            ;

list_float  :       FLOAT_LIT (COMMA list_float)?
            |       FLOAT_LIT
            ;

list_bool   :       BOOL_LIT (COMMA list_bool)?
            |       BOOL_LIT
            ;

list_string :       STRING_LIT (COMMA list_string)?
            |       STRING_LIT
            ;

//ARRAY_LIT   :       LP LIST_LIT RP
//            ;
//
//fragment LIST_LIT
//            :       INT_LIT (COMMA INT_LIT)*
//            |       FLOAT_LIT (COMMA FLOAT_LIT)*
//            |       BOOL_LIT (COMMA BOOL_LIT)*
//            |       STRING_LIT (COMMA STRING_LIT)*
//            ;

//=========================== 4: Type======================
//4.1 Primitive Type
common_type
    :   INT
    |   FLOAT
    |   BOOLEAN
    |   STRING
    ;

primitive_type
    :   common_type
    |   VOID
    ;

//4.2 Array type
array_type
    :   common_type LSB INT_LIT RSB
    ;


//=========================== 5: EXPRESSIONS======================

exp
    :   exp1 LTHAN exp1
    |   exp1 GTHAN exp1
    |   exp1 LEQUAL exp1
    |   exp1 GEQUAL exp1
    |   exp1
    ;

exp1
    :   exp2 EQUAL exp2
    |   exp2 NOT_EQUAL exp2
    |   exp2
    ;

exp2
    :   exp2 AND exp3
    |   exp2 OR exp3
    |   exp3
    ;

exp3
    :   exp3 ADD exp4
    |   exp3 SUB exp4
    |   exp4
    ;

exp4
    :   exp4 MUL exp5
    |   exp4 FDIV exp5
    |   exp4 IDIV exp5
    |   exp4 MOD exp5
    |   exp5
    ;

exp5
    :   exp5 CONCATE exp6
    |   exp6
    ;

exp6
    :   NOT exp6
    |   exp7
    ;

exp7
    :   SUB exp7
    |   ADD exp7
    |   exp8
    ;

exp8:   exp8 LSB exp RSB
    |   exp9
    ;

exp9:   exp9 DOT ID list_arg?
    |   exp10
    ;

exp10
    :  NEW ID list_arg
    |   exp11
    ;

exp11
    :   LB exp RB
    |   ID
    |   literals
    |   THIS
    ;

literals:       INT_LIT
        |       FLOAT_LIT
        |       BOOL_LIT
        |       STRING_LIT
        |       array_lit
        ;
//member access 5.6
//funcall
//    :   ID (LB listexp? RB)?
//    ;

list_arg
    :   LB listexp? RB
    ;

listexp
    :   exp COMMA listexp
    |   exp
    ;

//=========================== 7: STATEMENTS======================

all_state
    :   assign_state
    |   if_state
    |   for_state
    |   break_state
    |   continue_state
    |   return_state
    |   invocation_state
    ;

list_state
    :   all_state list_state
    |
    ;

list_decl_var
    :   decl_var list_decl_var
    |
    ;

block_state
    :   LP list_decl_var list_state RP
    ;

exp_state
    :   all_state
    |   block_state
    ;

assign_state
    :   exp COLON '=' exp SEMI
    ;

if_state
    :   IF exp THEN exp_state (ELSE exp_state)?
    ;

for_state
    :   FOR ID COLON '=' exp (TO|DOWNTO)  exp DO exp_state
    ;

break_state
    :   BREAK SEMI
    ;

continue_state
    :   CONTINUE SEMI
    ;

return_state
    :   RETURN exp SEMI
    ;

invocation_state
    :   exp DOT ID list_arg SEMI
    ;

//3.4 Keyword
BOOLEAN:    'boolean';
BREAK:      'break';
CLASS:      'class';
CONTINUE:   'continue';
DO:         'do';
ELSE:       'else';
EXTENDS:    'extends';
FLOAT:      'float';
IF:         'if';
INT:        'int';
NEW:        'new';
STRING:     'string';
THEN:       'then';
FOR:        'for';
RETURN:     'return';
TRUE:       'true';
FALSE:      'false';
VOID:       'void';
NIL:        'nil';
THIS:       'this';
FINAL:      'final';
STATIC:     'static';
TO:         'to';
DOWNTO:     'downto';

//3.5 Operator
ADD:        '+' ;
SUB:        '-' ;
MUL:        '*' ;
FDIV:       '/' ;
IDIV:       '\\' ;
MOD:        '%' ;
NOT_EQUAL:  '!=' ;
EQUAL:      '==' ;
LTHAN:      '<' ;
GTHAN:      '>' ;
LEQUAL:     '<=' ;
GEQUAL:     '>=' ;
OR:         '||' ;
AND:        '&&' ;
NOT:        '!' ;
CONCATE:    '^' ;

//3.6 Separator
LSB:        '[' ;
RSB:        ']' ;
COLON:      ':' ;
LB:         '(' ;
RB:         ')' ;
SEMI:       ';' ;
DOT:        '.' ;
COMMA:      ',' ;
RP:        '}' ;
LP:        '{' ;


//3.3 Identifier (note: put ID in the end of lexer declare, if not -> error)
ID: [_a-zA-Z]+ [_a-zA-Z0-9]* ;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: .
        {
               raise ErrorToken(self.text)
        }
        ;
UNCLOSE_STRING:
            '"' (~["\\] | ESCAPE_SEQUENCES)* {raise UncloseString(self.text[1:])};
ILLEGAL_ESCAPE:
        UNCLOSE_STRING '\\' ~[bfntr"\\] {raise IllegalEscape(self.text[1:])};