%option noyywrap

LETRA       [a-zA-Z]
DIGITO      [0-9]
ALNUM       [a-zA-Z0-9]
DOMINIO     {ALNUM}+("."{ALNUM}+)+
PROTOCOLO   (https?|ftp)"://"
CAMINHO     ("/"{ALNUM}[a-zA-Z0-9._~:/?#\[\]@!$&\'()*+,;=%-]*)*

%%

{PROTOCOLO}{DOMINIO}{CAMINHO}   {
    printf("URL: %s\n", yytext);
}
.    { /**/ }
\n   { /**/ }

%%

int main() {
    yylex();
    return 0;
}