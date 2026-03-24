%option noyywrap

DIGITO      [0-9]
ISBN10      {DIGITO}{9}[0-9Xx]
ISBN13      (978|979){DIGITO}{10}
ISBN10_H    {DIGITO}+(-{DIGITO}+)+[-]?[0-9Xx]
ISBN13_H    (978|979)-{DIGITO}+(-{DIGITO}+)+
ISBN        ({ISBN10}|{ISBN13}|{ISBN10_H}|{ISBN13_H})

%%

{ISBN}  { printf("ISBN válido: %s\n", yytext); }
.       { /**/ }
\n      { /**/ }

%%

int main() {
    yylex();
    return 0;
}