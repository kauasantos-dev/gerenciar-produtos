import sys
import json
import os

base_dir = os.path.dirname(__file__)
save_to = os.path.join(base_dir, 'lista_produtos.json')

class Produtos:
    def __init__(self):
        self.__lista = []

    def adicionar(self, nome, preco, estoque):
        nome = self.validar_nome(nome)
        preco = self.validar_preco(preco)
        estoque = self.validar_estoque(estoque)
        self.produto = {'Produto': nome, 'Preço': round(preco, 2), 'Estoque': estoque} 
        try:
            with open(save_to, "x", encoding="utf-8") as file:
                self.__lista.append(self.produto)
                json.dump(self.__lista, file, indent=2, ensure_ascii=False)
        except FileExistsError:          
            self.__lista = self.arquivo_r()
            self.__lista.append(self.produto)
            self.arquivo_w(self.__lista)
        print("\nProduto adicionado com sucesso!\n")
    
    def listar_produtos(self):
        try:
            self.__lista = self.arquivo_r()
            if not self.__lista:
                print("Erro: Não há produtos cadastrados.\n")
                return
            else:
                  print("\nProdutos cadastrados:\n")
                  for produto in self.__lista:
                      for chave, valor in produto.items():
                          if chave.lower() == 'produto':
                              print(f"{chave}: {valor} |", end=" ")
                          elif chave.lower() == 'preço':
                              print(f"{chave}: R${valor:.2f} |", end=" ")
                          elif chave.lower() == 'estoque':
                              print(f"{chave}: {valor}")
        except FileNotFoundError:
            print("Erro: Não há produtos cadastrados.\n")

    def buscar(self, nome):
        nome = self.validar_nome(nome)
        try:
            self.__lista = self.arquivo_r()
            verificar = False
            for i in range(len(self.__lista)):
                if nome.lower() == self.__lista[i]['Produto'].lower():
                    verificar = True
                    produto = self.__lista[i]
            if verificar:
               print("Produto encontrado:\n")
               for chave, valor in produto.items():
                  if chave.lower() == 'produto':
                     print(f"{chave}: {valor} |", end=" ")
                  elif chave.lower() == 'preço':
                     print(f"{chave}: R${valor:.2f} |", end=" ")
                  elif chave.lower() == 'estoque':
                     print(f"{chave}: {valor}")
                     return
            else:
                print("\nNenhum produto encontrado.\n")
                return
        except FileNotFoundError:
            print("Erro: Não há produtos cadastrados.\n")

    def excluir(self, nome):
        nome = self.validar_nome(nome)
        try:
            self.__lista = self.arquivo_r()
            verificar = False
            for i in range(len(self.__lista)):
                if nome.lower() == self.__lista[i]['Produto'].lower():
                    verificar = True
                    indice = i
                    break
            if verificar:
                del self.__lista[indice]
            else:
                print("\nNenhum produto encontrado.\n")
                return
            self.arquivo_w(self.__lista)
            print("\nProduto excluído com sucesso!\n")
        except FileNotFoundError:
            print("Erro: Não há produtos cadastrados.\n")     

    def atualizar(self, nome, numero, opcao):
        nome = self.validar_nome(nome)
        if opcao == '5':
          numero = self.validar_preco(numero)
        elif opcao == '6':
            numero = self.validar_estoque(numero)
        try:
              self.__lista = self.arquivo_r()
              verificar = False
              for i in range(len(self.__lista)):
                  if nome.lower() == self.__lista[i]['Produto'].lower():
                     verificar = True
                  if opcao == '5' and verificar:
                         self.__lista[i]['Preço'] = round(numero, 2)
                         print("\nPreço atualizado com sucesso!\n")
                         break
                  elif opcao == '6' and verificar:
                         self.__lista[i]['Estoque'] = numero
                         print("Estoque atualizado com sucesso!\n")
                         break
              if not verificar:
                  print("\nNenhum produto encontrado.\n")
                  return
              self.arquivo_w(self.__lista)
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
    
    def arquivo_r(self):
        with open(save_to, "r", encoding="utf-8") as file:
            return json.load(file)
    
    def arquivo_w(self, lista):
        with open(save_to, "w", encoding="utf-8") as file:
            json.dump(lista, file, indent=2, ensure_ascii=False)

produtos = Produtos()
print("===== GERENCIAMENTO DE PRODUTOS =====\n")
while True:
    print("\nSelecione uma opção abaixo (digite o número da opção):\n")
    print("[1]- Ver produtos cadastrados\n[2]- Adicionar novo produto\n[3]- Buscar produto\n[4]- Excluir produto\n[5]- Atualizar preço\n[6]- Atualizar estoque\n[7]- Sair\n")
    opcao = input()

    if opcao == '1':
        produtos.listar_produtos()
        
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
            produtos.atualizar(nome, preco, opcao)
            break
          except ValueError as e:
              print("Erro: ", e, " Tente novamente.\n")


    elif opcao == '6':
        while True:
           try:
              nome = input("Digite o nome do produto: ")
              estoque = input("Informe o novo estoque do produto: ")
              produtos.atualizar(nome, estoque, opcao)
              break
           except ValueError as e:
               print("Erro: ", e, " Tente novamente.\n")

    elif opcao == '7':
        print("\nPrograma encerrado.")
        sys.exit(0)

    else:
        print("\nOpção inválida. Por favor, digite uma opção válida.\n")