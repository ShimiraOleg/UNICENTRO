import re
import sys
from fractions import Fraction
from simplex import Simplex

def extrairTermos(expressao):
    padrao = r'([+-]?\s*(?:\d+(?:\.\d*)?|\d*\.\d+|\d+/\d+)?)\s*[a-zA-Z](\d+)'
    return re.findall(padrao, expressao)

def converterParaNumero(coeficienteString):
    coeficienteString = coeficienteString.replace(' ','')
    if coeficienteString in ('', '+'):
        return 1.0
    elif coeficienteString == '-':
        return -1.0
    
    if '/' in coeficienteString:
        try:
            fracao = Fraction(coeficienteString)
            return float(fracao)
        except(ValueError, ZeroDivisionError):
            raise ValueError(f"Fração inválida: {coeficienteString}")
    
    try:
        return float(coeficienteString)
    except(ValueError, ZeroDivisionError):
        raise ValueError(f"Fração inválida: {coeficienteString}")

def parseFuncaoObjetiva(linha, numVars):
    tipo = 'min' if 'min' in linha.lower() else 'max'
    coeficientes = [0.0] * numVars

    linhaLimpa = linha.lower()
    linhaLimpa = linhaLimpa.replace('min','').replace('max','')
    linhaLimpa = linhaLimpa.replace('z=','').replace('z =','')

    termos = extrairTermos(linhaLimpa)
    for coeficienteString, indexString in termos:
        index = int(indexString) - 1
        if index >= numVars:
            raise ValueError(f"Indice de variável fora do alcance: x{index+1}")
        coeficiente = converterParaNumero(coeficienteString)
        coeficientes[index] = coeficiente
    return coeficientes, tipo == 'max'

def parseRestricao(linha, numVars):
    operadores = ['<=', '>=', '=']
    operador = None
    for op in operadores:
        if op in linha:
            ladoEsquerdo, ladoDireito = linha.split(op, 1)
            operador = op
            break
    if operador is None:
        raise ValueError(f'restrição malformada - operador não encontrado: {linha}')
    
    coeficientes = [0.0] * numVars
    termos = extrairTermos(ladoEsquerdo)
    for coeficienteString, indexString in termos:
        index = int(indexString) - 1
        if index >= numVars:
            raise ValueError(f"Indice de variável fora do alcance: x{index+1}")
        coeficiente = converterParaNumero(coeficienteString)
        coeficientes[index] = coeficiente
    
    ladoDireitoValor = converterParaNumero(ladoDireito.strip())
    return coeficientes, ladoDireitoValor, operador

def contarVariaveis(linhas):
    indices = []
    for linha in linhas:
        par = re.finditer(r'[a-zA-Z](\d+)', linha)
        for p in par:
            indices.append(int(p.group(1)))
    return max(indices) if indices else 0

def validarProblema(A,B,C, tiposRestricoes):
    restricoes = len(A)
    varNum = len(C)

    if len(B) != restricoes:
        raise ValueError(f"Incompatibilidade: {restricoes} restrições mas {len(B)} valores em B")
    
    if len(tiposRestricoes) != restricoes:
        raise ValueError(f"Incompatibilidade: {restricoes} restrições mas {len(tiposRestricoes)} tipos")
    for i, linha in enumerate(A):
        if len(linha) != varNum:
            raise ValueError(f"Restrição {i+1}: esperadas {varNum} variáveis, encontradas {len(linha)}")

def imprimirProblema(C,A,B, tiposRestricoes, isMax):
    print("\nProblema formatado:")
    print("-" * 40)

    tipoObjetivo = "Maximizar" if isMax else "Minimizar"
    objetivoString = f"{tipoObjetivo} Z = "

    termosObjetivo = []
    for i, c in enumerate(C):
        if abs(c) < 1e-10:
            continue

        if c == 1.0:
            termo = f"x{i+1}"
        elif c == -1.0:
            termo = f"-x{i+1}"
        else:
            fracao = Fraction(c).limit_denominator(10000)
            if abs(float(fracao) - c) < 1e-10 and fracao.denominator != 1:
                termo = f"{fracao}x{i+1}"
            else:
                termo = f"{c:.1f}x{i+1}"
        if termosObjetivo and not termo.startswith('-'):
            termo = '+' + termo
        termosObjetivo.append(termo)
    objetivoString += ''.join(termosObjetivo) if termosObjetivo else "0"
    print(objetivoString)

    print("\nSujeito a:")
    for i in range(len(A)):
        termos = []
        for j, a in enumerate(A[i]):
            if a == 1.0:
                termo = f"x{j+1}"
            elif a == -1.0:
                termo = f"-x{j+1}"
            else:
                fracao = Fraction(a).limit_denominator(10000)
                if abs(float(fracao) - a) < 1e-10 and fracao.denominator != 1:
                    termo = f"{fracao}x{j+1}"
                else:
                    termo = f"{a}x{j+1}"
            if termos and not termo.startswith('-'):
                termo = "+" + termo
            termos.append(termo)
        restricaoString = ''.join(termos) if termos else "0"

        valorB = B[i]
        fracaoB = Fraction(valorB).limit_denominator(10000)
        if abs(float(fracaoB) - valorB) < 1e-10 and fracaoB.denominator != 1:
            stringB = str(fracaoB)
        else:
            stringB = str(valorB)
        
        print(f"  {restricaoString} {tiposRestricoes[i]} {stringB}")
    
    print(f"\n  x_i >= 0, i = 1,...,{len(C)}")

def resolverArquivo(nomeArquivo):
    try:
        with open(nomeArquivo, 'r', encoding='utf-8') as f:
            linhas = [linha.strip() for linha in f if linha.strip()]
    except FileNotFoundError:
        print(f"Erro: Arquivo '{nomeArquivo}' não encontrado.")
        return
    except Exception as e:
        print(f"Erro ao ler arquivo: {e}")
        return

    if not linhas:
        print("Erro: Arquivo está vazio.")
        return

    try:
        numVars = contarVariaveis(linhas)
        if numVars == 0:
            print("Erro: Nenhuma variável detectada.")
            return

        print(f"\nAnálise do arquivo: {nomeArquivo}")
        print(f"Variáveis detectadas: {numVars}")
        print(f"Restrições: {len(linhas) - 1}")

        funcaoObjetivo, isMax = parseFuncaoObjetiva(linhas[0], numVars)

        A = []
        B = []
        tipoRestricao = []
        
        for i, linha in enumerate(linhas[1:], 1):
            try:
                coefs, termo, tipo = parseRestricao(linha, numVars)
                A.append(coefs)
                B.append(termo)
                tipoRestricao.append(tipo)
            except ValueError as e:
                print(f"Erro na linha {i+1}: {e}")
                return
            
        validarProblema(A, B, funcaoObjetivo, tipoRestricao)
        imprimirProblema(funcaoObjetivo, A, B, tipoRestricao, isMax)

        print("\n" + "="*60)
        print("EXECUTANDO MÉTODO SIMPLEX")
        print("="*60)
        
        simplex = Simplex(A, B, funcaoObjetivo, tipoRestricao, isMax)
        resultado = simplex.calcularSimplex()
        
        if resultado is None:
           print("\nNão foi possível encontrar solução ótima.")
        
    except Exception as e:
        print(f"\nErro durante processamento: {e}")
        import traceback
        traceback.print_exc()

def main():
    resolverArquivo(sys.argv[1])
    return 0

if __name__ == "__main__":
    sys.exit(main())