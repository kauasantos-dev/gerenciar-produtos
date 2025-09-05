class Produto:
    def __init__(self):
        self.__produtos = {}
    
    def set_adicionar(self, nome, preco):
        preco = self.preco(preco)
        nome = self.nome(nome)
        if nome in self.__produtos:
            raise ValueError("Este produto já se encontra na lista.\n")
        else:
            self.__produtos[nome] = preco
        print("Produto adicionado com sucesso!\n")
    
    def get_listar(self):
        if not self.__produtos:
            print("Nenhum produto cadastrado.\n")
        else:
          print("Lista de produtos: \n")
          for produto, preco in self.__produtos.items():
              print(f"{produto}: R${preco:.2f}\n")
    
    def get_buscar(self, nome):
        nome = self.nome(nome)
        if nome in self.__produtos:
            print("Produto encontrado: \n")
            valor = self.__produtos[nome]
            print(f"{nome}: R${valor:.2f}\n")
        else:
            print("Produto não encontrado.\n")
    
    def preco(self, preco):
        try:
            preco = float(preco)
        except ValueError:
            raise ValueError("O preço do produto deve conter somente números.")
        if preco <= 0:
            raise ValueError("O preço do produto não pode ser menor ou igual a 0 (zero).")
        return preco
        
    def nome(self, nome):
        for letra in nome:
            if not letra.isalpha() and not letra.isdigit():
                raise ValueError("O nome do produto não pode conter caracteres especiais.")
        return nome
    