"""
Módulo que define a classe MatrizQuadrada, uma subclasse de Matriz, especializada
em operações com matrizes quadradas, como cálculo do traço, cofatores e determinante.

Classes:
    MatrizQuadrada: Representa uma matriz quadrada e fornece métodos específicos
    para operações matemáticas como traço e determinante.

Exceções:
    ValueError: Lançada quando a matriz fornecida não é quadrada.
"""
from .matriz_base import Matriz

class MatrizQuadrada(Matriz):
    """
    Representa uma matriz quadrada, herdando da classe base Matriz.

    Esta classe fornece métodos específicos para matrizes quadradas,
    como o cálculo do traço, cofatores e determinante.

    Métodos:
        traco(): Retorna o traço da matriz (soma da diagonal principal).
        _cofator(linha, coluna): Retorna a submatriz excluindo a linha e coluna especificadas.
        determinante(): Calcula o determinante da matriz via expansão de Laplace.
    """
    def __init__(self,dados):
        """
        Inicializa uma matriz quadrada com os dados fornecidos.

        Parâmetros:
            dados (list[list[float]]): Lista de listas representando a matriz.

        Levanta:
            ValueError: Se a matriz não for quadrada
            (número de linhas diferente do número de colunas).
        """
        if len(dados) !=len(dados[0]):
            raise ValueError("Matriz não é quadrada.")
        super().__init__(dados)
    def traco(self):
        """
        Calcula o traço da matriz.

        O traço é definido como a soma dos elementos da diagonal principal
        de uma matriz quadrada, ou seja, a soma dos elementos cujos índices
        de linha e coluna são iguais (posição [i][i]).

        Retorna:
        float: O valor do traço da matriz.

        Levanta:
        ValueError: Se a matriz não for quadrada
        (número de linhas diferente do número de colunas).
        """
        if self.linhas != self.colunas:
            raise ValueError("Método traço só pode ser calculado para matrizes quadradas")
        soma=0
        for i in range(self.linhas):
            soma += self.dados[i][i]
        return soma
    #cofator
    def _cofator(self, linha, coluna):
        """
        Calcula o cofator da matriz ao remover a linha e a coluna especificadas.

        Parâmetros:
            linha (int): Índice da linha a ser removida.
            coluna (int): Índice da coluna a ser removida.

        Retorna:
            MatrizQuadrada: A submatriz resultante da remoção da linha e coluna.
        """
        #Cria uma nova lista de listas (nova mariz) contendo:
        sub_matriz = [
            # - todas as linhas, exceto a 'linha' excluída
            [self.dados[i][j] for j in range(self.colunas) if j !=coluna]
            # - emcada linha, todos os elementos, exceto o da 'coluna' excluída
            for i in range(self.linhas) if i != linha
        ]

        return MatrizQuadrada(sub_matriz)
    #-determinante
    def determinante(self):
        """
        Calcula o determinante da matriz usando o método de Laplace (expansão por cofatores).

        Retorna:
            float: O valor do determinante da matriz.

        Levanta:
            ValueError: Se a matriz não for quadrada.
        """
        #Matriz 1X1
        if self.linhas ==1:
            return self.dados[0][0]
        #Matriz 2x2
        if self.linhas == 2:
            a,b = self.dados[0]
            c,d = self.dados[1]
            return a*d - b*c
        #Cálcula o determinante usando o método de Laplace
        det=0
        for j in range(self.colunas):
            cofator = self._cofator(0,j)
            det += ((-1)**j)*self.dados[0][j] * cofator.determinante()
        return det
    def produto_diagonal(self):
        produto = 1
        for i in range(self.linhas):
            produto *= self.dados[i][i]
        return produto