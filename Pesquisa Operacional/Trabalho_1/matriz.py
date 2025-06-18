EPSILON = 1e-10

class Matriz:
    @staticmethod
    def multiplicar(A, B):
        if len(A[0]) != len(B):
            raise ValueError("Número de colunas de A deve ser igual ao número de linhas de B")
        linhaA, colunaB = len(A), len(B[0])
        colunaA = len(A[0])
        resultado = [[0 for _ in range(colunaB)] for _ in range(linhaA)]
        for i in range(linhaA):
            for j in range(colunaB):
                for k in range(colunaA):
                    resultado[i][j] += A[i][k] * B[k][j]
        return resultado
    
    @staticmethod
    def determinante(M):
        ordemMatriz = len(M)
        if ordemMatriz == 0:
            return 1 
        if ordemMatriz != len(M[0]):
            raise ValueError("Matriz deve ser quadrada")
        
        A = [linha[:] for linha in M]
        determinante = 1

        for i in range(ordemMatriz):
            colunaMax = i
            for k in range(i+1, ordemMatriz):
                if abs(A[k][i]) > abs(A[colunaMax][i]):
                    colunaMax = k
            if colunaMax != i:
                A[i], A[colunaMax] = A[colunaMax], A[i]
                determinante *= -1
            if abs(A[i][i]) < EPSILON:
                return 0
            determinante *= A[i][i]
            for j in range(i + 1, ordemMatriz):
                fator = A[j][i] / A[i][i]
                for k in range(i,ordemMatriz):
                    A[j][k] -= fator * A[i][k]
        return determinante
    
    @staticmethod
    def inversa(M):
        n = len(M)
        matrizAumentada = []
        for i in range(n):
            linha = M[i][:] + [0] * n
            linha[n + i] = 1
            matrizAumentada.append(linha)
        
        for i in range(n):
            colunaMax = i
            for k in range(i + 1, n):
                if abs(matrizAumentada[k][i]) > abs(matrizAumentada[colunaMax][i]):
                    colunaMax = k
            
            matrizAumentada[i], matrizAumentada[colunaMax] = matrizAumentada[colunaMax], matrizAumentada[i]
            
            if abs(matrizAumentada[i][i]) < 1e-10:
                raise ValueError("Matriz não invertível (determinante zero)")
            
            pivo = matrizAumentada[i][i]
            for j in range(2 * n):
                matrizAumentada[i][j] /= pivo
            
            for j in range(n):
                if i != j:
                    fator = matrizAumentada[j][i]
                    for k in range(2 * n):
                        matrizAumentada[j][k] -= fator * matrizAumentada[i][k]
        
        inversa = []
        for i in range(n):
            inversa.append(matrizAumentada[i][n:])
        
        return inversa
    
    @staticmethod
    def resolverSistema(A,b):
        ordemMatriz = len(A)
        matrizAumentada = [A[i][:] + [b[i]] for i in range(ordemMatriz)]
        for i in range(ordemMatriz):
            colunaMax = i
            for k in range(i + 1, ordemMatriz):
                if abs(matrizAumentada[k][i]) > abs(matrizAumentada[colunaMax][i]):
                    colunaMax = k
            matrizAumentada[i], matrizAumentada[colunaMax] = matrizAumentada[colunaMax], matrizAumentada[i]
            
            if abs(matrizAumentada[i][i]) < 1e-10:
                raise ValueError("Sistema não tem solução única")
            
            for j in range(i + 1, ordemMatriz):
                factor = matrizAumentada[j][i] / matrizAumentada[i][i]
                for k in range(i, ordemMatriz + 1):
                    matrizAumentada[j][k] -= factor * matrizAumentada[i][k]
        
        x = [0] * ordemMatriz
        for i in range(ordemMatriz - 1, -1, -1):
            x[i] = matrizAumentada[i][ordemMatriz]
            for j in range(i + 1, ordemMatriz):
                x[i] -= matrizAumentada[i][j] * x[j]
            x[i] /= matrizAumentada[i][i]
        
        return x