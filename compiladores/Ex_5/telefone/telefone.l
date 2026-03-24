%option noyywrap

DIGITO      [0-9]
DDD         [1-9]{DIGITO}
SEP         [ ]?
FIXO        {DDD}{SEP}(2|3|4|5){DIGITO}{3}-{DIGITO}{4}
CELULAR     {DDD}{SEP}9{DIGITO}{4}-{DIGITO}{4}
PAREN       \({DDD}\){SEP}(9{DIGITO}{4}-{DIGITO}{4}|(2|3|4|5){DIGITO}{3}-{DIGITO}{4})
NUM_LIMPO   {DDD}9{DIGITO}{8}

%%

{FIXO}      { printf("Telefone fixo válido: %s\n", yytext); }
{CELULAR}   { printf("Celular válido: %s\n", yytext); }
{PAREN}     { printf("Telefone com DDD válido: %s\n", yytext); }
{NUM_LIMPO} { printf("Celular (sem formatação) válido: %s\n", yytext); }
.           { /**/ }
\n          { /**/ }

%%

int main() {
    yylex();
    return 0;
}