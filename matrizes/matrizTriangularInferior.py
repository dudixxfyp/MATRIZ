"""
módulo matriz_triangular_inferior

Este módulo define a classe MatrizTriangularInferior, que representa uma matriz
quadrada onde todos os elementos acima da diagonal principal são zero. A classe
herda de MatrizQuadrada e valida se a matriz fornecida atende a essa condição.
"""

from .matriz_quadrada import MatrizQuadrada
from .matriz_geral import MatrizGeral

class MatrizTriangularInferior(MatrizQuadrada):
    """
    Representa uma matriz triangular inferior,
    onde todos os elementos acima da diagonal principal são zero.

    Herda de:
        MatrizQuadrada: Classe base que representa uma matriz quadrada genérica.

    Lança:
        ValueError: Se algum elemento acima da diagonal principal for diferente de zero.
    """

    def __init__(self, dados):
        """
        Inicializa uma instância de MatrizTriangularInferior.

        Parâmetros:
            dados (list[list[float]]): Lista de listas representando os elementos da matriz.

        Lança:
            ValueError: Se a matriz não for triangular inferior
            (elementos acima da diagonal principal diferentes de zero).
        """
        super().__init__(dados)
        for i in range(self.linhas):
            for j in range(i + 1, self.colunas):
                if dados[i][j] != 0:
                    raise ValueError("A Matriz não é uma matriz triangular inferior")

    def determinante(self):
        """
        Calcula o determinante da matriz triangular inferior.

        Retorna:
            float: Produto dos elementos da diagonal principal.
        """
        return self.produto_diagonal()

    def __mul__(self, matriz_b):
        """
        Realiza a multiplicação da matriz triangular inferior por outra matriz.

        Parâmetros:
            matriz_b (Matriz): A matriz a ser multiplicada.

        Retorna:
            MatrizGeral: Resultado da multiplicação.

        Lança:
            ValueError: Se as dimensões das matrizes forem incompatíveis para multiplicação.
        """
        if self.colunas != matriz_b.linhas:
            raise ValueError("Dimensões incompatíveis para a multiplicação de matrizes")

        resultado = []
        for i in range(self.linhas):
            linha = []
            for j in range(matriz_b.colunas):
                soma = 0
                for k in range(i + 1):
                    soma += self.dados[i][k] * matriz_b.dados[k][j]
                linha.append(soma)
            resultado.append(linha)

        return MatrizGeral(resultado)

    def resolver_sistema(self, b):
        """
        Resolve um sistema linear do tipo Lx = b, onde L é uma matriz triangular inferior.

        Parâmetros:
            b (list[float]): Vetor de termos independentes.

        Retorna:
            list[float]: Solução do sistema.

        Lança:
            ValueError: Se o vetor b não tiver o mesmo número de linhas da matriz.
        """
        if len(b) != self.linhas:
            raise ValueError("Dimensões incompatíveis entre matriz e vetor.")
        x = [0] * self.linhas
        for i in range(self.linhas):
            soma = sum(self.dados[i][j] * x[j] for j in range(i))
            x[i] = (b[i] - soma) / self.dados[i][i]
        return x
 
