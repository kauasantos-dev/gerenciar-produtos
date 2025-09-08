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
                arquivo.write(f"{self.dicionario['Produto']} | Preço: R${self.dicionario['Preço']:.2f} | Estoque: {self.dicionario['Estoque']}\n")
        except FileExistsError:          
            with open("produtos.txt", "a") as arquivo:
                arquivo.write(f"{self.dicionario['Produto']} | Preço: R${self.dicionario['Preço']:.2f} | Estoque: {self.dicionario['Estoque']}\n")
        print("\nProduto adicionado com sucesso!\n")
    
    def ver_produtos(self):
        try:
            with open("produtos.txt", "r") as arquivo:
                conteudo = arquivo.readlines()
                arquivo.seek(0)
                if not conteudo:
                    print("Erro: Não há produtos cadastrados.\n")
                    return
                else:
                  print("\nProdutos cadastrados:")
                  for linha in arquivo:
                      if linha:
                          print(linha.strip())
        except FileNotFoundError:
            print("Erro: Não há produtos cadastrados.\n")

    def buscar(self, nome):
        nome = self.validar_nome(nome)
        try:
            with open("produtos.txt", "r") as arquivo:
                for linha in arquivo:
                    partes = linha.strip().split(" | ")
                    if nome.lower() == partes[0].lower():
                        print("\nProduto encontrado:")
                        print(f"{linha}")
                        return
                print("\nNenhum produto encontrado.\n")
        except FileNotFoundError:
            print("Erro: Não há produtos cadastrados.\n")

    def excluir(self, nome):
        nome = self.validar_nome(nome)
        try:
            verificar = False
            with open("produtos.txt", "r+") as arquivo:
                lista = arquivo.readlines()
                for i in range(len(lista)):
                    partes = lista[i].strip().split(" | ")
                    if nome.lower() == partes[0].lower():
                        del lista[i]
                        print("Produto excluído com sucesso!\n")
                        verificar = True
                        break
            if not verificar:
                print("\nNenhum produto encontrado.\n")
                return
            with open("produtos.txt", "w") as arquivo:
                for produto in lista:
                    arquivo.write(f"{produto}")
        except FileNotFoundError:
            print("Erro: Não há produtos cadastrados.\n")

    def update_estoque(self, nome, estoque):
        nome = self.validar_nome(nome)
        estoque = self.validar_estoque(estoque)
        try:
          with open("produtos.txt", "r") as arquivo:
            lista = arquivo.readlines()
            verificar = False
            for i in range(len(lista)):
                partes = lista[i].strip().split(" | ") #o split vai seprar cada parte de acordo com o delimitador " | " e vai transformar numa lista
                if nome.lower() == partes[0].lower():
                    verificar = True
                    for j in range(len(partes)):
                        if partes[j].startswith("Estoque:"): #o startswith() verifica se partes[j] começa com o conteúdo que eu coloquei como parâmetro
                           partes[j] = f"Estoque: {estoque}"
                    lista[i] = " | ".join(partes) + "\n" #o join serve pra juntar os indices de uma lista em uma única string e colocar algo entre eles, nesse caso o " | "
                    break
            if not verificar: #se verificar for False
                print("Nenhum produto encontrado.\n")
                return   
          with open("produtos.txt", "w") as arquivo:
              arquivo.writelines(lista) #pega cada indice da lista e escreve em cada linha do arquivo 
              print("Estoque atualizado com sucesso!\n")
        except FileNotFoundError:
            print("Erro: Não há produtos cadastrados.\n")          

    def update_preco(self, nome, preco):  #mesma lógica de update_estoque
        nome = self.validar_nome(nome)
        preco = self.validar_preco(preco)
        try:
          with open("produtos.txt", "r") as arquivo:
              lista = arquivo.readlines()
              verificar = False
              for i in range(len(lista)):
                  partes = lista[i].strip().split(" | ")
                  if nome.lower() == partes[0].lower():
                      verificar = True
                      for j in range(len(partes)):
                          if partes[j].startswith("Preço:"):
                              partes[j] = f"Preço: R${preco:.2f}"
                      lista[i] = " | ".join(partes) + "\n"
                      break
              if not verificar:
                  print("Nenhum produto encontrado.\n")
                  return
          with open("produtos.txt", "w") as arquivo:
              arquivo.writelines(lista)
              print("\nPreço atualizado com sucesso!\n")
        except FileNotFoundError:
            print("Erro: Não há produtos cadastrados.\n")

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

produtos = Produtos()
print("===== GERENCIAMENTO DE PRODUTOS =====\n")
while True:
    print("Selecione uma opção abaixo (digite o número da opção):\n")
    print("[1]- Ver produtos cadastrados\n[2]- Adicionar novo produto\n[3]- Buscar produto\n[4]- Excluir produto\n[5]- Atualizar preço\n[6]- Atualizar estoque\n[7]- Sair\n")
    opcao = input()

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
            nome = input("Informe o nome do produto: ")
            preco = input("Informe o novo preço do produto: ")
            produtos.update_preco(nome, preco)
            break
          except ValueError as e:
              print("Erro: ", e, " Tente novamente.\n")


    elif opcao == '6':
        while True:
           try:
              nome = input("Digite o nome do produto: ")
              estoque = input("Informe o novo estoque do produto: ")
              produtos.update_estoque(nome, estoque)
              break
           except ValueError as e:
               print("Erro: ", e, " Tente novamente.\n")

    elif opcao == '7':
        print("\nPrograma encerrado.")
        sys.exit(0)

    else:
        print("\nOpção inválida. Por favor, digite uma opção válida.\n")