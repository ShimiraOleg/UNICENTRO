from matriz import Matriz

class Simplex:
    def __init__(self, A, B, C, tipoRestricao, isMax=False):
        self.validarEntrada(A, B, C, tipoRestricao)
        self.aOriginal = [linha[:] for linha in A]
        self.bOriginal = B[:]
        self.cOriginal = C[:]
        self.tipoRestricao = tipoRestricao[:]
        self.isMax = isMax
        self.tolerancia = 1e-10
        self.interacoesMax = 10000
        self.numIteracoesFaseI = 0
        self.numIteracoesFaseII = 0

        # Converter para minimização se necessário
        if isMax:
            self.cOriginal = [-c for c in self.cOriginal]
        
        self.prepararFormaPadrao()
    
    def validarEntrada(self, A, B, C, tipoRestricao):
        m = len(A)
        n = len(C)
        if not A or not B or not C:
            raise ValueError("Matrizes/vetores de entrada não podem estar vazios")
        
        if len(B) != m:
            raise ValueError(f"Incompatibilidade: {m} restrições mas {len(B)} valores em B")
        
        if len(tipoRestricao) != m:
            raise ValueError(f"Incompatibilidade: {m} restrições mas {len(tipoRestricao)} tipos")
        
        for i, linha in enumerate(A):
            if len(linha) != n:
                raise ValueError(f"Restrição {i+1}: esperadas {n} variáveis, encontradas {len(linha)}")
        
        tipos_validos = ["<=", ">=", "="]
        for i, tipo in enumerate(tipoRestricao):
            if tipo not in tipos_validos:
                raise ValueError(f"Tipo de restrição inválido na linha {i+1}: {tipo}")
    
    def prepararFormaPadrao(self):
        self.m = len(self.aOriginal)
        self.n = len(self.cOriginal)

        # Garantir b >= 0
        for i in range(self.m):
            if self.bOriginal[i] < 0:
                self.aOriginal[i] = [-a for a in self.aOriginal[i]]
                self.bOriginal[i] = -self.bOriginal[i]
                if self.tipoRestricao[i] == "<=":
                    self.tipoRestricao[i] = ">="
                elif self.tipoRestricao[i] == ">=":
                    self.tipoRestricao[i] = "<="        
        
        self.A = []
        self.numFolgas = 0
        self.numExcesso = 0
        self.indiceArtificial = []

        for i in range(self.m):
            linha = self.aOriginal[i][:] + [0.0] * self.m
            if self.tipoRestricao[i] == "<=":
                linha[self.n + i] = 1.0
                self.numFolgas += 1
            elif self.tipoRestricao[i] == ">=":
                linha[self.n + i] = -1.0
                self.numExcesso += 1
                self.indiceArtificial.append(i)
            elif self.tipoRestricao[i] == "=":
                self.indiceArtificial.append(i)
            self.A.append(linha)

        self.B = self.bOriginal[:]
        self.C = self.cOriginal + [0.0] * self.m
        self.totalVariaveis = self.n + self.m
    
    def calcularSimplex(self):
        print(f"Iniciando Simplex com {len(self.indiceArtificial)} variáveis artificiais")
        
        necessitaFaseI = any(tipo in [">=", "="] for tipo in self.tipoRestricao)
        
        if necessitaFaseI:
            print("Executando Fase I...")
            sucesso = self.faseI()
            if not sucesso:
                print("\nProblema infactível - não existe solução")
                return None
            print(f"Fase I concluída em {self.numIteracoesFaseI} iterações")
        else:
            print("Fase I não necessária - criando base trivial...")
            self.criarBaseTrivial()

        print("Executando Fase II...")
        solucao = self.faseII()
        
        if solucao is not None:
            print(f"Fase II concluída em {self.numIteracoesFaseII} iterações")
            self.imprimirSolucao(solucao)

        return solucao
    
    def criarBaseTrivial(self):
        """Cria base inicial quando todas as restrições são <="""
        self.base = list(range(self.n, self.n + self.m))
        self.naoBase = list(range(self.n))
        print(f"Base inicial: {self.base}")
        print(f"Não-base inicial: {self.naoBase}")
    
    def faseI(self):
        numArtificiais = len(self.indiceArtificial)
        print(f"Criando {numArtificiais} variáveis artificiais")
        
        # Expandir matriz A com variáveis artificiais
        aArtificial = []
        for i in range(self.m):
            linha = self.A[i][:]
            for j in range(numArtificiais):
                if i == self.indiceArtificial[j]:
                    linha.append(1.0)
                else:
                    linha.append(0.0)
            aArtificial.append(linha)
        
        # Função objetivo artificial: minimizar soma das variáveis artificiais
        cArtificial = [0.0] * self.totalVariaveis + [1.0] * numArtificiais
        
        # Criar base inicial artificial
        self.base = []
        self.naoBase = list(range(self.totalVariaveis))
        
        # Definir variáveis básicas
        indexVar = self.n
        for i in range(self.m):
            if self.tipoRestricao[i] == "<=":
                # Variável de folga é básica
                self.base.append(indexVar)
                self.naoBase.remove(indexVar)
            else:
                # Variável artificial é básica
                try:
                    indexArtificial = self.indiceArtificial.index(i)
                    self.base.append(self.totalVariaveis + indexArtificial)
                except ValueError:
                    # Fallback - usar variável de folga se possível
                    self.base.append(indexVar)
                    if indexVar in self.naoBase:
                        self.naoBase.remove(indexVar)
            indexVar += 1
        
        print(f"Base artificial inicial: {self.base}")
        
        # Salvar estado original
        aOriginal = self.A
        cOriginal = self.C
        numVarsOriginais = self.totalVariaveis
        
        # Usar problema artificial
        self.A = aArtificial
        self.C = cArtificial
        self.totalVariaveis += numArtificiais
        
        # Executar simplex na Fase I
        self.numIteracoesFaseI = 0
        while self.numIteracoesFaseI < self.interacoesMax:
            self.numIteracoesFaseI += 1
            
            solucaoBasica = self.calcularSolucaoBasica()
            if solucaoBasica is None:
                print(f"Falha ao calcular solução básica na iteração {self.numIteracoesFaseI}")
                return False
            
            # Verificar valor das variáveis artificiais
            valorArtificial = 0.0
            for i in range(self.m):
                if self.base[i] >= numVarsOriginais:
                    valorArtificial += solucaoBasica[i]
            
            custosRelativos = self.calcularCustosRelativos()
            if custosRelativos is None:
                print("Falha ao calcular custos relativos")
                return False
            
            k, cMin = self.encontrarVariavelEntrada(custosRelativos)
            
            # Teste de otimalidade
            if cMin >= -self.tolerancia:
                # Verificar se há variáveis artificiais básicas com valor positivo
                if valorArtificial > self.tolerancia:
                    print(f"Problema infactível: variáveis artificiais = {valorArtificial}")
                    return False
                
                # Fase I concluída com sucesso
                self.A = aOriginal
                self.C = cOriginal
                self.totalVariaveis = numVarsOriginais
                
                # Remover variáveis artificiais da base e não-base
                self.naoBase = [var for var in self.naoBase if var < numVarsOriginais]
                
                # Completar base se necessário
                while len(self.base) < self.m:
                    for var in range(numVarsOriginais):
                        if var not in self.base and var not in self.naoBase:
                            self.base.append(var)
                            break
                
                # Completar não-base
                for var in range(numVarsOriginais):
                    if var not in self.base and var not in self.naoBase:
                        self.naoBase.append(var)
                
                print(f"Fase I concluída. Base final: {self.base}")
                return True
            
            # Continuar iteração
            direcao = self.calcularDirecaoSimplex(k)
            if direcao is None:
                print("Falha ao calcular direção simplex")
                return False
            
            l, epsilon = self.determinarVariavelSaida(solucaoBasica, direcao)
            if l is None:
                print("Problema ilimitado na Fase I")
                return False
            self.atualizarBase(k, l)
        
        print("Número máximo de iterações atingido na Fase I")
        return False
    
    def faseII(self):
        self.numIteracoesFaseII = 0
        
        while self.numIteracoesFaseII < self.interacoesMax:
            self.numIteracoesFaseII += 1
            
            solucaoBasica = self.calcularSolucaoBasica()
            if solucaoBasica is None:
                print(f"Falha ao calcular solução básica na iteração {self.numIteracoesFaseII}")
                return None
            
            custosRelativos = self.calcularCustosRelativos()
            if custosRelativos is None:
                print("Falha ao calcular custos relativos")
                return None
            
            k, cMin = self.encontrarVariavelEntrada(custosRelativos)
            
            # Teste de otimalidade
            if cMin >= -self.tolerancia:
                return self.construirSolucaoCompleta(solucaoBasica)
            
            # Calcular direção simplex
            direcao = self.calcularDirecaoSimplex(k)
            if direcao is None:
                print("Falha ao calcular direção simplex")
                return None
            
            # Determinar variável de saída
            l, epsilon = self.determinarVariavelSaida(solucaoBasica, direcao)
            if l is None:
                print("Problema ilimitado - função objetivo tende a -∞")
                return None
            self.atualizarBase(k, l)
        
        print("Número máximo de iterações atingido na Fase II")
        return None
    
    def calcularSolucaoBasica(self):
        # Construir matriz básica B
        B = []
        for i in range(self.m):
            linha = []
            for j in range(self.m):
                if self.base[j] < len(self.A[i]):
                    linha.append(self.A[i][self.base[j]])
                else:
                    linha.append(0.0)
            B.append(linha)
        
        try:
            solucaoBasica = Matriz.resolverSistema(B, self.B)
            # Verificar factibilidade
            for valor in solucaoBasica:
                if valor < -self.tolerancia:
                    return None
            return solucaoBasica
        
        except ValueError:
            return None
    
    def calcularCustosRelativos(self):
        # Custos das variáveis básicas
        custosVariaveisBasicas = []
        for i in range(self.m):
            if self.base[i] < len(self.C):
                custosVariaveisBasicas.append(self.C[self.base[i]])
            else:
                custosVariaveisBasicas.append(0.0)
        
        # Construir matriz básica transposta
        B = []
        for i in range(self.m):
            linha = []
            for j in range(self.m):
                if self.base[j] < len(self.A[i]):
                    linha.append(self.A[i][self.base[j]])
                else:
                    linha.append(0.0)
            B.append(linha)
        
        # Transpor matriz
        bTransposta = [[B[j][i] for j in range(self.m)] for i in range(self.m)]
        
        try:
            lambdaVetor = Matriz.resolverSistema(bTransposta, custosVariaveisBasicas)
            custosRelativos = []
            for j in range(len(self.naoBase)):
                indexVar = self.naoBase[j]
                if indexVar < len(self.C):
                    # λ^T * a_j
                    lambdaA = sum(lambdaVetor[i] * self.A[i][indexVar] for i in range(self.m))
                    custoRelativo = self.C[indexVar] - lambdaA
                    custosRelativos.append(custoRelativo)
                else:
                    custosRelativos.append(0.0)
            
            return custosRelativos
        except ValueError as e:
            print(f"Erro ao calcular custos relativos: {e}")
            return None
    
    def encontrarVariavelEntrada(self, custosRelativos):
        if not custosRelativos:
            return None, 0
        
        cMin = min(custosRelativos)
        k = custosRelativos.index(cMin)
        return k, cMin
    
    def calcularDirecaoSimplex(self, k):
        indexVar = self.naoBase[k]
        
        # Construir matriz básica
        B = []
        for i in range(self.m):
            linha = []
            for j in range(self.m):
                if self.base[j] < len(self.A[i]):
                    linha.append(self.A[i][self.base[j]])
                else:
                    linha.append(0.0)
            B.append(linha)
        
        # Coluna da variável entrante
        colunaVariavelEntrante = []
        for i in range(self.m):
            if indexVar < len(self.A[i]):
                colunaVariavelEntrante.append(self.A[i][indexVar])
            else:
                colunaVariavelEntrante.append(0.0)
        
        try:
            y = Matriz.resolverSistema(B, colunaVariavelEntrante)
            return y
        except ValueError as e:
            print(f"Erro ao calcular direção simplex: {e}")
            return None
    
    def determinarVariavelSaida(self, solucaoBasica, y):
        razoes = []
        for i in range(self.m):
            if y[i] > self.tolerancia:
                razao = solucaoBasica[i] / y[i]
                razoes.append((razao, i))
        
        if not razoes:
            return None, None  # Problema ilimitado
        
        epsilon, l = min(razoes)
        return l, epsilon
    
    def atualizarBase(self, k, l):
        varEntrada = self.naoBase[k]
        varSaida = self.base[l]
        
        self.base[l] = varEntrada
        self.naoBase[k] = varSaida
        
        # Manter listas ordenadas para facilitar debugging
        self.base.sort()
        self.naoBase.sort()
    
    def construirSolucaoCompleta(self, solucaoBasica):
        x = [0.0] * self.totalVariaveis
        
        for i in range(self.m):
            if self.base[i] < len(x):
                x[self.base[i]] = solucaoBasica[i]
        
        return x
    
    def imprimirSolucao(self, x):
        print("\nSOLUÇÃO ÓTIMA ENCONTRADA")
        print("="*50)
        
        # Variáveis de decisão
        print("\nVariáveis de decisão:")
        for i in range(self.n):
            print(f"  x{i+1} = {x[i]:.6f}")
        
        # Valor ótimo
        valorOtimo = sum(self.cOriginal[i] * x[i] for i in range(self.n))
        if self.isMax:
            valorOtimo = -valorOtimo
        
        print(f"\nValor ótimo da função objetivo:")
        print(f"  Z = {valorOtimo:.6f}")
        
        # Status das restrições
        print("\nStatus das restrições:")
        for i in range(self.m):
            valorRestricao = sum(self.aOriginal[i][j] * x[j] for j in range(self.n))
            folga = self.bOriginal[i] - valorRestricao
            
            status = ""
            if abs(folga) < self.tolerancia:
                status = "ATIVA"
            elif self.tipoRestricao[i] == "<=":
                status = "INATIVA"
            elif self.tipoRestricao[i] == ">=":
                status = "INATIVA"
            elif self.tipoRestricao[i] == "=":
                status = "ATIVA"
            
            print(f"  Restrição {i+1}: {status} (folga = {folga:.6f})")
        
        print("="*50)