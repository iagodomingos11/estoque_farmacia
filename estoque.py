# Licença: Uso demonstrativo, proibida a comercialização sem autorização.
# Autor: Iago Domingos Pinto (2025)

import json
import os

estoque = []

def salvar_estoque():
    with open("estoque.json", "w") as f:
        json.dump(estoque, f)

def carregar_estoque():
    global estoque
    if os.path.exists("estoque.json"):
        with open("estoque.json", "r") as f:
            estoque = json.load(f)

def adicionar_produto():
    nome = input("Nome do produto: ").strip()
    quantidade = int(input("Quantidade: "))
    preco = float(input("Preço (R$): "))
    produto = {"nome": nome, "quantidade": quantidade, "preco": preco}
    estoque.append(produto)
    salvar_estoque()
    print("Produto adicionado com sucesso!\n")

def remover_produto():
    nome = input("Nome do produto para remover: ").strip().lower()
    for produto in estoque:
        if produto["nome"].lower() == nome:
            estoque.remove(produto)
            salvar_estoque()
            print("Produto removido com sucesso!\n")
            return
    print("Produto não encontrado.\n")

def listar_estoque():
    if not estoque:
        print("Estoque vazio.\n")
        return
    for i, produto in enumerate(estoque, 1):
        print(f"{i}. Nome: {produto['nome']} | Qtd: {produto['quantidade']} | Preço: R${produto['preco']:.2f}")
    print()

def buscar_produto():
    nome = input("Buscar produto por nome: ").strip().lower()
    encontrados = [p for p in estoque if nome in p["nome"].lower()]
    if encontrados:
        for produto in encontrados:
            print(f"Nome: {produto['nome']} | Qtd: {produto['quantidade']} | Preço: R${produto['preco']:.2f}")
    else:
        print("Nenhum produto encontrado com esse nome.\n")

def menu():
    carregar_estoque()
    while True:
        print("\n=== Gerenciador de Estoque de Farmácia ===")
        print("1. Adicionar produto")
        print("2. Remover produto")
        print("3. Listar estoque")
        print("4. Buscar produto")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            remover_produto()
        elif opcao == "3":
            listar_estoque()
        elif opcao == "4":
            buscar_produto()
        elif opcao == "5":
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida, tente novamente.\n")

if __name__ == "__main__":
    menu()
