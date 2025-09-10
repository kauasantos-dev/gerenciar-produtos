import sys
import json
import os

base_dir = os.path.dirname(__file__)
save_to = os.path.join(base_dir, 'produtos.json')

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
            with open(save_to, "r", encoding="utf-8") as file:
                self.__lista = json.load(file)
                self.__lista.append(self.produto)
            with open(save_to, "w", encoding="utf-8") as file:
                json.dump(self.__lista, file, indent=2, ensure_ascii=False)
        print("\nProduto adicionado com sucesso!\n")
    
    @property
    def produtos(self):
        try:
            with open(save_to, "r", encoding="utf-8") as file:
                self.__lista = json.load(file)
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
            with open(save_to, "r", encoding="utf-8") as file:
                self.__lista = json.load(file)
                verificar = False
                for produto in self.__lista:
                    for chave, valor in produto.items():
                        if chave.lower() == 'produto':
                           if nome.lower() == valor.lower():
                               verificar = True
                               print("\nProduto encontrado:\n")
                               #if chave.lower() == 'produto':
                                #   print(f"{chave}: {valor} |", end=" ")
                               #elif chave.lower() == 'preço':
                                #   print(f"{chave}: R${valor:.2f} |", end=" ")
                               #elif chave.lower() == 'estoque':
                                #   print(f"{chave}: {valor}")
                if not verificar:
                   print("\nNenhum produto encontrado.\n")
        except FileNotFoundError:
            print("Erro: Não há produtos cadastrados.\n")

    def excluir(self, nome):
        nome = self.validar_nome(nome)
        try:
            verificar = False
            with open(save_to, "r", encoding="utf-8") as file:
                self.__lista = json.load(file)
                for i in range(len(self.__lista)):
                    for chave, valor in self.__lista[i].items():
                        if chave.lower() == 'produto':
                           if nome.lower() == valor.lower():
                                verificar = True
                                indice = i
                if verificar:
                    del self.__lista[indice]
                    print("Produto excluído com sucesso!\n")
                elif not verificar:
                    print("\nNenhum produto encontrado.\n")
                    return
            with open(save_to, "w", encoding="utf-8") as file:
                json.dump(self.__lista, file, indent=2, ensure_ascii=False)
        except FileNotFoundError:
            print("Erro: Não há produtos cadastrados.\n")

    def update_estoque(self, nome, estoque):
        nome = self.validar_nome(nome)
        estoque = self.validar_estoque(estoque)
        try:
          with open(save_to, "r", encoding="utf-8") as file:
            self.__lista = json.load(file)
            verificar = False
            for i in range(len(self.__lista)):
                for chave, valor in self.__lista[i].items():
                    if chave.lower() == 'produto':
                        if nome.lower() == valor.lower():
                            verificar = True
                    if chave.lower() == 'estoque' and verificar:
                        self.__lista[i][chave] = estoque
                if not verificar:
                        print("\nNenhum produto encontrado.\n")
                        return 
          with open(save_to, "w", encoding="utf-8") as file:
              json.dump(self.__lista, file, indent=2, ensure_ascii=False) 
              print("Estoque atualizado com sucesso!\n")
        except FileNotFoundError:
            print("Erro: Não há produtos cadastrados.\n")      

    def update_preco(self, nome, preco):  #mesma lógica de update_estoque
        nome = self.validar_nome(nome)
        preco = self.validar_preco(preco)
        try:
          with open(save_to, "r", encoding="utf-8") as file:
              self.__lista = json.load(file)
              verificar = False
              for i in range(len(self.__lista)):
                  for chave, valor in self.__lista[i]:
                     if chave.lower() == 'produto':
                         if nome.lower() == valor.lower():
                             verificar = True
                     if chave.lower() == 'preço' and verificar:
                         self.__lista[i][chave] = preco
              if not verificar:
                  print("\nNenhum produto encontrado.\n")
                  return
          with open(save_to, "w", encoding="utf-8") as file:
                  json.dump(self.__lista, file, indent=2, ensure_ascii=False)
                  print("\nPreço atualizado com sucesso.\n")
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
    print("\nSelecione uma opção abaixo (digite o número da opção):\n")
    print("[1]- Ver produtos cadastrados\n[2]- Adicionar novo produto\n[3]- Buscar produto\n[4]- Excluir produto\n[5]- Atualizar preço\n[6]- Atualizar estoque\n[7]- Sair\n")
    opcao = input()

    if opcao == '1':
        produtos.ver_produtos
        
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