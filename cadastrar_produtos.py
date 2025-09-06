import sys

class Produtos:
    def adicionar(self, nome, preco, estoque):
        nome = self.set_nome(nome)
        preco = self.set_preco(preco)
        estoque = self.set_estoque(estoque)
        try:
            with open("produtos.txt", "x") as arquivo:
                arquivo.write(f"{nome} | Preço: R${preco:.2f} | Estoque: {estoque}\n")
        except FileExistsError:
            with open("produtos.txt", "a") as arquivo:
                arquivo.write(f"{nome} | Preço: R${preco:.2f} | Estoque: {estoque}\n")
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
        nome = self.set_nome(nome)
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
        nome = self.set_nome(nome)
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
                        
    def set_nome(self, nome):
            if not nome.replace(" ", "").isalnum(): #letras e números
                raise ValueError("O nome do produto não deve conter caracteres especiais.")
            return nome.strip()
    
    def set_preco(self, preco):
        try:
            preco = float(preco)
        except ValueError:
            raise ValueError("O preço do produto deve conter apenas números.")
        if preco <= 0:
            raise ValueError("O preço do produto não pode ser menor ou igual a 0 (zero).")
        return preco
    
    def set_estoque(self, estoque):
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
    print("1- Ver produtos cadastrados\n2- Adicionar novo produto\n3- Buscar produto\n4- Excluir produto\n5- Sair\n")
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
              print("Err0: ", e, " Tente novamente.\n")

    elif opcao == '5':
        print("\nPrograma encerrado.")
        sys.exit(0)

    else:
        print("\nOpção inválida. Por favor, digite uma opção válida.\n")