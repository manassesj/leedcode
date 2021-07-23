class Product():

    def __init__(self, name, composition,calories):
        self.composition = composition
        self.calories = calories
        self.name = name

coke = Product("Coke", "", "")
pepsi = Product("Pepsi", "", "")
soda = Product("Soda", "", "")

products = {
            1 : [coke, 25, 1],
            2 : [pepsi, 35, 1],
            3 : [soda, 45, 1]
        }

class Machine():
    ''' A classe maquina terão os seguintes atributos, moedas que a maquina aceita, os produtos
    que a maquina possui (Reprensado por um dicionario onde, a chave é o numero do produto na maquina
    e uma lista de valores onde tem o produto em si, o seu valor e quantidade disponivel'''
    def __init__(self, products):
        self.coins = [1, 5, 10, 25]
        self.products = products
        self.sum = 0
    ''' Essa função vai esperar ate o usuario não inserir mais moedas, dentro da função
    é chamado mais duas funções auxiliares '''
    def waiting_for_coin(self):
        while True:
                coin = int(input("Insert de Coin"))
                if coin != "":
                    self.received_coin(coin)
                else:
                    product = int(input("Type the product number"))
                    self.select_product(product)
                    
    ''' Uma das funções auxiliares. Recebe o valor do moeda, caso não for valido printa uma mensagem
    de erro e se caso for valido soma essa moeda ao valor total '''
    def received_coin(self, coin):

        if coin not in self.coins: 
            return print("Coin no suported")
        else:
            self.sum += 1
    ''' Segunda função auxiliar, essa funções é responsavel por captar o numero do produto selecionado,
    caso o numero for invalido é printado um erro, caso o produto não tiver mais no estoque é printado
    um aviso que o produto esta esgotado e é dado a opção do usuario recolher o dinheiro de volta
    ou escolher outro produto e se o produto existir e estiver em estoque ele chama a função auxiliar
    que vai entregar o produto e o troco'''
    def select_product(self, product):

        if product not in self.products:
            return print("Product not found")
        else:
            if self.products[product][2] == 0:
                print("Sold out")
                product = input("Select another product or press refound")
                if(product == "refound"):
                    return self.refound()
                else:
                    return self.select_product(int(product))
            elif self.sum < self.products[product][1]:
                print("Insufficient money")
                return self.refound()
            else:
                self.drop_product(product)

    ''' Função que entrega o pruduto. Reduz um unidade da quantidade do produto que foi selecionado
        entrega o produto na bandeija da maquina e retorna o troco '''
    def drop_product(self, product):
        self.products[product][2] -= 1
        remaining_change = self.sum - self.products[product][1]

        print("Product {} on the tray bellow".format(self.products[product][0]))
        print("Remaining change: {}".format(remaining_change))

    ''' Função de refound. Entrega o dinheiro do usuario e reseta a soma da maquina '''
    def refound(self):
        print("Returning the money: {}".format(self.sum))
        self.sum = 0
        return True
    
    ''' Função que reseta a maquina. Reseta a soma e receber os novos suplementos '''
    def reset_machine(self, new_suplies):
        self.sum = 0
        self.products = new_suplies


