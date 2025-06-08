import pickle

from  matrizes.matriz_base import Matriz
from  matrizes.matriz_geral import MatrizGeral
from  matrizes.matriz_quadrada import MatrizQuadrada
from  matrizes.matriz_diagonal import MatrizDiagonal
from  matrizes.matrizTriangularInferior import MatrizTriangularInferior
from  matrizes.matrizTriangularSup import MatrizTriangularSuperior
matrizes = {}

def menu_principal():
    while True:
        print("\n=== CALCULADORA MATRICIAL ===")
        print("1. Inserir nova matriz manualmente")
        print("2. Inserir matriz de arquivo")
        print("3. Inserir matriz identidade")
        print("4. Imprimir matriz(ns)")
        print("5. Listar todas as matrizes")
        print("6. Alterar uma matriz")
        print("7. Remover uma matriz")
        print("8. Zerar a lista")
        print("9. Salvar lista")
        print("10. Carregar lista")
        print("11. Operações com matrizes")
        print("12. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1": inserir_matriz_manual()
        elif opcao == "4": imprimir_matrizes()
        elif opcao == "5": listar_matrizes()
        elif opcao == "7": remover_matriz()
        elif opcao == "8": matrizes.clear(); print("Lista zerada.")
        elif opcao == "9": salvar_lista()
        elif opcao == "10": carregar_lista()
        elif opcao == "11": menu_operacoes()
        elif opcao == "12": break
        else: print("Opção inválida.")

def inserir_matriz_manual():
    nome = input("Nome da matriz: ")
    tipo = input("Tipo (geral, quadrada, diagonal, tri_sup, tri_inf): ").lower()
    n = int(input("Linhas: "))
    m = int(input("Colunas: "))

    dados = []
    for i in range(n):
        linha = list(map(float, input(f"Linha {i+1}: ").split()))
        dados.append(linha)

    if tipo == "geral":
        matriz = MatrizGeral(dados)
    elif tipo == "quadrada":
        matriz = MatrizQuadrada(dados)
    elif tipo == "diagonal":
        matriz = MatrizDiagonal(dados)
    elif tipo == "tri_sup":
        matriz = MatrizTriangularSuperior(dados)
    elif tipo == "tri_inf":
        matriz = MatrizTriangularInferior(dados)
    else:
        print("Tipo inválido.")
        return

    matrizes[nome] = matriz
    print(f"Matriz {nome} inserida.")

def imprimir_matrizes():
    nome = input("Nome da matriz: ")
    if nome in matrizes:
        print(matrizes[nome])
    else:
        print("Não encontrada.")

def listar_matrizes():
    for nome, matriz in matrizes.items():
        print(f"{nome}: {type(matriz).__name__}, {matriz.linhas}x{matriz.colunas}")

def remover_matriz():
    nome = input("Nome da matriz a remover: ")
    if nome in matrizes:
        del matrizes[nome]
        print("Removida.")
    else:
        print("Não encontrada.")

def salvar_lista():
    nome = input("Nome do arquivo .pkl: ")
    with open(nome, "wb") as f:
        pickle.dump(matrizes, f)
    print("Lista salva.")

def carregar_lista():
    global matrizes
    nome = input("Nome do arquivo .pkl: ")
    with open(nome, "rb") as f:
        matrizes = pickle.load(f)
    print("Lista carregada.")

def menu_operacoes():
    print("\n=== OPERACOES ===")
    print("1. Soma A + B")
    print("2. Subtração A - B")
    print("3. Escalar * A")
    print("4. Multiplicação A x B")
    print("5. Transposição")
    print("6. Traço (quadrada)")
    print("7. Determinante (triangular)")
    opcao = input("Escolha: ")

    if opcao == "1":
        a, b, c = input("A B C (nomes): ").split()
        matrizes[c] = matrizes[a] + matrizes[b]
    elif opcao == "2":
        a, b, c = input("A B C (nomes): ").split()
        matrizes[c] = matrizes[a] - matrizes[b]
    elif opcao == "3":
        escalar = float(input("Escalar: "))
        a = input("Matriz A: ")
        c = input("Nome do resultado: ")
        matrizes[c] = escalar * matrizes[a]
    elif opcao == "4":
        a, b, c = input("A B C (nomes): ").split()
        matrizes[c] = matrizes[a] @ matrizes[b]
    elif opcao == "5":
        a = input("Matriz A: ")
        c = input("Nome do resultado: ")
        matrizes[c] = matrizes[a].transposta()
    elif opcao == "6":
        a = input("Matriz quadrada: ")
        print("Traço:", matrizes[a].traco())
    elif opcao == "7":
        a = input("Matriz triangular: ")
        print("Determinante:", matrizes[a].determinante())

if __name__ == "__main__":
    menu_principal()
   


