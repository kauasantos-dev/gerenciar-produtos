import sys

class Produtos:
    def __init__(self):
        self.dicionario = {}

    def adicionar(self, nome, preco, estoque):
        nome = self.validar_nome(nome)
        preco = self.validar_preco(preco)
        estoque = self.validar_estoque(estoque)
        self.dicionario = {'Produto': nome, 'Preço': preco, 'Estoque': estoque} 
        try:
            with open("produtos.txt", "x") as arquivo:
                arquivo.write(f"{self.dicionario['Produto']} | Preço: R${self.dicionario['Preço']:.2f} | Estoque: {self.dicionario['Estoque']:.2f}\n")
        except FileExistsError:          
            with open("produtos.txt", "a") as arquivo:
                arquivo.write(f"{self.dicionario['Produto']} | Preço: R${self.dicionario['Preço']:.2f} | Estoque: {self.dicionario['Estoque']:.2f}\n")
        print("\nProduto adicionado com sucesso!\n")
    
    def ver_produtos(self):
        try:
            with open("produtos.txt", "r") as arquivo:
                conteudo = arquivo.readlines()
                arquivo.seek(0)
                if not conteudo:
                    print("\nNão há produtos cadastrados.\n")
                    return
                else:
                  print("\nProdutos cadastrados:")
                  for linha in arquivo:
                      if linha:
                          print(linha.strip())
        except FileNotFoundError:
            print("\nNão há produtos cadastrados.\n")

    def buscar(self, nome):
        nome = self.validar_nome(nome)
        try:
            with open("produtos.txt", "r") as arquivo:
                for linha in arquivo:
                    if nome.lower() in linha.lower():
                        print("\nProduto encontrado:")
                        print(f"{linha}")
                        return
                print("\nNenhum produto encontrado.\n")
        except FileNotFoundError:
            print("\nNão há produtos cadastrados.\n")

    def excluir(self, nome):
        nome = self.validar_nome(nome)
        try:
            verificar = False
            with open("produtos.txt", "r+") as arquivo:
                lista = arquivo.readlines()
                for i in range(len(lista)):
                    if nome.lower() in lista[i].lower():
                        del lista[i]
                        print("Produto excluído com sucesso!\n")
                        verificar = True
                        break
            if not verificar == True:
                print("\nNenhum produto encontrado.\n")
                return
            with open("produtos.txt", "w") as arquivo:
                for produto in lista:
                    arquivo.write(f"{produto}")
        except FileNotFoundError:
            print("\nNão há produtos cadastrados.\n")

    def update_estoque(self, nome, estoque):
        nome = self.validar_nome(nome)
        estoque = self.validar_estoque(estoque)
        try:
          with open("produtos.txt", "r") as arquivo:
            lista = arquivo.readlines()
            fatiamento = ""
            produto = ""
            verificar = False
            for i in range(len(lista)):
                if nome.lower() in lista[i].lower():
                    verificar = True
                    linha = lista[i]
                    indice = i
                    for letra in linha:
                        if letra != "|":
                            fatiamento += letra
                        else:
                            produto += fatiamento + "|"
                            fatiamento = ""
                            if produto.count("|") == 2:
                                produto += f" Estoque: {estoque}\n"
                                break
            if verificar == False:
                print("Nenhum produto encontrado.\n")
                return
            del lista[indice]
            lista.append(produto)
          with open("produtos.txt", "w") as arquivo:
            for i in range(len(lista)):
                arquivo.write(lista[i])
            print("Estoque atualizado com sucesso!\n")
        except FileNotFoundError:
            print("Nenhum produto cadastrado.\n")          

    def validar_nome(self, nome):
            if not nome.replace(" ", "").isalnum(): #letras e números
                raise ValueError("O nome do produto não deve conter caracteres especiais.")
            return nome.strip()
    
    def validar_preco(self, preco):
        try:
            preco = float(preco)
        except ValueError:
            raise ValueError("O preço do produto deve conter apenas números.")
        if preco <= 0:
            raise ValueError("O preço do produto não pode ser menor ou igual a 0 (zero).")
        return preco
    
    def validar_estoque(self, estoque):
        try:
            estoque = int(estoque)
        except ValueError:
            raise ValueError("O estoque deve conter apenas números.")
        if estoque < 0:
            raise ValueError("O estoque não pode ser menor que 0 (zero).")
        return estoque

    print("===== GERENCIAMENTO DE PRODUTOS =====")
while True:
    print("\nSelecione uma opção abaixo (digite o número da opção):\n")
    print("1- Ver produtos cadastrados\n2- Adicionar novo produto\n3- Buscar produto\n4- Excluir produto\n5- Atualizar estoque\n6- Sair\n")
    opcao = input()
    produtos = Produtos()

    if opcao == '1':
        produtos.ver_produtos()
        
    elif opcao == '2':
        while True:
          try:
            nome = input("Digite o nome do produto: ")
            preco = input("Informe o preço do produto: ")
            estoque = input("Informe o estoque do produto: ")
            produtos.adicionar(nome, preco, estoque)
            break
          except ValueError as e:
            print("Erro: ", e, " Tente novamente.\n")

    elif opcao == '3':
        while True:
          try:
            nome = input("Digite o nome do produto: ")
            produtos.buscar(nome)
            break
          except ValueError as e:
              print("Erro: ", e, " Tente novamente.\n")

    elif opcao == '4':
        while True:
          try:
              nome = input("Informe o nome do produto: ")
              produtos.excluir(nome)
              break
          except ValueError as e:
              print("Erro: ", e, " Tente novamente.\n")

    elif opcao == '5':
        while True:
           try:
              nome = input("Digite o nome do produto: ")
              estoque = input("Informe o novo estoque do produto: ")
              produtos.update_estoque(nome, estoque)
              break
           except ValueError as e:
               print("Erro: ", e, " Tente novamente.\n")

    elif opcao == '6':
        print("\nPrograma encerrado.")
        sys.exit(0)

    else:
        print("\nOpção inválida. Por favor, digite uma opção válida.\n")