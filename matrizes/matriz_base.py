
"""
Este módulo define a classe Matriz, que representa uma matriz numérica e implementa
operações matriciais básicas como soma, subtração, multiplicação, transposição,
cálculo do traço e do determinante.

A classe garante que os dados fornecidos sejam válidos (numéricos e com dimensões consistentes)
e fornece uma interface intuitiva para manipulação de matrizes em Python.
"""

class Matriz:
    """
    Classe que representa uma matriz numérica e permite operações matriciais básicas.

    Esta classe implementa uma matriz como uma lista de listas de números (inteiros ou floats),
    e fornece métodos para realizar operações como soma, subtração, multiplicação, transposição,
    cálculo do traço e do determinante.

    A matriz deve ser retangular (todas as linhas com o mesmo número de colunas) e conter apenas
    valores numéricos.

    Atributos:
    ----------
    dados : list[list[float]]
        Lista de listas representando os elementos da matriz.
    linhas : int
        Número de linhas da matriz.
    colunas : int
        Número de colunas da matriz.

    Métodos:
    --------
    __str__() -> str:
        Retorna uma representação legível da matriz.
    __add__(matriz_b: Matriz) -> Matriz:
        Soma duas matrizes de mesma dimensão.
    __sub__(matriz_b: Matriz) -> Matriz:
        Subtrai duas matrizes de mesma dimensão.
    __mul__(matriz_b: Matriz) -> Matriz:
        Multiplica duas matrizes compatíveis.
    transposta() -> Matriz:
        Retorna a matriz transposta.
    """
    # - Caracteristicas:
    def __init__(self,dados):
        """
            Inicializa uma matriz com dados fornecidos.

            Parâmetros:
            dados: (list of list of numbers): Lista de listas representando as linhas da
            matriz

            ValueError: Se as linhas não tiverem o mesmo número de colunas
            ou se algum elemento não for numérico
        """
        #verificar o usuário inputou todas os dados das linhas
        if not all(len(linha) == len(max(dados)) for linha in dados):
            raise ValueError("Todas as linhas devem ter o mesmo numero de colunas")
        for linha in dados:
            for elemento in linha:
                if not isinstance(elemento,(int,float)):
                    raise ValueError("Todos os elementos da matriz devem ser dados do tipo "
                    "(int ou float)")
        #numeros
        self.dados = dados
        #numero de colunas
        self.colunas = len(dados[0])
        #numero de linhas
        self.linhas =  len(dados)
    # metodos da Matriz:
    #str
    def __str__(self):
        """
        Retorna uma representação em string da matriz, com colunas separadas por tabulação
        e linhas separadas por quebras de linha.

        Retorna:
        str: Representação legível da matriz.
        """
        #converte matriz em string
        #faz isso para cada elemento da lista de listas (cada linha da matriz)
        return '\n'.join(['\t'.join(map(str, linha)) for linha in self.dados])
    #soma
    def __add__(self,matriz_b):
        """
        Soma duas matrizes de mesma dimensão.

        Parâmetros:
        matriz_b (Matriz): Outra matriz a ser somada com esta.

        Retorna:
        Matriz: Nova matriz resultante da soma elemento a elemento.

        Levanta:
        ValueError: Se as matrizes não tiverem as mesmas dimensões.
        """
    #dados_soma e dados devem ter a mesma ordem
        if (self.linhas,self.colunas) != (matriz_b.linhas,matriz_b.colunas):
            if (self.linhas != matriz_b.linhas) & (self.colunas == matriz_b.colunas):
                raise ValueError("As matrizes devem ser de mesmo grau para serem somadas"
                " (número de linhas diferentes)")
            if (self.colunas != matriz_b.colunas) & (self.linhas == matriz_b.linhas):
                raise ValueError("As matrizes devem ser de mesmo grau para serem somadas"
                " (número de colunas diferentes)")
            else:
                raise ValueError("As matrizes devem ser de mesmo grau para serem somadas"
                " (número de colunas e linhas diferentes)")
        #se matrizes forem da mesma ordem soma os itens
        return Matriz([
            #soma linha o Aij com o item Bij
            [self.dados[i][j] + matriz_b.dados[i][j]
            #faz isso para todos os itens da matriz
            for j in range(self.colunas)]
            for i in range(self.linhas)
        ])
    #-subtracao
    def __sub__(self,matriz_b):
        """
        Subtrai duas matrizes de mesma dimensão.

        Parâmetros:
        matriz_b (Matriz): Outra matriz a ser somada com esta.

        Retorna:
        Matriz: Nova matriz resultante da subtração elemento a elemento.

        Levanta:
        ValueError: Se as matrizes não tiverem as mesmas dimensões.
        """
    #matriz_b e dados devem ter a mesma ordem
        if self.colunas != matriz_b.linhas:
            if (self.linhas != matriz_b.linhas) & (self.colunas == matriz_b.colunas):
                raise ValueError("As matrizes devem ser de mesmo grau" \
                " para serem somadas (número de linhas diferentes)")
            if (self.colunas != matriz_b.colunas) & (self.linhas == matriz_b.linhas):
                raise ValueError("As matrizes devem ser de mesmo grau" \
                " para serem somadas (número de colunas diferentes)")
            else:
                raise ValueError("As matrizes devem ser de mesmo grau" \
                " para serem somadas (número de colunas e linhas diferentes)")
        return Matriz([
            #soma linha o Aij com o item Bij
            [self.dados[i][j] - matriz_b.dados[i][j]
            #faz isso para todos os itens da matriz
            for j in range(self.colunas)]
            for i in range(self.linhas)
        ])
        #-multiplicacao
    def __mul__(self,matriz_b):
        """
        Multiplica duas matrizes compatíveis.

        Parâmetros:
        matriz_b (Matriz): Outra matriz a ser somada com esta.

        Retorna:
        Matriz: Nova matriz resultante da multiplicação elemento a elemento.

        Levanta:
        ValueError: Se as matrizes não tiverem as mesmas dimensões.
        """
    #dmatriz_b e dados devem ser compatíveis
        if self.colunas != matriz_b.linhas:
            raise ValueError("A matriz A deve ter o numero de colunas " \
            "igual ao numero de linhas da matriz B")
        resultado = [
            [
                #produto escalar de linha por coluna
                sum(self.dados[i][k]*matriz_b.dados[k][j]
                    #faz isso para todas colunas da matriz A
                     for k in range(self.colunas))
                #a mesma coisa para todas as colunas da matriz B
                for j in range(matriz_b.colunas)
            ]
            #repete o processo para todas as linhas
            for i in range(self.linhas)
        ]
        #Matriz resultado
        return Matriz(resultado)
    #-transposta
    def transposta(self):
        """
        Retorna a matriz transposta.

        A transposta de uma matriz é obtida trocando suas linhas por colunas.
        Ou seja, o elemento na posição (i, j) da matriz original passa a ocupar
        a posição (j, i) na matriz transposta.

        Retorna:
        Matriz: Uma nova instância da classe Matriz representando a transposta da matriz original.
        """
        #troca linhas (i) por colunas (j)
        return Matriz([[self.dados[j][i]
                        #faz isso para todos os elementos da linha
                        for j in range(self.linhas)]
                        #faz isso para tos os elementos da coluna
                        for i in range(self.colunas)])
