"""
módulo matriz_diagonal

Este módulo define a classe MatrizDiagonal, que representa uma matriz quadrada
com todos os elementos fora da diagonal principal iguais a zero. A classe herda
de MatrizQuadrada e adiciona validação para garantir que a matriz seja diagonal,
além de fornecer um método para calcular seu determinante.
"""
from .matriz_quadrada import MatrizQuadrada

class MatrizDiagonal(MatrizQuadrada):
    """
    Representa uma matriz diagonal, onde todos os elementos fora da diagonal principal são zero.

    Herda de:
        MatrizQuadrada: Classe base que representa uma matriz quadrada genérica.

    Lança:
        ValueError: Se algum elemento fora da diagonal principal for diferente de zero.
    """
    def __init__(self, dados):
        """
        Inicializa uma instância de MatrizDiagonal.

        Parâmetros:
            dados (list[list[float]]): Lista de listas representando os elementos da matriz.

        Lança:
            ValueError: Se a matriz não for diagonal
             (elementos fora da diagonal principal diferentes de zero).
        """
        super().__init__(dados)
        for i in range(self.linhas):
            for j in range(self.colunas):
                if i != j and dados[i][j] != 0:
                    raise ValueError("Não é uma Matriz Diagonal")           

    def determinante(self):
        """
        Calcula o determinante da matriz diagonal.

        Retorna:
            float: O produto dos elementos da diagonal principal.
        """
        det = 1
        for i in range(self.linhas):
            det *= self.dados[i][i]
        return det
