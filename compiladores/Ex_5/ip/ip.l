%option noyywrap

DIGITO  [0-9]
OCTETO  (25[0-5]|2[0-4]{DIGITO}|1{DIGITO}{2}|[1-9]{DIGITO}|{DIGITO})
IP      {OCTETO}\.{OCTETO}\.{OCTETO}\.{OCTETO}

%%

{IP}    { printf("IP válido: %s\n", yytext); }
.       { /**/ }
\n      { /**/ }

%%

int main() {
    yylex();
    return 0;
}